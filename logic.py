def validate_book(book_data):
    """
    Minimum implementation to pass the unit tests.
    """
    title = book_data.get("title")
    author = book_data.get("author")

    # Pass if title and author exist, and title is not just whitespace
    if title and author and title.strip():
        return True

    return False
