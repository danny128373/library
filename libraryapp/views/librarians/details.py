import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection


def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.user_id,
            a.email,
            a.first_name,
            a.last_name
        FROM libraryapp_librarian l
        JOIN auth_user a on user_id = a.id
        WHERE l.id = ?
        """, (librarian_id,))

        return db_cursor.fetchone()


@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = get_librarian(librarian_id)

        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)
