from django.shortcuts import render, redirect
from .models import FamilyMember

def add_member(request):
    family_members = FamilyMember.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        birth_year = request.POST['birth_year']
        death_year = request.POST.get('death_year', None)
        parent_id = request.POST.get('parent', None)
        parent = FamilyMember.objects.get(id=parent_id) if parent_id else None
        new_member = FamilyMember(name=name, gender=gender, birth_year=birth_year, death_year=death_year, parent=parent)
        new_member.save()
        return redirect('family_members')
    return render(request, 'tree_family/add_member.html', {'family_members': family_members})

def family_members(request):
    family_members = FamilyMember.objects.all()
    return render(request, 'tree_family/family_members.html', {'family_members': family_members})

def home(request):
    return render(request, 'tree_family/home.html')
