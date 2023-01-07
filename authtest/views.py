from django.shortcuts import render, redirect
from authtest.models import Subject
from django.http import Http404
from authtest.models import Quiz
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        act = User.objects.create_user(request.POST['name'], request.POST['address'], request.POST['password'])
        act.save()
        return redirect(home)
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
    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    contents = Quiz.objects.all()
    context = {
        'subject': subject,
        'qz': contents
    }
    return render(request, "authtest/quiz.html", context)

def start(request, subject_id):
    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    context = {
        'subject': subject
    }
    return render(request, "authtest/start.html", context)

def make(request, subject_id):
    if request.method == 'POST': #作成ボタンが押された場合の挙動
        qt = Quiz(value = request.POST['value'], question = request.POST['question'], answer = request.POST['answer'])
        qt.save()
        try:
            subject = Subject.objects.get(pk = subject_id)
        except Subject.DoesNotExist:
            raise Http404("Subject does not exist")
        context = {
            'subject': subject
        }
        return redirect(quiz, subject.id)
    else:
        try:
            subject = Subject.objects.get(pk = subject_id)
        except Subject.DoesNotExist:
            raise Http404("Subject does not exist")
        context = {
            'subject': subject
        }
        return render(request, "authtest/make.html", context)

def dt(request, subject_id, quiz_id):
    try:
        quiz = Quiz.objects.get(pk = quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")

    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")

    context = {
        'subject': subject,
        'quiz': quiz
    }
    return render(request, "authtest/dt.html", context)

def dl(request, subject_id, quiz_id):
    try:
        quiz = Quiz.objects.get(pk = quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")

    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    quiz.delete()

    contents = Quiz.objects.all()
    context = {
        'subject': subject,
        'qz': contents
    }
    return render(request, "authtest/quiz.html", context)

def ud(request, subject_id, quiz_id):
    try:
        quiz = Quiz.objects.get(pk = quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")

    try:
        subject = Subject.objects.get(pk = subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")

    if request.method == 'POST': #更新ボタンが押されたら
        quiz.value = request.POST['value']
        quiz.question = request.POST['question']
        quiz.answer = request.POST['answer']
        quiz.save()
        return redirect(dt, subject.id, quiz.id)
    context = {
        "subject": subject,
        "quiz": quiz
    }
    return render(request, 'authtest/ed.html', context)