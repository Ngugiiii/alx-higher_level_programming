--  lists the number of records with the same score in the table
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
