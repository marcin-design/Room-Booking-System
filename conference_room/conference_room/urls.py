from django.contrib import admin
from django.urls import path
from conf_app import views as conf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', conf_views.DefaultPage.as_view()),
    path('room/list/', conf_views.list_of_rooms, name='list_of_rooms'),
    path('room/search/<int:room_id>/', conf_views.searching_by_id),
]
