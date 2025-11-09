# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),


    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', views.list_books, name='book_list'),
]