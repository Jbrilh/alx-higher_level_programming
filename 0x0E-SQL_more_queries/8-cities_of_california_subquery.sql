-- List all citites of CA in the database hbtn_0d_usa
-- Results are ordered by ascednging citites.id.
SELECT id, name
FROM cities
WHERE state_id IN
(SELECT id FROM states
	WHERE name = "california")
ORDER BY id;
