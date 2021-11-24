from django.urls import path
from . import views

urlpatterns = [
    path('explore',views.explore,name='explore'),
    path('<int:id>',views.hotel_view,name='hotel_view'),
    path('<int:id>/<int:room_id>',views.room_view,name='room_view'),
    path('<int:id>/<int:room_id>/book',views.book_room,name='book_room'),
    path('<int:id>/<int:room_id>/checkout',views.checkout,name='checkout'),
    path('<int:id>/<int:room_id>/save',views.save_data,name='save_data')
]