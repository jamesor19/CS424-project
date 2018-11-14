from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



#I tried to cover a few urls. The list ones arn't working too well but it's just to show the idea

urlpatterns = [
    path('book/title/<str:book_title>', views.book, name = 'book_detail'),
    path('books', views.book_list),
    path('book/update/title/<str:book_title>', views.book_update, name="book_update"),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
