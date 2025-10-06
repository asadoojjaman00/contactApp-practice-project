from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:id>/', views.update_contact, name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact')
]
