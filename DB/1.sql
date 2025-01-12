SELECT
    c.first_name,
    c.last_name,
    a.address,
    a.district,
    ci.city,
    co.country,
    a.postal_code
FROM
    customer c
        JOIN
    rental r ON c.customer_id = r.customer_id
        JOIN
    address a ON c.address_id = a.address_id
        JOIN
    city ci ON a.city_id = ci.city_id
        JOIN
    country co ON ci.country_id = co.country_id
WHERE
    date_part('year', r.rental_date) = date_part('year', NOW()) - 1;
