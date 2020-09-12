from django.shortcuts import render
from .models import Book, BookInstance, Genre, Author, Language


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_books_with_word_star = Book.objects.filter(title__icontains='star').count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()

    # Generate counts of visit to this view (page)
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_books_with_word_star': num_books_with_word_star,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    # context_objects_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # template_name = 'book212/book2_list.html'


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author


    
