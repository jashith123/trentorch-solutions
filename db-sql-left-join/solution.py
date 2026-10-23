-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL
--   )
--
--   CREATE TABLE orders (
--       id INTEGER PRIMARY KEY,
--       user_id INTEGER NOT NULL,
--       product TEXT NOT NULL
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return id, name and order_count for every user, including users with no orders.
SELECT users.id, users.name, COUNT(orders.id) AS order_count FROM users LEFT JOIN orders ON orders.user_id = users.id GROUP BY users.id, users.name
