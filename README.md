# Fuel Consumption Analysis for Vehicles Made Between 2000-2022
This is a data engineering project that focuses on the data pipeline from beginning to end. It utilizes a dataset found on Kaggle that contains all the data of vehicles made by various car manufacturers. 

Data Source from Kaggle https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption

Run the data through my etl script written in [Python ETL Script](https://github.com/DakotaVarnell/FuelConsumptionDataPipeline/blob/master/python_scripts/extract_transform_load.py) where I've clean the data significantly, created new columns for important aspects of the data such as drive_type and flex-fuel-vehicle and rewritten the data to a new file

## Now I have a cleaned csv file which I uploaded into an AWS S3 bucket for storage
I named the S3 bucket pipelineprojectbucket and as you can see I've sucessfully uploaded the newly transformed csv file
![s3_bucket_population](https://user-images.githubusercontent.com/89564744/222986387-1ac3a28c-71e4-4e18-bc83-7e67a652b012.PNG)

## Then I connected my S3 bucket 'pipelineprojectbucket' to the newly created Amazon Athena database
I created the database to include the columns shown below as well as their data types
![athena_table_creation](https://user-images.githubusercontent.com/89564744/222986513-70851eab-978a-4116-b53e-4b97536f46a3.PNG)

## I created a few new tables using queries to seperate important information into individual tables
~~~~sql
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

~~~~

# Finally I created a dashboard on Amazon Quicksight to visualize the tables I had just created in Athena

## Average Fuel Economy by Make of Vehicle
As you can see from the chart below, the Smart brand reigns supreme with the highest fuel economy around 50mpg while the lowest performers are luxury performance car brands such as Bugatti and Ferrari. 
![image](https://user-images.githubusercontent.com/89564744/222990354-961a45e2-faa4-48d3-a491-305aaf8bf00d.png)


## Average Fuel Economy by Year 2000-2022
On Average between the years 2000 and 2022 fuel economy has remained within the range of 25-30mpg with an oddly high year in 2014 that goes above 30mpg. 
![image](https://user-images.githubusercontent.com/89564744/222990379-ad3a489c-90f3-4b6f-ab19-c3f62c2e9806.png)


## Average Fuel Economy by Number of Cylinders
As you can see from the chart below, for the most part engines with more cylinders do not get as good fuel economy as those with less. Three-Cylinder engines perform significantly higher than all the others in this example. 
![image](https://user-images.githubusercontent.com/89564744/222990410-e703079a-13e9-4e2a-9209-50167ebba9cb.png)


## Average Emissions by Engine Size(liters)
No surprise here but as the size of engines increase the more emissions are emitted from the vehicle. 
![image](https://user-images.githubusercontent.com/89564744/222990440-e06524bf-f64d-42af-831b-c5ba01d3f441.png)


## Number of Vehicle Models by Make
Between the years 2000 and 2022 the company that produced the most vehicle models was Chevrolet with Ford and BMW following close behind. 
![image](https://user-images.githubusercontent.com/89564744/222990468-8cd67b4d-daa0-4bcc-b97d-1610012ac688.png)


