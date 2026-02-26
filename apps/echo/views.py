from django.shortcuts import render

def echo_room(request, room_name):
    return render(request, "echo/bingo.html", {
        "room_name": room_name
    })