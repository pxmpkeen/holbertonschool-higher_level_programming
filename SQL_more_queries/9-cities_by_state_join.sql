-- join
SELECT cities.id AS id, cities.name AS state_id, states.name AS name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id;
