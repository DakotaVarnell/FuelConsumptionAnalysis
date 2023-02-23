#Process the information on the Fuel_Consumption.csv file-clean it and modify it
#Data Source from kaggle https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption

#import csv library
import csv

#create a list where we will be storing the row information
column_titles = ['YEAR', 'MAKE', 'MODEL', 'VEHICLE CLASS', 'DRIVE-TYPE', 'FLEX-FUEL', 'ENGINE SIZE', 'CYLINDERS', 'TRANSMISSION', 'FUEL', 'FUEL CONSUMPTION', 'HWY (mpg)', 'COMB (mpg)', 'EMISSIONS']
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

#open the csv file and read it 
with open('data_files\Raw_Fuel_Consumption_2000-2022.csv', encoding="utf8") as csv_file:
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

            #if the length of the row is 12 then it didn't contain the drive_type and thus wasn't added, then add a null value in column 3
            elif len(row_information[i]) == 12 and key not in row_information[i][2]:
                row_information[i].insert(3,'Null')

        #add a new column called flex_fuel which will contain FFV if the vehicle has flex fuel, otherwise null, similar to drive_type
        for key in flex_fuel:
            
            #if the vehicle model lists Flex Fuel(FFV) then remove it from model and create a new column that contains FFV if true, null if not
            if key in row_information[i][2]:
                row_information[i][2] = str(row_information[i][2]).replace(key, '')
                row_information[i].insert(4, key)

            #if the length of the row is 13 then it doesn't contain flex fuel and didn't create the new column, add a nul value in column 4
            elif (len(row_information[i]) == 13 and key not in row_information[i][2]):
                row_information[i].insert(4, 'Null')

        #navigate our csv and change the drive type from the code such as M5 to the true value -> Manual 5-Speed
        for key in transmission_type:

            #check to see what key the current row transmisson type corresponds to and then replace it with the value of the key/val pair
            if key in row_information[i][8]:
                row_information[i][8] = str(transmission_type.get(key))

        #navigate our csv and change the fuel type from the code such as X to the true value -> Gasoline       
        for key in fuel_type:

            #check to see what key the current row fuel type corresponds to and then replace it with the value of the key/val pair
            if key in row_information[i][9]:
                row_information[i][9] = str(fuel_type.get(key))

#Rewrite our CSV to reflect these changes
with open('data_files\Final_Fuel_Consumption_2000-2022.csv','w', newline = '', encoding='utf8') as csv_file:

    #Create csv writer
    csv_writer = csv.writer(csv_file, delimiter=',')

    #Iterate through every row of the list and write the row to our new csv file
    for row in range(len(row_information)):
        csv_writer.writerow(row_information[row])
        
