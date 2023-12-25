import requests
import json
from bs4 import BeautifulSoup

# Replace with the website URL
url = "https://www.nseindia.com"
xhr_url = "https://www.nseindia.com/reports/fii-dii"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(url, headers=headers)


# Identify the XHR request URL and data format
# ...

# Send the XHR request
xhr_response = requests.get(xhr_url)

# Parse the data depending on the format (e.g., JSON)
data = json.loads(xhr_response.text)

# Extract the desired data from the parsed JSON
# ...

