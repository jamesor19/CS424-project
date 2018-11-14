from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bookmanager.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView

from bookmanager.forms import BookForm
from django.urls import reverse

#2 views one for single and other for list which doesnt work too well

def book(request,book_title):
    book = Book.objects.get(title=book_title)
    
    response = render(request,'bookmanager/book_detail.html',{
        "book":book
    })
    return response
    
   
 

def book_list(request):
    books = Book.objects.all()
    
    response=render(request,'bookmanager/book_list.html',{
        'books':books
    })
    return response
    
    


@login_required
def book_update(request,book_title):
    book = Book.objects.get(title=book_title)
    if request.method=="POST":
        form = BookForm(request.POST, instance=book) # populates the form fields with POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book_detail',kwargs={'book_title':book_title}))
        else:
            return HttpResponseRedirect('/')

    form = BookForm(instance=book)
    return render(request,'bookmanager/book_update.html',{
            'form':form
        })

 