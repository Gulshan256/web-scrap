import requests
from bs4 import BeautifulSoup

# Specify the URL you want to scrape
url = 'https://www.nseindia.com/reports/fii-dii'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(url, headers=headers)

print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'mid_body live_mkt_watch'
    target_div = soup.find('div', class_='mid_body live_mkt_watch')

    if target_div:
        # Print the HTML content of the target div
        # print(target_div.prettify())
        # with open("divdata", 'w') as f:
        #     f.write(target_div.prettify())


        #  <a download="equity-derivatives.csv" href="javascript:;" onclick="downloadCSV()">
            #  <img alt="csv" height="16" src="/assets/images/icon-xls.svg" title="csv" width="16"/>
            #  Download (.csv)
            # </a>
        
        # download CSV file
        csv_link = target_div.find('a', onclick="downloadCSV()")
        print(csv_link)
        csv_url = csv_link.get('href')
        print(csv_url)
        csv_response = requests.get(csv_url)
        print(csv_response.status_code)


    else:
        print("Div with class 'mid_body live_mkt_watch' not found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
