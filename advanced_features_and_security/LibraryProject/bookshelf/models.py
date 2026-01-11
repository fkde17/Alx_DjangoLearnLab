from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# --- ADD THIS MANAGER CLASS (Step 3) ---
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth=None, profile_photo=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password=password, **extra_fields)

# --- UPDATE YOUR EXISTING USER MODEL (Step 1 Completion) ---
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.FileField(upload_to='profile_photos/', null=True, blank=True) # Using FileField based on your restrictions

    # LINK THE MANAGER HERE
    objects = CustomUserManager() 

    def __str__(self):
        return self.username


# ---- Role Check Functions ----
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# ---- Admin View ----
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# ---- Librarian View ----
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# ---- Member View ----
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Automatically create a UserProfile whenever a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Save the UserProfile whenever the User object is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ... (all your existing imports and CustomUser, CustomUserManager classes) ...

# ... (all your existing Role Check Functions) ...
# ... (all your existing UserProfile, Author, Library, Librarian classes) ...

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()
    
    class Meta:
        # EXISTING DJANGO-MAPPED PERMISSIONS (Keep these)
        # Note: Django automatically creates 'add_book', 'change_book', 'delete_book'
        # based on the model name. Your existing definitions override them, which is fine.
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
            
            # --- NEW CUSTOM PERMISSIONS ---
            ("can_view", "Can view book details"),
            ("can_create", "Can create a new book"),
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete existing books"),
        ]

    def __str__(self):
        return self.title

# ... (rest of your models) ...

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
