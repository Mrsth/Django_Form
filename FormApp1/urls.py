from django.urls import path
from FormApp1 import views

urlpatterns = [
    path('login/', views.login_handler),
    path('dash/',views.dash_handler),
    path('dash/logout/',views.logout_handler)   
]