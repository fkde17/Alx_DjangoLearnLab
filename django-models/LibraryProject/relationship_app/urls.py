# relationship_app/urls.py
from django.urls import path
from .views import list_books
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]