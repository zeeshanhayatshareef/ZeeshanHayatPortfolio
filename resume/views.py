from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def Index(request):
    headers = Header.objects.all()
    abouts = About.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    certifications = Certification.objects.all()
    projects = MyProject.objects.all()
    addresses = Address.objects.all()
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts = Contact(name=name, email= email, subject=subject, message=message)
        contacts.save()
        messages.success(request, "message sent successfully")
    return render(request, 'index.html', {'headers':headers, 'abouts':abouts, 'skills':skills, 'educations':educations, 'experiences':experiences, 'certifications':certifications, 'projects':projects, 'addresses':addresses, 'contacts':contacts})




