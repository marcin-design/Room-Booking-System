from django.contrib import admin
from django.urls import path
from conf_app import views as conf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', conf_views.AddingRooms.as_view()),
]
