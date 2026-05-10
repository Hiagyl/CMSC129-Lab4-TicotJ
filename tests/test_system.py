# tests/test_system.py
import pytest
from playwright.sync_api import expect

# The live_server fixture starts your Flask app automatically


@pytest.mark.usefixtures('live_server')
def test_user_story_1_add_book(page, live_server):
    """
    User Story 1: As a reader, I want to add a new book with a title and author.
    """
    page.goto(live_server.url())

    # Fill out the form
    page.fill("#title", "1984")
    page.fill("#author", "George Orwell")
    page.click("#add-book-btn")

    # Check if the book appears in the list
    expect(page.locator("#book-list")).to_contain_text("1984")


def test_user_story_2_view_list(page, live_server):
    """
    User Story 2: As a librarian, I want to view a list of all saved books.
    """
    page.goto(live_server.url())

    # The list should exist even if empty
    expect(page.locator("#book-list")).to_be_visible()


def test_user_story_3_remove_book(page, live_server):
    """
    User Story 3: As a user, I want to remove a book from the list.
    """
    page.goto(live_server.url())

    # Assuming a book exists, try to click a delete button
    # This will fail because no such button exists yet
    page.click(".delete-btn:first-child")

    expect(page.locator("#book-list")).not_to_contain_text("1984")
