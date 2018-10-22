from django.shortcuts import render

from bookmanager.models import Book
from django.http import HttpResponse
from django.views.generic.list import ListView

#2 views one for single and other for list which doesnt work too well

def book(request,title):
    book = Book.objects.get(title=title)
    
    return HttpResponse('%s by %s %s'%(Book.title,Book.author_name,member.author_surname))
    
    #I Couldnt get this response to work with the template so I just commented it out and used the hhtpResponse
    #response = render(request,'CS424-project/booklist/bookmanager/Templates/bookdetail.html',{})
    #return response


def book_list(request):
    
    
    #My template didnt work right and this didn't work exactly as I wanted and it didn't list by the titles but as the object reference 
    #books = Book.objects.values().order_by('title')
    books= Book.objects.only('title')
   
 

    return HttpResponse(books)
    