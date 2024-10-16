-- a SQL script that lists all bands with Glam rock as their main style, 
-- ranked by their longevity

SELECT origin, sum(fans) as nb_fans
from metal_bands
Group by origin
Order by nb_fans DESC;
