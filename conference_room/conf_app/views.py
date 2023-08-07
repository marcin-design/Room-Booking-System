from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from .models import Room

class DefaultPage(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'base_html.html', context={})

class AfterAddingRoomView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'after_adding_room.html', {})

class AddingRooms(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity", 0)
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("myCheckbox") == "on"
        if not name:
            return render(request, 'no_name.html')
        if capacity <= 0:
            return render(request, 'no_capacity.html')
        if Room.objects.filter(name=name).first():
            return render(request, 'room_already_exists.html')
        Room.objects.create(name=name, capacity=capacity, projector=projector)
        return redirect("added/")

def list_of_rooms(request):
    rooms = Room.objects.all()
    if not rooms:
        message = ""
    return render(request, 'listed_rooms.html', {'rooms': rooms})

def searching_by_id(request, room_id):
    rooms = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'rooms': rooms})

class DeleteRoomView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'listed_rooms.html')


