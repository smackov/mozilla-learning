from django.shortcuts import render
from django.views import generic

from .models import Book, BookInstance, Genre, Author, Language

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_books_with_word_star = Book.objects.filter(title__icontains='star').count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_books_with_word_star': num_books_with_word_star,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

    
class BookListView(generic.ListView):
    model = Book
    context_objects_name = 'my_book_list'
    queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'books/my_arbitrary_template_name_list.html'

