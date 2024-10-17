from django.urls import path
from .views import Item

urlpatterns = [
    path("",Item.as_view() ),
]