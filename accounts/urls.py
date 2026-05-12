from django.urls import path 


from . import views #trae todas las viws que estan a esta altura. No antes, no después, sino en la misma carpeta.

urlpatterns = [
    path('login/',),
    path('logout/'),
    path('register/'),
]