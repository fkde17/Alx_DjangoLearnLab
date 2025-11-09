from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book



def list_books(request):
    """
    This view should render a simple text list of book titles and their authors.
    """
    books = Book.objects.all()

    text_output = "\n".join(
        f"{book.title} by {book.author.name}" for book in books
    ) or "No books available."

    return render(
        request,
        'relationship_app/list_books.html',
        {
            'text_output': text_output,
            'books': books
        }
    )

class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, listing all books available in that library.
    Utilizes Django’s DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'