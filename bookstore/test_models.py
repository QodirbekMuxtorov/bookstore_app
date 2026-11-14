import pytest
from bookstore.models import Book


@pytest.mark.django_db
def test_book_creation():
    book = Book.objects.create(
        title="O'tkan kunlar",
        author="Abdulla Qodiriy",
        price=45000,
    )
    assert book.title == "O'tkan kunlar"


@pytest.mark.django_db
def test_book_str():
    book = Book.objects.create(
        title="Mehrobdan chayon",
        author="Abdulla Qodiriy",
        price=40000,
    )
    assert str(book) == "Mehrobdan chayon (Abdulla Qodiriy)"