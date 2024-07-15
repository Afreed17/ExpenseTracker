Expense Tracker Application

Video Demo
https://youtube.com/watch?v=nDwm_HjKFoc

Description
The Expense Tracker application is a command line tool designed to help users manage their personal expenses efficiently It offers a range of features including adding new expenses viewing existing ones deleting specific expenses generating monthly reports and saving expense data to a CSV file for easy future reference and analysis

Features
Add Expenses Users can input a description amount and date for new expenses
View Expenses Users can see all recorded expenses listed in a tabular format
Delete Expenses Users can remove expenses using their unique ID
Generate Monthly Report Users can generate a report summarizing expenses for each month
Save to CSV The application saves all expenses to a CSV file making it easy to view and analyze the data externally
Files
projectpy Contains the main application code including all functionality for managing expenses
test_projectpy Contains unit tests for the application functions using the pytest framework
requirementstxt Lists required libraries for running the tests
Design Choices
Command Line Interface The application uses a simple command line interface for ease of use and accessibility
Expense Class Each expense is represented as an instance of the Expense class encapsulating relevant details
ExpenseTracker Class The ExpenseTracker class manages the collection of expenses and provides methods for the main operations
CSV Storage All expenses are saved in a CSV file with a structured format allowing for easy data management
How to Run
1 Install the required libraries

sh
Copy code
pip install r requirementstxt
2 Run the main application

sh
Copy code
python projectpy
3 Run tests to ensure functionality

sh
Copy code
pytest
Example Usage
1 Start the application
2 Choose an option from the menu eg add an expense
3 Follow prompts to enter details for your expenses
4 View expenses or generate reports as needed
5 Save your expenses to a CSV file before exiting

Future Enhancements
Implement user authentication to secure personal expense data
Add data visualization for expenses over time
Introduce categories for expenses to facilitate better tracking
Author
Mohamed Afreed K
Kerala India
httpsgithubcomAfreed17

This READMEmd file provides a comprehensive overview of the Expense Tracker application detailing its features files design choices usage instructions and potential future enhancements This documentation ensures users and developers understand the applications functionality and can effectively utilize and contribute to the project