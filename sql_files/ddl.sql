--DDL:Finds the average mpg of various drive types and sorts them from highest to lowest and creates a new table from it
CREATE TABLE average_by_drivetype AS
select drive_type, round(avg(comb_mpg), 2) as average_mpg 
from fuel_consumption
group by drive_type
order by average_mpg desc;

--DDL:Finds the average mpg of various numbers of cylinders and sorts them from highest to lowest and creates a new table from it
CREATE TABLE average_by_num_cylinder AS
select cylinders, round(avg(comb_mpg), 2) as average_mpg 
from fuel_consumption
group by cylinders
order by average_mpg desc;

--DDL:Finds the average mpg of each auto maker and sorts them from highest to lowest and creates a new table from it
CREATE TABLE average_by_make AS
select make, round(avg(comb_mpg), 2) as average_mpg 
from fuel_consumption
group by make
order by average_mpg desc;

--DDL:Finds the average mpg of year and sorts them from earliest year to latest and creates a new table from it
CREATE TABLE average_by_year AS
select year, round(avg(comb_mpg), 2) as average_mpg 
from fuel_consumption
group by year
order by year asc;


--DDL to drop tables
drop table fuel_consumption;
drop table average_by_drivetype;
drop table average_by_num_cylinder;
drop table average_by_make;
drop table average_by_year;