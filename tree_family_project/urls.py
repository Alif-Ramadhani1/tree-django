"""
URL configuration for tree_family_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tree_family.views import add_member, family_members   # Import family_members dari views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-member/', add_member, name='add_member'),
    path('family-members/', family_members, name='family_members'),   # Tambahkan path untuk family_members
]

