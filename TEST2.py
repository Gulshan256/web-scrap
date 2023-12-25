from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.nseindia.com/reports/fii-dii'
# Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--chromedriver-executable=" + r"C:\Users\kumar\Downloads\chromedriver_win32/chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Open the webpage
    driver.get(url)

    # Wait for the page to load (you may need to adjust the time accordingly)
    driver.implicitly_wait(10)

    # Get the page source after JavaScript has modified the content
    page_source = driver.page_source

    # Use BeautifulSoup to parse the dynamically loaded content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the table using the BeautifulSoup as usual
    table = soup.find('table', id='fiidiiTable')

    if table:
        # Print the HTML content of the table
        print(table.prettify())
        with open("tabledata.html", 'w') as f:
            f.write(table)
    else:
        print("Table with ID 'fiidiiTable' not found on the page.")

except Exception as e:
    print(e)
