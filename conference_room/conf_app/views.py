from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View
from .models import Room

class DefaultPage(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'base_html.html', context={})

class AddingRooms(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'add_room.html', {})

def list_of_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'listed_rooms.html', {'rooms': rooms})

def searching_by_id(request, room_id):
    rooms = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'rooms': rooms})

