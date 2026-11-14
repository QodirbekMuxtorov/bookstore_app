from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books-cbv/', views.BookListView.as_view(), name='book_list_cbv'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bookstore/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]