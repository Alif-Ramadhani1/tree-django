from django.urls import path
from .views import family_members

urlpatterns = [
    path('add-member/', add_member, name='add_member'),
    path('family-members/', family_members, name='family_members'),
]
