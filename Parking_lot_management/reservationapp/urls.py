from django.urls import path,include
from . import views

urlpatterns = [
    path('reserve/<int:parking_lot_no>/<int:block_no>/<int:floor_no>/<int:parking_slot_no>',views.parking_lot_index,name='parking_lot_index'),

]