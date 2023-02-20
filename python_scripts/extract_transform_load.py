#import csv library
import csv
#Source from kaggle https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption


#create a list where we will be storing the row information
column_titles = ['YEAR', 'MAKE', 'MODEL', 'VEHICLE CLASS', 'DRIVE-TYPE', 'FLEX-FUEL', 'ENGINE SIZE', 'CYLINDERS', 'TRANSMISSION', 'FUEL', 'FUEL CONSUMPTION', 'HWY (mpg)', 'COMB (L/100 km)', 'COMB (mpg)', 'EMISSIONS']
row_information = []

#Create dictionaries we will use to check our values against and rewrite
fuel_type = {'X':'Regular Gasoline', 'Z':'Premium Gasoline', 'D':'Diesel', 'E':'Ethanol'}
drive_types = {'4X4':'4-Wheel Drive', 'AWD':'All-Wheel Drive', '4WD':'4-Wheel Drive'}
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
        row_information[i][11] = round((235.215/float(row_information[i][9])), 1)

        #remove our comb efficiency for l/100 km because we already have the mpg equivalent
        del row_information[i][12]

        #add a new column called drive-type which will grab the drive type from the model and remove it from model and add it to drive type column

        #iterate over the drive_type keys and check if they are listed in the vehicle model
        for key in drive_types:

            #if the vehicle model lists the drive type(4X4, AWD, 4WD) then remove it from the model name and then create a new column that contains the listed drive_type
            if key in row_information[i][2]:
                row_information[i][2] = str(row_information[i][2]).replace(key, '')
                row_information[i].insert(3, key)

            #if the length of the row is 12 then it didn't contain the drive_type and thus wasn't added, so double check and then add a null value in column 3
            elif len(row_information[i]) == 12 and key not in row_information[i][2]:
                row_information[i].insert(3,'Null')

        #add a new column called flex_fuel which will contain a boolean showing whether the vehicle is flex fuel, does similar to drive-type
        for key in flex_fuel:
            
            if key in row_information[i][2]:
                row_information[i][2] = str(row_information[i][2]).replace(key, '')
                row_information[i].insert(4, key)
                
            elif (len(row_information[i]) == 13 and key not in row_information[i][2]):
                row_information[i].insert(4, 'Null')
            


    #Testing just show the top few hundred
    for i in range(len(row_information)):
        
        if row_information[i][4] != 'Null':
            print(row_information[i])


# #open the file we will be writing to
# file = open('data_files\Fuel_Consumption_2000-2022.csv', 'a', encoding='utf-8')

# #rewrite our csv converting the liters/km to miles/gallon
# for i in range(len(row_information)):

#     file.write(insert_stmt)
