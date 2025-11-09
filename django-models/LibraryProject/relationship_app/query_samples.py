from .models import Author, Library


def run_queries():
    print("="*60)
    print("DJANGO ORM RELATIONSHIP QUERIES")
    print("="*60)

    # --- 1. Query all books by a specific author ---
    print("\n1. All books by 'George Orwell':")
    author = Author.objects.get(name="George Orwell")
    books_by_author = author.books.all()
    for book in books_by_author:
        print(f"   - {book.title}")
    print()

    # --- 2. List all books in a specific library ---
    print("2. All books in 'Central City Library':")
    library_name = "Central City Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    for book in books_in_library:
        print(f"   - {book.title} by {book.author.name}")
    print()

    # --- 3. Retrieve the librarian for a library ---
    print("3. Librarian for 'Central City Library':")
    librarian = library.librarian
    print(f"   {librarian.name}")
    print()


if __name__ == "__main__":
    # Run this script after setting up sample data
    run_queries()