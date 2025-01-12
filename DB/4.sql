SELECT
    e.first_name,
    e.last_name,
    s.store_id,
    DATE_PART('year', r.rental_date) AS year,
    COUNT(r.rental_id) AS rental_count
FROM
    rental r
JOIN
    staff e ON r.staff_id = e.staff_id
JOIN
    store s ON e.store_id = s.store_id
GROUP BY
    e.first_name,
    e.last_name,
    s.store_id,
    DATE_PART('year', r.rental_date)
ORDER BY
    e.last_name,
    e.first_name,
    s.store_id,
    year;