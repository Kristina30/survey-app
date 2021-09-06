import gspread
from google.oauth2.service_account import Credentials

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

    for survey_row in survey_data:
        print(survey_row)

def ask_survey_questions():
    """
    This method gets the questions from the sruvey spread sheet
    """

    survey_data = SHEET.worksheet("survey_data").get_all_values()
    questions_row = survey_data[0]
    for int in range(len(questions_row)):
        print(questions_row[int] + "? ")
        question_answer = input("Answer:\n ")
    

    

#get_survey_data()
ask_survey_questions()