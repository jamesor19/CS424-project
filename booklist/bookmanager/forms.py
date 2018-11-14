from django import forms

from bookmanager.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=[]
        fields = ['title','author_name','author_surname']
