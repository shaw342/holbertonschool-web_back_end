-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT (IFNULL(split,2020)) - (IFNULL(formed,0)) lifespan
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC