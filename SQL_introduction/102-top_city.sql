-- temp
SELECT city, AVG(value) as avg_temp from temperatures where month in (7, 8) group by city ORDER BY avg_temp DESC LIMIT 3;

