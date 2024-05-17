from django.shortcuts import render
from .models import FamilyMember

def add_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = request.POST.get('parent', None)
        if parent_id:
            parent = FamilyMember.objects.get(id=parent_id)
        else:
            parent = None
        new_member = FamilyMember(name=name, parent=parent)
        new_member.save()
    return render(request, 'tree_family/add_member.html', {'family_members': family_members})

def family_members(request):
    family_members = FamilyMember.objects.all()
    return render(request, 'tree_family/family_members.html', {'family_members': family_members})

def home(request):
    return render(request, 'tree_family/home.html')
