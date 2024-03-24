-- Just Tragedy...
SELECT DISTINCT title
FROM tv_shows s
LEFT JOIN tv_show_genres sg
ON sg.show_id = s.id
LEFT JOIN tv_genres g
ON g.id = sg.genre_id
WHERE s.title NOT IN (
	SELECT title
	FROM tv_shows s
	INNER JOIN tv_show_genres sg
	ON sg.show_id = s.id
	INNER JOIN tv_genres g
	ON g.id = sg.genre_id
	WHERE g.name = 'Comedy'
)
ORDER BY title;
