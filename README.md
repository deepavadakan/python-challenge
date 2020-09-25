# python-challenge
PyBank (Located in the PyBank folder)

    Resources folder: Contains the budget_data.csv used in the script
    Analysis folder: Contains FinancialAnaysis.txt with the results from the analysis
    main.py: Python script that analyzes the records to calculate each of the following 
        and outputs to the terminal and to the FinancialAnalysis.txt file found in the Analysis folder:

        The total number of months included in the dataset

        The net total amount of "Profit/Losses" over the entire period

        The average of the changes in "Profit/Losses" over the entire period

        The greatest increase in profits (date and amount) over the entire period

        The greatest decrease in losses (date and amount) over the entire period

PyPoll (Located in the PyPoll folder)

    Resources folder: Contains the election_data.csv used in the script
    Analysis folder: Contains Election_Results.txt with the results from the analysis
    main.py: Python script that analyzes the votes and calculates each of the following 
        and outputs to the terminal and to the Election_Results.txt file found in the Analysis folder:

        The total number of votes cast

        A complete list of candidates who received votes

        The percentage of votes each candidate won

        The total number of votes each candidate won

        The winner of the election based on popular vote.

PyBoss (Located in the PyBoss folder)

    Resources folder: Contains the employee_data.csv used in the script
    Results folder: Contains converted_employee_data.csv with the newly formatted data
    main.py: Python script able to convert employee records to the required format 
        and outputs to the converted_employee_data.txt file found in the Results folder.
        The required conversions are as follows:

            The Name column split into separate First Name and Last Name columns.

            The DOB data re-written into MM/DD/YYYY format.

            The SSN data re-written such that the first five numbers are hidden from view.

            The State data re-written as simple two-letter abbreviations.
        
    used dict from afhaque/us_state_abbrev.py for abbreviated states