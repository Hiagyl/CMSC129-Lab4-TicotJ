# tests/test_unit.py
import pytest
from logic import validate_book


def test_validate_book_with_valid_data():
    # This should return True, but the stub returns None
    book = {"title": "The Pristine Code", "author": "Alice Smith"}
    assert validate_book(book) is True
g

def test_validate_book_with_empty_title():
    # This should return False, but the stub returns None
    book = {"title": "", "author": "Alice Smith"}
    assert validate_book(book) is False


def test_validate_book_missing_author():
    # This should return False, but the stub returns None
    book = {"title": "The Pristine Code"}
    assert validate_book(book) is False
