INSERT INTO libraryapp_library
    (title, address)
VALUES
    ('Bellview Library', '500 Main Street');

INSERT INTO libraryapp_book
    (title, isbn, year_published, location_id, author, librarian_id)
VALUES
    ('Lamb', '59359409490', 2004, 1, 'Christopher Moore', 1);

INSERT INTO libraryapp_book
    (title, isbn, year_published, location_id, author, librarian_id)
VALUES
    ('Taiko', '04275747474873', 2001, 1, 'Eiji Yoshikawa', 1);

INSERT INTO libraryapp_book
    (title, isbn, year_published, location_id, author, librarian_id)
VALUES
    ('The Golem and the Jinni', '8592475822', 2013, 1, 'Helene Wecker', 2);

SELECT
    l.id,
    l.user_id,
    l.location_id,
    a.first_name,
    a.last_name
FROM libraryapp_librarian l
    join auth_user a on user_id = a.id
WHERE l.id = 2