# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# --------------------------------------------------
# 1. Function-based View: List all books
# --------------------------------------------------
def list_books(request):
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# --------------------------------------------------
# 2. Class-based View: Detail of a specific library
# --------------------------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'pk'  # default, but explicit for clarity