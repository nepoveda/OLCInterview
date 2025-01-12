SELECT
    rental_data.rental_id,
    rental_data.title,
    rental_data.rental_date,
    rental_data.return_date,
    rental_data.rental_rate,
    rental_data.days_late,
    ROUND(CAST(0.01 * rental_data.days_late * rental_data.rental_rate AS numeric), 3) AS penalty
FROM (
    SELECT
        r.rental_id,
        f.title,
        r.rental_date,
        r.return_date,
        f.rental_rate,
        DATE_PART('day', AGE(r.return_date, r.rental_date)) - 4 AS days_late
    FROM
        rental r
    JOIN
        inventory i ON r.inventory_id = i.inventory_id
    JOIN
        film f ON i.film_id = f.film_id
    WHERE
        r.return_date IS NOT NULL
) AS rental_data WHERE rental_data.days_late > 0;