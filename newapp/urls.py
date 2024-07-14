from django.urls import path

from newapp.apps import NewappConfig
from newapp.views import render_home, render_contacts

app_name = NewappConfig.name
# urlpatterns = [path('', include("newapp.urls", namespace="newapp"))]
urlpatterns = [path('', render_home, name='home'), path('contacts/', render_contacts, name='contacts')]
