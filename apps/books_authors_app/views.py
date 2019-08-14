from django.shortcuts import render, HttpResponse, redirect

from .models import *

def books(request):
    context = {"books": Books.objects.all()}		
    return render(request, "books_authors_app/books.html", context)

def create_book(request):
    Books.objects.create(title = request.POST['title'], description = request.POST['description'])
    return redirect(request, '/')

def book_details(request, book_id):
    selected_book = Books.objects.get(id = int(book_id))
    context = { 
        'id' : selected_book.id,
        'title' : selected_book.title,
        'description' : selected_book.desc,
        'book_authors' : selected_book.authors.all().order_by("last_name"),
        'all_authors' : Authors.objects.all().order_by("last_name")
    }      
    return render(request, "books_authors_app/books_details.html", context)

def authors(request):
    context = {"authors": Authors.objects.all()}
    return render(request, "books_authors_app/authors.html", context)

def author_details(request, author_id):
    selected_author = Authors.objects.get(id = int(author_id))
    context = { 
        'id' : selected_author.id,
        'first_name' : selected_author.first_name,
        'last_name' : selected_author.last_name,
        'notes' : selected_author.notes,
        'author_books' : selected_author.books.all().order_by("title"),
        'all_books' : Books.objects.all().order_by("title")
    }      
    return render(request, "books_authors_app/authors_details.html", context)