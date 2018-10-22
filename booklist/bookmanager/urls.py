from django.contrib import admin
from django.urls import path
from . import views



#I tried to cover a few urls. The list ones arn't working too well but it's just to show the idea

urlpatterns = [
    path(' ',views.book_list),
    path('admin/', admin.site.urls),
    path('book/title/<str:title>', views.book),
    path('book/', views.book_list),
    path('bookmanager/',views.book_list),
]
