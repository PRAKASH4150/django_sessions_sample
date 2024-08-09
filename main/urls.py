from django.urls import path
from . import views

urlpatterns = [
    path('view-1/', views.view_1, name='view_1'),
    path('view-2/', views.view_2, name='view_2'),
    path('view-3/', views.view_3, name='view_3'),
]
