"""Routes for the app."""
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book


def book_detail(request, pk=None):
    """Render the detail page for a single book."""
    context = {
        'book': get_object_or_404(Book, id=pk)
    }

    return render(request, 'book_detail.html', context)


def book_list(request):
    """Render the whole list of books for a given user."""
    context = {
        'books': get_list_or_404(Book)
    }

    return render(request, 'book_list.html', context)
