import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from libraryapp.models import Book
from ..connection import Connection
from libraryapp.models import model_factory


@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            # row_factory has a default function, but we defined a custom model_factory function
            conn.row_factory = model_factory(Book)

            db_cursor = conn.cursor()
            # querying all books from db using sqlite3
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)
            # assigns list of instances of books to all_books
            all_books = db_cursor.fetchall()
        # template we want to load to display the info we queried
        template = 'books/list.html'
        # dict we are passing to our template to iterate (has to be dict)
        context = {
            'all_books': all_books
        }
        # returns httprequest, the template, and the info we queried(context)
        return render(request, template, context)
    # gets called when user wants to add a book
    elif request.method == 'POST':
        # form_data gets assigned the dictionary of all the inputs from the user
        form_data = request.POST
        # inserts and adds book to the db
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
                              (form_data['title'], form_data['author'],
                               form_data['isbn'], form_data['year_published'],
                               request.user.librarian.id, form_data["location"]))
        # redirects after post to /books where you can see your new book
        return redirect(reverse('libraryapp:books'))
