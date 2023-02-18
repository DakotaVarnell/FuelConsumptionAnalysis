#import csv library
import csv
#Source from kaggle https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption


#create a list where we will be storing the row information
column_titles = ['YEAR', 'MAKE', 'MODEL', 'VEHICLE CLASS', 'ENGINE SIZE', 'CYLINDERS', 'TRANSMISSION', 'FUEL', 'FUEL CONSUMPTION', 'HWY (mpg)', 'COMB (L/100 km)', 'COMB (mpg)', 'EMISSIONS']
row_information = []

#Create dictionaries we will use to check our values against and rewrite
fuel_type = {'X':'Regular Gasoline', 'Z':'Premium Gasoline', 'D':'Diesel', 'E':'Ethanol'}
drive_types = {'4x4':'4-Wheel Drive', 'AWD':'All-Wheel Drive'}
flex_fuel = {'FFV':'Flex Fuel Vehicle'}
transmission_type = {
'A':'Automatic', 'AM':'Automatic Manual', 'AS':'Automatic with Select Shift', 
'AV':'Continuously Variable', 'M3':'3-Speed Manual', 'M4':'4-Speed Manual', 
'M5':'5-Speed Manual', 'M6':'6-Speed Manual', 'M7':'7-Speed Manual',
'M8':'8-Speed Manual', 'M9':'9-Speed Manual', 'M10':'10-Speed Manual'
}
