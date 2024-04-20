from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_table, name='contactlist'),
    path('contactlist_tables', views.contactlist_tables, name='contactlist_tables')
]