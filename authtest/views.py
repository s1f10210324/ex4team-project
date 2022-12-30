from django.shortcuts import render, redirect
from authtest.models import Subject
from django.http import Http404
from authtest.models import Quiz

# Create your views here.

def home(request):
    if request.method == 'POST':
       subject = Subject(title = request.POST['title'])
       subject.save()
       return redirect(detail, subject.id)
    context = {
        "subjects": Subject.objects.all()
    }
    return render(request, "authtest/home.html", context)

def new(request):
    return render(request, 'authtest/new.html')

def detail(request, subject_id):
    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    context = {
        'subject': subject
    }
    return render(request, "authtest/detail.html", context)

def update(request, subject_id):
    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    if request.method == 'POST': #更新ボタンが押されたら
        subject.title = request.POST['title']
        subject.save()
        return redirect(detail, subject_id)
    context = {
        "subject": subject
    }
    return render(request, 'authtest/edit.html', context)

def delete(request, subject_id):
    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    subject.delete()
    return redirect(home)

def quiz(request, subject_id):
    return render(request, 'authtest/quiz.html')