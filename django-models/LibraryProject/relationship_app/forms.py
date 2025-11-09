# relationship_app/forms.py
from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
        }