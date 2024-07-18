from django.urls import path

from catalog.apps import NewappConfig


app_name = NewappConfig.name
# urlpatterns = [path('', include("catalog.urls", namespace="catalog"))]
urlpatterns = [
    # path("", render_home, name="home"),
    # path("contacts/", render_contacts, name="contacts"),
]
