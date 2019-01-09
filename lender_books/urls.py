from .views import book_detail, book_list
from django.urls import path


urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:pk>', book_detail, name='book_detail'),
]
