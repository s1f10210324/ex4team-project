from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "study/index.html")

def room(request, room_name):
    return render(request, "study/room.html", {"room_name": room_name}) # roomメソッドがroom_nameと一緒に呼ばれると、study/room.htmlを使って画面表示

