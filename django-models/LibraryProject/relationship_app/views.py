from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden



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

def check_role(role):
    def role_check(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return role_check


# Admin View
@user_passes_test(check_role('Admin'), login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Librarian View
@user_passes_test(check_role('Librarian'), login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member View
@user_passes_test(check_role('Member'), login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')