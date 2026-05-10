def validate_book(book_data: dict) -> bool:
    """
    Improved validation logic using type hints and consolidated checks.
    """
    title = book_data.get("title", "").strip()
    author = book_data.get("author", "").strip()

    # A book is valid only if both title and author are non-empty strings
    return bool(title and author)
