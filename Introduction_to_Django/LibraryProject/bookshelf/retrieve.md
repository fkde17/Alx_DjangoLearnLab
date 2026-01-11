# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Display its details
print(book.id, book.title, book.author, book.publication_year)

# Expected Output:
# 1 1984 George Orwell 1949
