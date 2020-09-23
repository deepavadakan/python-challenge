import csv
import os
from datetime import datetime

#to find the state abbreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#set path to the election_data.csv which is in the resources folder
#csvpath = os.path.join("Resources","election_data.csv")
#csv file from which to read data
hr_data_path = "employee_data.csv"
#csv file to write the formatted data
newhr_data_path ="newemployee_data.csv"

#in both csv files
with open(hr_data_path) as hrfileStream, open(newhr_data_path, "w") as newhrfileStream: 

    #open the files for reading and writing
    hr_datareader = csv.reader(hrfileStream) 
    newhr_datareader = csv.writer(newhrfileStream) 
    
    #find the header row
    hr_data_header = next(hr_datareader) 
    
    #add new header row   
    newhr_dataheader = [hr_data_header[0], "First Name", "Last Name", hr_data_header[2], hr_data_header[3], hr_data_header[4]]
    newhr_datareader.writerow(newhr_dataheader)

    #for each row in the file
    for row in hr_datareader:

        #find and split the name into first and last name
        emp_name = row[1].split()
        first_name = emp_name[0]
        last_name = emp_name[1]

        #format date to mm/dd/yyyy
        date_time_object = datetime.strptime(row[2], '%Y-%m-%d')
        hr_date = date_time_object.strftime("%m/%d/%Y")

        #find the abbreviated State
        hr_state = us_state_abbrev[row[4]]

        #create the row and add to the new csv file
        newhr_row = [row[0], first_name, last_name, hr_date, row[3], hr_state]
        newhr_datareader.writerow(newhr_row)
