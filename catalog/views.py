from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Blog, Version
from catalog.services import get_catalog_from_cache


def render_home(request):
    return render(request, "home.html")


def render_contacts(request):
    latest_products = Product.objects.order_by("-created_at")[:5]
    for product in latest_products:
        print(product)
    return render(request, "contacts.html", {"latest_products": latest_products})


class ProductListView(ListView, LoginRequiredMixin):
    model = Product

    def get_queryset(self):
        return get_catalog_from_cache().filter(publication_sign=True)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = context_data["object_list"]

        for product in products:
            active_version = product.versions.filter(
                indication_current_version=True
            ).first()
            if active_version:
                product.active_version = active_version

        return context_data


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.request.user == self.object.owner: # Можно убрать, так как это нужно только для примера
    #         self.object.views_counter += 1
    #         self.object.save()
    #         return self.object
    #     raise PermissionDenied# Можно убрать, так как это нужно только для примера


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog_list")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (
            user.has_perm("catalog.can_edit_category")
            and user.has_perm("catalog.can_edit_description")
            and user.has_perm("catalog.can_cancel_publication")
        ):
            return ProductModeratorForm
        raise PermissionDenied("У вас недостаточно прав для редактирования")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_list")


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(publication_sign=True)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
        "date_creation",
        "publication_sign",
    )
    success_url = reverse_lazy("catalog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
        "date_creation",
        "publication_sign",
    )
    success_url = reverse_lazy("catalog:blog_list")

    def get_success_url(self):
        return reverse(
            "catalog:blog_detail",
            kwargs={"pk": self.object.pk, "slug": self.object.slug},
        )


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")
