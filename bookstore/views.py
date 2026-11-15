from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .forms import BookForm, OrderForm
from .models import Book, Order
from .serializers import BookSerializer


@login_required
def book_list(request):
    books = Book.objects.select_related('category').all()
    return render(request, 'bookstore/book_list.html', {'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'bookstore/book_detail.html', {'book': book})


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookstore/book_form.html', {'form': form})


@login_required
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookstore/book_form.html', {'form': form, 'book': book})


@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookstore/book_confirm_delete.html', {'book': book})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'bookstore/register.html', {'form': form})


@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(initial={'book': request.GET.get('book')})
    return render(request, 'bookstore/order_form.html', {'form': form})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).select_related('book')
    return render(request, 'bookstore/order_list.html', {'orders': orders})


class BookListView(ListView):
    model = Book
    template_name = 'bookstore/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.select_related('category')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer