from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View
from .models import Room

class AddingRooms(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'base_html.html', context={})

class ListOfRooms(View):
    def get(self, request, *args, **kwargs):
        context =
