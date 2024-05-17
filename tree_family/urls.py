from django.urls import path
from .views import family_members
from . import views

urlpatterns = [
    path('family-members/', family_members, name='family_members'),
    path('', views.home, name='home'),
    path('add-member/', views.add_member, name='add_member'),
]
