-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL,
--       age INTEGER
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return page 2 of the users (2 rows per page), ordered by id.
SELECT * FROM users ORDER BY id LIMIT 2 OFFSET 2
