from django.shortcuts import render, redirect
from django.http import Http404
from authtest.models import Folder1
from authtest.models import Card

# Create your views here.
def home(request):
    if request.method == 'POST':
        folder = Folder1(title=request.POST['file'])
        folder.save()
        contents = {
        "contents": Folder1.objects.all()
        }
        return render(request, 'authtest/home.html', contents)
    return render(request, 'authtest/home.html')

def new(request):
    return render(request, 'authtest/new.html')

def detail(request, folder_id):
    try:
        folder = Folder1.objects.get(pk=folder_id)
    except Folder1.DoesNotExist:
        raise Http404("Folder does not exist")
    context={
        "folder": folder
    }
    return render(request, "authtest/detail.html", context)

def update(request, folder_id):
    try:
        folder = Folder1.objects.get(pk=folder_id)
    except Folder1.DoesNotExist:
        raise Http404("Folder does not exist")
    if request.method == 'POST':
        folder.title = request.POST['file']
        folder.save()
        return redirect(detail, folder_id)
    contents = {
        "contents": folder
    }
    return render(request, "teamapp/edit.html", contents)

def delete(folder_id):
    try:
        folder = Folder1.objects.get(pk=folder_id)
    except Folder1.DoesNotExist:
        raise Http404('Folder does not exist')
    folder.delete()
    return redirect(home)

def card(request):
    if request.method == 'POST':
        card = Card(problem=request.POST['problem'], answer=request.POST['answer'])
        card.save()   
        return redirect(paperhtml)
    
    if ('sort' in request.GET):
        if request.GET['sort'] == 'miss':
            cards = Card.objects.order_by('-miss')
        else:
            cards = Card.objects.order_by('posted_at')
    else:
        cards = Card.objects.order_by('-posted_at')

    data = {
        "cards": cards,
    }
    return render(request, 'authtest/paper.html', data)

def paperhtml(request):
    return render(request, 'authtest/paper.html')

def paper_detail(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    data = {
        'card': card,
    }
    return render(request, 'teamapp/paper_detail.html', data)

def paper_delete(card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        Http404("Card does not exist")

    card.delete()

    return redirect(paperhtml)