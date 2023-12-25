from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
 
url = 'https://www.nseindia.com/reports/fii-dii' 

# enable headless mode
# Options.add_argument("--headless")
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 

driver.get(url) 
time.sleep(1)
driver.page_source

# get all the lines from the page
# element = driver.find_element(By.ID, "fiidiiTable")
# get table  head element
# element = driver.find_element(By.TAG_NAME, "thead")
# # get table  head element
# element = driver.find_element(By.TAG_NAME, "tbody")
# get all the rows of the table
row=driver.find_elements(By.TAG_NAME, "tr")
# get all the columns of the table
col=driver.find_elements(By.TAG_NAME, "td")

for i in row:
	print(i.text)



# update the sheet sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/....'
import os.path


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()


# for i in col:
# 	print(i.text)



# elements = driver.find_elements(By.TAG_NAME, "tr")

# data_list=[]
# for i in elements:   
# 	tesxt=i.text.split(" ")
# 	tesxt=i.text.split("\n")

# 	for j in range (len(tesxt)):
# 		if tesxt[j+1].startswith("("):
# 			tesxt[j]=tesxt[j]+" \n"+tesxt[j+1]
# 			tesxt.pop(j+1)
# 			j=len(tesxt)-1
		
# 	data_list.append(tesxt)


# print(data_list)

# ['CATEGORY', 'DATE', 'BUY VALUE(₹ Crores)', 'SELL VALUE(₹ Crores)', 'NET VALUE(₹ Crores)']

# [['CATEGORY', 'DATE', 'BUY VALUE', '(₹ Crores)', 'SELL VALUE', '(₹ Crores)', 'NET VALUE', '(₹ Crores)'], ['DII ** 14-Dec-2023 12,118.30 11,565.13 553.17'], ['FII/FPI * 14-Dec-2023 21,080.40 17,510.33 3,570.07']]