from django.shortcuts import render, redirect
from .models import Book


def book_registr(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        date = request.POST['date']

        book = Book(title=title, author=author, date=date)
        book.save()

    return render(request, 'app/book_registr.html')