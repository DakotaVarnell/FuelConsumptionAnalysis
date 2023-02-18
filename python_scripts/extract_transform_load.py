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

# #open the csv file and read it 
with open('data_files\Fuel_Consumption_2000-2022.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #iterate through each row and read them into a python list
    for row in csv_reader:
        row_information.append(row)

    #iterate through our list and transform the values
    for i in range(len(row_information)):

        #convert our hwy efficiency from l/100 km to mpg
        row_information[i][9] = round((235.215/float(row_information[i][9])), 1)

        #remove our comb efficiency for l/100 km because we already have the mpg equivalent
        del row_information[i][10]

        #add a new column called drive-type which will grab the drive type from the model and remove it from model and add it to drive type column

        #add a new column called flex_fuel which will contain a boolean showing whether the vehicle is flex fuel, does similar to drive-type


# #open the file we will be writing to
# file = open('data_files\Fuel_Consumption_2000-2022.csv', 'a', encoding='utf-8')

# #rewrite our csv converting the liters/km to miles/gallon
# for i in range(len(row_information)):

#     file.write(insert_stmt)
