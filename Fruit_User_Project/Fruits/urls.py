from django.urls import path
from .views import Show_Add_Fruit,Update_Fruit
urlpatterns = [
    path('show_add_fruit/',Show_Add_Fruit,name='For listing all fruits'),
    path('update_fruit/<int:id>/',Update_Fruit,name='Updating the existing fruit'),
]