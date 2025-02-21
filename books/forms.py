from django import forms 
from .models import Books
class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["book_title","book_description","book_author","book_page","book_publications","book_image"]
        