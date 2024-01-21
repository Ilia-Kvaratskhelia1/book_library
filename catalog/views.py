from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    books_info = Book.objects.all()
    
    return render(request, 'index.html', {'books_info':books_info})

def book_detail(request,title):
    
    book_detail = Book.objects.get(title = title)
    
    return render(request, 'book_detail.html', {'books':book_detail})

def add_book(request):
    if request.method == 'POST':
        new_book = Book(
            author = request.POST.get('author'),
            published_year = request.POST.get('published_year'),
            title = request.POST.get('title'),
        )
        
        new_book.save()
        return redirect('index')
    
    return render(request, 'add_book.html')


def edit_book(request, title):
    book = Book.objects.get(title = title)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')

        book.save()
        return redirect('book_detail', title=book.title)
    
    return render(request, 'edit_book.html', {'book':book})
        
        
def del_book(request, title):
    book = Book.objects.get(title = title)
    
    if request.method == 'POST':
        book.delete()
        
        return redirect('index')
    
    return render(request, 'delete_book.html', {'book':book})