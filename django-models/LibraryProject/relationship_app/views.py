from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def list_books(request):
    """
    This view should render a simple text list of book titles and their authors.
    """
    # books = Book.objects.all()
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'books': books})
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
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('relationship_app:book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# Edit Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated.')
            return redirect('relationship_app:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# Delete Book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted.')
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})