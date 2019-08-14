from django.shortcuts import render, HttpResponse, redirect

from .models import *

def books(request):
    context = {"books": Books.objects.all()}		
    return render(request, "books_authors_app/books.html", context)

def create_book(request):
    Books.objects.create(title = request.POST['title'], desc = request.POST['description'])
    return redirect ('/')

def book_details(request, book_id):
    selected_book = Books.objects.get(id = int(book_id))
    context = { 
        'id' : selected_book.id,
        'title' : selected_book.title,
        'description' : selected_book.desc,
        'book_authors' : selected_book.authors.all().order_by("last_name"),
        'all_authors' : Authors.objects.exclude(books = Books.objects.filter(id = selected_book.id)).order_by("last_name")
    }      
    return render(request, "books_authors_app/books_details.html", context)

def add_author(request):
    author_name = request.POST['selected_author'].split(" ")
    Books.objects.get(id = int(request.POST['book_id'])).authors.add(Authors.objects.get(first_name = author_name[0], last_name = author_name[1]))
    return redirect('/books/' + str(request.POST['book_id']))

def add_book(request):
    Authors.objects.get(id = int(request.POST['author_id'])).books.add(Books.objects.get(title = request.POST['selected_book']))
    return redirect('/authors/' + str(request.POST['author_id']))

def authors(request):
    context = {"authors": Authors.objects.all()}
    return render(request, "books_authors_app/authors.html", context)

def create_author(request):
    Authors.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect ('/authors')

def author_details(request, author_id):
    selected_author = Authors.objects.get(id = int(author_id))
    context = { 
        'id' : selected_author.id,
        'first_name' : selected_author.first_name,
        'last_name' : selected_author.last_name,
        'notes' : selected_author.notes,
        'author_books' : selected_author.books.all().order_by("title"),
        'all_books' : Books.objects.exclude(authors = Authors.objects.filter(id = selected_author.id)).order_by("title")
    }      
    return render(request, "books_authors_app/authors_details.html", context)