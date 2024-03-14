-- bruh
SELECT s.title, g.genre_id FROM tv_shows AS s INNER JOIN tv_show_genres AS g ON s.id = g.show_id WHERE s.id IN (SELECT show_id FROM tv_show_genres GROUP BY show_id HAVING genre_id >= 1) ORDER BY s.title, g.genre_id 
