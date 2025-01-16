from django.urls import path
from .views import Show_Add_User,Update_User
urlpatterns = [
    path('show_add_user/',Show_Add_User,name='For listing all users'),
    path('update_user/<int:id>/',Update_User,name='Updating the existing user'),
]