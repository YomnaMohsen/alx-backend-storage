-- a SQL script that ranks country origins of bands, 
-- ordered by the number of (non-unique) fans

SELECT origin, sum(fans) as nb_fans
from metal_bands
Group by origin
Order by nb_fans DESC;
