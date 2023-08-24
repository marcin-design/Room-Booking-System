from django.contrib import admin
from django.urls import path
from conf_app import views as conf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', conf_views.DefaultPage.as_view()),
    path('room/list/', conf_views.list_of_rooms, name='list_of_rooms'),
    path('room/search/<int:room_id>/', conf_views.RoomDetailsView.as_view()),
    path('room/new/added/', conf_views.AfterAddingRoomView.as_view(), name='adding_room'),
    path('room/new/', conf_views.AddingRooms.as_view()),
    path('room/delete/<int:room_id>/', conf_views.DeleteRoomView.as_view()),
    path('room/edit/<int:room_id>/', conf_views.EditingRooms.as_view()),
    path('room/edit/edited/', conf_views.EditedView.as_view(), name='edited'),
    path('room/book/<int:room_id>/', conf_views.BookRoomView.as_view()),
]
