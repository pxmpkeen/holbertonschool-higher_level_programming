--  their rating.
SELECT name, SUM(rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON sg.genre_id = g.id
INNER JOIN tv_show_ratings sr
ON sr.show_id = sg.show_id
GROUP BY name
ORDER BY rating DESC;
