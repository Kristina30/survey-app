import gspread
from google.oauth2.service_account import Credentials
import os
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Survey')


def get_survey_data():
    """
    This method gets data from the Survey spredsheet and display it to the user
    """

    survey_data = SHEET.worksheet("survey_data").get_all_values()
    count = 0

    survey_data_rows = []
    for survey_row in survey_data:
        count = count + 1
        # second row in the spreadsheet is the data type so we need to skip it
        if (count != 2):
            survey_data_rows.append(survey_row)

    print(tabulate(survey_data_rows))


def ask_survey_questions():
    """
    This method gets the questions and data type from the sruvey spread sheet
    """
    survey_answers = []
    survey_data = SHEET.worksheet("survey_data").get_all_values()

    questions_row = survey_data[0]
    data_types = survey_data[1]

    for int in range(len(questions_row)):
        while True:
            print(questions_row[int] + "? (type: " + data_types[int] + ")")
            question_answer = input("Answer: ")
            if validate_data(question_answer, data_types[int]):
                break
        survey_answers.append(question_answer)
    return survey_answers


def validate_data(value, data_type):
    """
    This function validates the entered data based on the question data type
    """
    try:
        result = False
        if (data_type == "text"):
            if (len(value) > 0):
                return True
        if (data_type == "number"):
            if (int(value) > 0):
                return True
        if (len(data_type.split("/")) > 1):
            data_values = data_type.split("/")
            for str in data_values:
                if (str.lower() == value.lower()):
                    return True
    except ValueError as e:
        print(f"Invalid data for type {data_type} - {e}")
        return False
    if (result is False):
        print(f"Invalid data for type {data_type}")

    return result


def save_survey_data(survey_data):
    """
    This function will accept as paramater an array of survey answers.
    It will save the data to the servey spreadsheet
    """
    print("Updating survey worksheet...\n")

    worksheet_to_update = SHEET.worksheet("survey_data")
    worksheet_to_update.append_row(survey_data)
    print("Survey worksheet updated.\n")


def clearConsole():
    """
    This method will be used to clear the console for the user
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def print_main_menu():
    """
    this functions prints the main menu
    """
    print("Please select one of the following options:\n")
    print("1-Complete survey")
    print("2-View all survey results")
    print("3 View survey results per gender")
    print("4 View survey results per age group")
    print("5 Exit\n")
    menu_selection = input("What is your choice?:")
    return menu_selection


def main():
    """
    This is the main function from which all other function will be called.
    Initialy the main function will display the menu to the user
    """
    while True:
        menu_selection = print_main_menu()
        if (menu_selection == "1"):
            clearConsole()
            new_survey_row = ask_survey_questions()
            save_survey_data(new_survey_row)
            clearConsole()
        if (menu_selection == "2"):
            clearConsole()
            get_survey_data()
            sub_menu_selection = input("Enter 1 to return to the main menu:")
            if(sub_menu_selection == "1"):
                clearConsole()
               
        if (menu_selection == "5"):
            print("Thank you!")
            break


print("Welcome to our survey\n")
main()
