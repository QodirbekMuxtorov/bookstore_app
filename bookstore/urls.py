from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books-cbv/', views.BookListView.as_view(), name='book_list_cbv'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_create, name='order_create'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bookstore/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('books/<int:id>/edit/', views.book_update, name='book_update'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
]