/* First exercise */
SELECT title, gross - budget AS net_profit
FROM films;

/* second exercise */
SELECT title, duration / 60.0 as duration_hours
FROM films;

/* Third exercise */
SELECT AVG(duration) / 60.0 as avg_duration_hours
FROM films;