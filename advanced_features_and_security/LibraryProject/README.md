# 📚 LibraryProject - Permissions and Group Setup

This project implements detailed access control for Book management using Django's built-in permissions system, leveraging custom permissions defined on the `Book` model.

---

## Access Control Implementation

### 1. Custom Permissions (defined in `bookshelf/models.py`)

The following custom permissions are defined on the `Book` model:

| Permission Codename | Description | App Usage |
| :--- | :--- | :--- |
| `bookshelf.can_view` | Can view the list of books. | Enforced on `list_books` view. |
| `bookshelf.can_create` | Can create a new book instance. | Enforced on `add_book` view. |
| `bookshelf.can_edit` | Can modify existing book instances. | Enforced on `edit_book` view. |
| `bookshelf.can_delete` | Can remove book instances. | Enforced on `delete_book` view. |

### 2. User Groups and Access Roles

User groups are set up in the Django Admin to map specific permissions to user roles.

* **Viewers:** Granted `bookshelf.can_view`. (Read-only access)
* **Editors:** Granted `bookshelf.can_create` and `bookshelf.can_edit`. (Can add and modify books)
* **Admins:** Granted **all** custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`). (Full CRUD control)

### 3. Enforcement in Views

All critical book management views in `bookshelf/views.py` are protected using the **`@permission_required`** decorator with the `raise_exception=True` flag for strict enforcement.

Example:
```python
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # ... logic ...