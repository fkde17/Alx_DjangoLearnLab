from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
