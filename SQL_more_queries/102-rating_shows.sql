-- rotten tomatoes.
SELECT title, SUM(rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY title
ORDER BY rating DESC;
