-- lists all records of the table second_table
SELECT score, name
WHERE name != ''
FROM second_table
ORDER BY score DESC;