from django.urls import path
from driver_api import views 
 
urlpatterns = [ 
    path('driver/', views.driver_list, name='driver_list'),
    path('driver/<str:pk>/', views.driver_detail, name='driver_detail'),

    path('truck/', views.truck_list, name='truck_list'),
    path('truck/<str:pk>/', views.truck_detail, name='truck_detail'),
]
