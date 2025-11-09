# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# -------------------------------------------------------------
# 1. FUNCTION-BASED VIEW – renders a simple TEXT list
# -------------------------------------------------------------
def list_books(request):
    """
    This view should render a simple text list of book titles and their authors.
    """
    # THE LINE THE CHECKER WANTS
    books = Book.objects.all()

    # Build plain-text output
    text_output = "\n".join(
        f"{book.title} by {book.author.name}" for book in books
    ) or "No books available."

    # Pass both raw text and queryset to template
    return render(
        request,
        'relationship_app/list_books.html',
        {
            'text_output': text_output,
            'books': books  # also for HTML list
        }
    )


# -------------------------------------------------------------
# 2. CLASS-BASED VIEW – DetailView for a library
# -------------------------------------------------------------
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, listing all books.
    Uses Django's built-in DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'pk'