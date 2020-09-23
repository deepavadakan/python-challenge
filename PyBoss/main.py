import csv
import os
from datetime import datetime

#dict to find the state abbreviation
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

#csv file from which to read data
hr_data_path = os.path.join("employee_data.csv")

#open employee_data.csv to read
with open(hr_data_path) as hrfileStream: 

    hr_datareader = csv.reader(hrfileStream) 
    
    #find the header row
    hr_data_header = next(hr_datareader) 

    #create lists for each column
    emp_ID = []
    first_name = []
    last_name = []
    dob = []
    ssn = []
    state = []
    
    #for each row in the file
    for row in hr_datareader:

        #add emp_IDs to list
        emp_ID.append(row[0])

        #find and split the name into first and last name lists
        emp_name = row[1].split()
        first_name.append(emp_name[0])
        last_name.append(emp_name[1])

        #format date to mm/dd/yyyy and add to list
        date_time_object = datetime.strptime(row[2], '%Y-%m-%d')
        dob.append(date_time_object.strftime("%m/%d/%Y"))

        #add modified ssn to list
        new_ssn = "****-**-" + row[3][-4:] #append last 4 digits to masked ssn
        ssn.append(new_ssn)

        #find the abbreviated State and add to list
        state.append(us_state_abbrev[row[4]])

#csv file to write the formatted data
newhr_data_path = os.path.join("newemployee_data.csv")

with open(newhr_data_path, "w") as newhrfileStream:

    newhr_datareader = csv.writer(newhrfileStream) 

    #add new header row   
    newhr_dataheader = [hr_data_header[0], "First Name", "Last Name", hr_data_header[2], hr_data_header[3], hr_data_header[4]]
    newhr_datareader.writerow(newhr_dataheader)

    #zip all the lists and add them to the csv file
    hr_data = zip(emp_ID, first_name, last_name, dob, ssn, state)
    newhr_datareader.writerows(hr_data)
