from django.urls import path , include
from .views import BookList , BookViewSet
from rest_framework import DefaultRouter 


router = DefaultRouter()
router.register(r'books_all' , Bookviewset , basename = 'book_all')
urlpatterns = [
    path('books/' , BookList.as_view() , name = 'book-list'),
    path('api/' , include(router.urls)),
]