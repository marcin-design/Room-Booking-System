from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from .models import Room, Book
from datetime import date, datetime

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
        return redirect("AfterAddingRoomView")

def list_of_rooms(request):
    rooms = Room.objects.all()
    if not rooms:
        message = ""
    return render(request, 'listed_rooms.html', {'rooms': rooms})

def searching_by_id(request, room_id):
    rooms = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'rooms': rooms})

class DeleteRoomView(View):
    def get(self, request, room_id):
        #Download the room based on the given id or return 404 if it doesn't exist
        delete_room = get_object_or_404(Room, id=room_id)
        delete_room.delete()
        #Add function name to redirect to needed view - list of rooms
        return redirect('list_of_rooms')

class EditedView(View):
    def get(self, request,  *args, **kwargs):
        return TemplateResponse(request, 'after_editing.html', {})

class EditingRooms(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'edit_room.html', {'room': room})

    def post(self, request, room_id, *args, **kwargs):
        room = Room.objects.get(pk=room_id)
        name = request.POST.get("name")
        capacity = request.POST.get("capacity", 0)
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("myCheckbox") == "on"
        if not name:
            return render(request, 'no_name.html')
        if capacity <= 0:
            return render(request, 'no_capacity.html')
        existing_room = Room.objects.filter(name=name).exclude(pk=room_id).first()
        if existing_room:
            return render(request, 'room_already_exists.html')
        room.name = name
        room.capacity = capacity
        room.projector = projector
        room.save()
        return redirect('edited')

class BookRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'book.html', {'room': room})

    def post(self, request, room_id, *args, **kwargs):
        room = Room.objects.get(pk=room_id)
        comment = request.POST.get("comment")
        book_date = request.POST.get("book_date")


        if Book.objects.filter(room=room, book_date=book_date):
            return render(request, "already_booked.html")
        if book_date < str(datetime.now().date()):
            return render(request, "incorrect_book_date.html")

        Book.objects.create(room=room, book_date=book_date, comment=comment)
        return redirect("list_of_rooms")

























