CREATE OR REPLACE FUNCTION add_new_film(
    title VARCHAR,
    description TEXT,
    release_year INT,
    language_id INT,
    rental_duration INT,
    rental_rate NUMERIC,
    length INT,
    replacement_cost NUMERIC,
    rating VARCHAR,
    special_features TEXT[]
) RETURNS VOID AS
$$
    BEGIN
INSERT INTO film (title,
                  description,
                  release_year,
                  language_id,
                  rental_duration,
                  rental_rate,
                  length,
                  replacement_cost,
                  rating,
                  special_features)
VALUES (title,
        description,
        release_year,
        language_id,
        rental_duration,
        rental_rate,
        length,
        replacement_cost,
        rating::mpaa_rating,
        special_features);
END;
$$ LANGUAGE plpgsql;
