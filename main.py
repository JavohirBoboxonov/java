# -- create table users(
# -- id serial primary key,
# -- full_name varchar(100),
# -- email varchar(100),
# -- password text,
# -- created_at timestamp
# -- );

# -- insert into users(full_name, email, password, created_at)
# -- values
# -- ('Ali Valiyev', 'alivali@gmail.com', '12345', now()),
# -- ('Dilshod Ganiyev', 'dilshod@gmail.com', '14785', now());

# -- ==================================================================

# -- create table autors (
# -- id serial primary key,
# -- full_name varchar(100),
# -- country varchar(100)
# -- );

# -- INSERT INTO autors (full_name, country)
# -- VALUES
# -- ('Ali Valiyev', 'Uzbekistan'),
# -- ('Dilshod Ganiyev', 'Uzbekistan');

# -- ====================================================

# -- create table genres (
# -- id  serial primary key,
# -- name varchar(50  )
# -- );

# -- INSERT INTO genres (name)
# -- VALUES
# -- ('Drama'),
# -- ('Fantastika');

# -- ========================================================

# -- create table books(
# -- id serial primary key,
# -- title varchar(150),
# -- autor_id integer references autors(id),
# -- description text,
# -- publisher_year integer,
# -- genre_id integer references genres(id),
# -- created_at timestamp
# -- );

# -- insert into books(title, description, published_year, author_id, genre_id, created_at)
# -- values
# -- ('Diqqat', 'Yaxshi kitob', 1997, 1, 1, now()),
# -- ('Savol', 'Yaxshi kitob', 1998, 2, 2, now());

# -- =====================================================

# -- create table comments(
# -- id serial primary key,
# -- user_id integer references users(id),
# -- book_id integer references books(id),
# -- content text,
# -- created_at timestamp
# -- );

# -- INSERT INTO comments (user_id, book_id, content, created_at)
# -- VALUES
# -- (1, 1, 'Ajoyib kitob', NOW()),
# -- (2, 2, 'Kitob juda qiziqarli', NOW());

# -- =====================================================

# -- 1) masala
# -- select * from books
# -- order by published_year

# -- 2) masala
# -- select g.name as genre_name, count(b.id) as book_count from genres g
# -- inner join books b on b.genre_id = g.id
# -- group by g.name
# -- order by book_count desc

# -- 3) masala
# -- select b.id, b.title from books b
# -- inner join comments c on c.book_id = b.id
# -- where c.id is null;

# -- 4) masala
# -- SELECT a.full_name, COUNT(b.id) AS book_count FROM authors a
# -- LEFT JOIN books b ON b.author_id = a.id
# -- GROUP BY a.id, a.full_name
# -- ORDER BY book_count DESC
# -- limit 5;
