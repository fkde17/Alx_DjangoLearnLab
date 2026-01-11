from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
Book.objects.get(id=book.id)
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
