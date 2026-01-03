from django.urls import path, include

from .views import UpdatePasswordView

urlpatterns = [  
    path("update/", UpdatePasswordView, name='update_password'),  
]

