import requests
from bs4 import BeautifulSoup

# Specify the URL you want to scrape
url = 'https://www.nseindia.com/reports/fii-dii'
# url  = 'https://www.nseindia.com/all-reports'
# # url  = 'https://www.nseindia.com/market-data/price-bands-surveillance-actions'
# url  = 'https://www.nseindia.com//all-reports/historical-equities-fii-fpi-dii-trading-activity'
#print(stock_url)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.status_code)



if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data=soup.body.prettify()

    print(data)
  
    # with open('soupjj.tex', 'w') as f:
    #     f.write(soup.body.prettify())

    # print(soup.prettify())
    # Identify the all the div 
    # divs = soup.find_all('div', {'class': 'fii-dii-table-container'})
    # tables = soup.find_all('table')
    # h1_tags = soup.find_all('h1')
    # links = soup.find_all('a')
    # print(divs)

    # #  write all the links to a html file
    # with open('div.html', 'w') as f:
    #     for link in divs:
    #         f.write(str(link))
    #         f.write('\n')



#     # Identify the table by ID ('fiidiiTable')
#     table = soup.find('table', id='fiidiiTable')

#     if table:
#         # Extract data from the table
#         rows = table.find_all('tr')

#         for row in rows:
#             # Extract data from each row
#             columns = row.find_all(['td', 'th'])

#             # Print the data (customize as needed)
#             for column in columns:
#                 print(column.text.strip(), end='\t')
#             print()  # Move to the next line after each row

#     else:
#         print("Table with ID 'fiidiiTable' not found on the page.")

# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")


"""
/option-chain
/market-data/new-stock-exchange-listings-today
/market-data/all-upcoming-issues-ipo
/resources/exchange-communication-circulars
/all-reports
/resources/exchange-communication-holidays
/resources/exchange-communication-press-releases
/contact/contact-us
/
/market-data/live-equity-market?symbol=NIFTY%2050
/currency-getquote?symbol=USDINR#inr-contracts
#
/
javascript:;
/national-stock-exchange/about-nse-company
/structure-key-personnel/corporate-structure
/investor-relations/announcements
/national-stock-exchange/awards-recognition
/regulation
/event-gallery
/resources/exchange-communication-media-center
/resources/exchange-communication-holidays
/careers-at-nse
/contact/contact-us
/nse-academy/nse-academy-overview
/nse-clearing
/nse-data-and-analytics
/nse-foundation/about-us
/nse-indices
/nse-international-exchange/about
/nseint_clearing/nse-international-clearing-overview
/nse-investments
/nseit
/national-stock-exchange/our-group
/products-services/about-equity-market
/products-services/about-indices
/products-services/emerge-platform-about-sme
/products-services/mf-about-mfss
/products-services/about-equity-derivatives
/products-services/about-currency-derivatives
/products-services/about-commodity-derivatives
/products-services/about-interest-rate-derivatives
/products-services/fixed-income-debt-overview
/products-services/about-initial-public-offerings
https://www.nseindia.com/national-stock-exchange/about-nse-company
https://www.nseindia.com/national-stock-exchange/our-group
https://www.nseindia.com/products-services
javascript:;
/market-data/pre-open-market-cm-and-emerge-market
/market-data/live-equity-market
/market-data/equity-derivatives-watch
/market-data/live-market-indices
/market-data/bonds-traded-in-capital-market
/market-data/stocks-in-call-auction
/market-data/securities-lending-and-borrowing
/market-data/securities-available-for-trading
/market-data/securities-information-contracts-available-for-trading
/market-data/price-bands-surveillance-actions
/all-reports/historical-equities-fii-fpi-dii-trading-activity
/market-data/legend-of-series
/market-data/liquidity-enhancement-scheme
/market-data/new-stock-exchange-listings-today
/market-data/all-upcoming-issues-ipo
/all-reports
/market-data/real-time-data-subscription
/market-data/analytical-products
/market-data/non-display-data
/market-data/eod-historical-data-subscription
/market-data/corporate-data-subscription
/market-data/data-subscription-fees
/market-data/nse-data-policy
https://www.nseindia.com/market-data/analysis-and-tools-capital-market-snapshot
https://www.nseindia.com/option-chain
https://www.nseindia.com/resources/historical-reports-capital-market-daily-monthly-archives
javascript:;
/invest/first-time-investor-getting-started
/invest/first-time-investor-products
/invest/first-time-investor-stamp-duty-charges-taxes
/invest/first-time-investor-foreign-investment-limits
/invest/investor-charter
/invest/be-a-smart-investor
/invest/investors-awareness-programs
/invest/investors-regulatory-actions
/invest/investors-registered-investors
/invest/find-a-stock-broker
/invest/company-listing-directory-resources-for-investors
/invest/exit-option-for-share-holders
/invest/investors-feedback-form
https://www.nseindia.com/invest/investors-home
https://www.nseindia.com/invest/first-time-investor-products
https://investorhelpline.nseindia.com/NICEPLUS/
javascript:;
/companies-listing/raising-capital-onboarding-process
/companies-listing/raising-capital-public-issues-eligibility-equity-debt
/companies-listing/raising-capital-public-issues-listing-on-emerge
/companies-listing/raising-capital-debt-private-placement
/sse
/companies-listing/raising-capital-mutual-funds-etfs-process
/companies-listing/raising-capital-further-issues-main-sme-checklist
/companies-listing/public-issue-advertisements
/companies-listing/corporate-filings-announcements
/companies-listing/corporate-filings-board-meetings
/companies-listing/corporate-filings-actions
/companies-listing/corporate-filings-financial-results
/companies-listing/corporate-filings-shareholding-pattern
/companies-listing/corporate-filings-offer-documents
/companies-listing/corporate-filings-scheme-document
/companies-listing/sebi-regulations
/companies-listing/compliance-information-compliance-calendar-main-board
/companies-listing/xbrl-information
http://ec2-3-221-41-38.compute-1.amazonaws.com
/companies-listing/corporate-filings-directory
/companies-listing/circular-for-listed-companies-equity-market
https://www.nseindia.com/companies-listing/corporate-filings-application
https://www.nseindia.com/regulations/listing-compliance
https://neaps.nseindia.com/NEWLISTINGCORP/
javascript:;
/trade/admission-process-documents-to-become-a-member
/trade/membership-types
/trade/deposits-networth-requirements-for-membership
/trade/membership-using-enit
/trade/members-change-in-name
/trade/members-compliance
/trade/membership-suspension-expulsion
/trade/membership-formats
/trade/platform-services-neat-trading-system
/trade/platform-services-non-neat-front-end
/trade/platform-services-test-market-facility
/trade/platform-services-connectivity
https://www.nseindia.com/trade/members-homepage
https://ims.connect2nsccl.com/MemberPortal/
https://www.nseindia.com/resources/exchange-communication-circulars
javascript:;
/regulations/exchange-market-regulations-rules-byelaws-nseil
/regulations/exchange-market-surveillance-actions
/regulations/exchange-disclosures-nsccl-iosco-core-sgf-default-waterfall
/regulations/exchange-defaulting-clients
/regulations/unsolicited-messages-report
/submit-tipoff
/trade/members-compliance
/invest/complaint-arbitration-status
/regulations/exchange-market-surveillance-regulatory-actions
/regulations/member-sebi-debarred-entities
/regulations/member-circulars-for-members
/regulations/public-notice
/regulations/listing-compliance
/regulations/clarification-verification-to-market-rumour
/regulations/list-of-companies-proposed-to-be-delisted
/regulations/queries-raised-to-listed-companies
/regulations/list-complaint-status-against-companies-report
/regulations/public-notice-compulsory-delisting
javascript:;
/learn/overview-about-nse-academy
/learn/process-to-register-ncfm-nse-certification-in-financial-markets
/learn/self-study-ncfm-modules-all
/learn/ncfm-prepare-for-a-test
/learn/visit-nse-program
/learn/interactive-courses
/learn/recorded-courses
/learn/class-room-courses
/learn/post-graduate-program-full-time
/learn/nse-international-certificate-program
/learn/courses-for-under-graduates
/learn/courses-for-dealers
/learn/courses-for-working-professionals
/learn/self-study-ncfm-modules-all
/learn/academic-calendar
https://www.nseindia.com/learn/find-a-course
https://www.nseindia.com/learn/nse-knowledge-hub
https://www.ncfm-india.com/ORE/OREloginPage.jsp
javascript:;
/resources/exchange-communication-circulars
/resources/exchange-communication-press-releases
/resources/exchange-communication-holidays
/resources/exchange-communication-contingency-drill-calendar
/resources/exchange-communication-media-queries
/all-reports
/resources/historical-reports-capital-market-daily-monthly-archives
/resources/forms-formats-members
/national-stock-exchange/nse-volume-business-growth
/report-detail/eq_security
/report-detail/fo_eq_security
/historical-spot-price
/reports-indices-historical-index-data
/reports-indices-historical-vix
https://www.nseindia.com/resources/exchange-communication-circulars
https://www.nseindia.com/all-reports
javascript:;
/complaints/complaint-at-exchange
/complaints/process-of-making-a-complaint
/complaints/grievance-redressal-committee
/complaints/arbitration-panel
/complaints/defaulters-committee
/complaints/file-a-complaint-online
/complaints/about-arbitration
/complaints/about-defaulter-section
/complaints/details-to-be-provided-for-lodging-claims
/complaints/submit-tipoff
/complaints/defaulter-expelled-members
/complaints/arbitration-hearing
/complaints/arbitration-awards
/complaints/investor-protection-fund-trust
/complaints/complaints-public-notice
https://smartodr.in/login
https://www.nseindia.com/complaints/arbitration-status
https://www.nseindia.com/contact/contact-us
javascript:;
/research/publications-reports-nse-market-pulse
/research/publications-reports-nse-market-insights
/research/publications-reports-corporate-governance-reports
/research/publications-reports-nse-market-insights
/research/publications-reports-nse-market-insights
/research/research-initiatives
/research/research-initiatives
/research/working-papers
/research/past-initiatives
/research/opportunities
/research/events-upcoming-programs
/research/events-seminars-panel-dicussions
/research/events-conferences
/research/events-lecture-series
/research/conversations
https://www.nseindia.com/research/publications-reports-nse-market-pulse
https://www.nseindia.com/research/research-initiatives
https://www.nseindia.com/research/events-seminars-panel-dicussions
/market-data/live-equity-market?symbol=NIFTY%2050
/currency-getquote?symbol=USDINR#inr-contracts
#
javascript:increaseFont()
javascript:resetFont()
javascript:decreaseFont()
javascript:highContrast()
javascript:normalContrast()
 https://www.nsenmf.com/
https://www.ncfm-india.com/ORE/OREloginPage.jsp
javascript:;
/feedback/new
javascript:;
/
javascript:;
/national-stock-exchange/about-nse-company
/structure-key-personnel/corporate-structure
/investor-relations/announcements
/national-stock-exchange/awards-recognition
/regulation
/event-gallery
/resources/exchange-communication-media-center
/resources/exchange-communication-holidays
/careers-at-nse
/contact/contact-us
/nse-academy/nse-academy-overview
/nse-clearing
/nse-data-and-analytics
/nse-foundation/about-us
/nse-indices
/nse-international-exchange/about
/nseint_clearing/nse-international-clearing-overview
/nse-investments
/nseit
/national-stock-exchange/our-group
/products-services/about-equity-market
/products-services/about-indices
/products-services/emerge-platform-about-sme
/products-services/mf-about-mfss
/products-services/about-equity-derivatives
/products-services/about-currency-derivatives
/products-services/about-commodity-derivatives
/products-services/about-interest-rate-derivatives
/products-services/fixed-income-debt-overview
/products-services/about-initial-public-offerings
/nse-disclaimer
/nse-terms-of-use
/nse-copyright
/sitemap
/website-policies
https://itunes.apple.com/us/app/nse-nmf-ii/id1227619380?mt=8
https://play.google.com/store/apps/details?id=coms.nsenmf.nsenmf&hl=en
https://play.google.com/store/apps/details?id=com.xlx.eipodc
https://www.facebook.com/NationalStockExchange/
https://twitter.com/NSEIndia?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor
https://in.linkedin.com/company/national-stock-exchange-of-india-limited
https://www.youtube.com/user/NSEIL1india
https://www.instagram.com/nseindia
https://www.threads.net/@nseindia
https://www.nseindia.com/rss-feed
/nse-copyright
javascript:;
javascript:;
javascript:;
javascript:;
#qinvest_equity_mr
#qinvest_deriv_mr
#qinvest_debt_mr
javascript:;
/all-reports
javascript:;
/all-reports-derivatives
javascript:;
/all-reports-debt
/market-data/analysis-and-tools-capital-market-snapshot
#qlink_corporate_01
javascript:;
#circulars_equity
#circulars_debt
/companies-listing/circular-for-listed-companies-equity-market
/companies-listing/circular-for-listed-companies-debt-market
/companies-listing/corporate-filings-application
#q_members_circulars
#q_members_trading
#q_members_clearing
#q_members_listing
#q_members_compliance
#q_members_others
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
javascript:;
/resources/exchange-communication-circulars
http://feeds.feedburner.com/nseindia/circulars
tel:1800 266 0050
tel:022 68645400
tel:022 50998100
tel:1800 266 0050
tel:022 68645400
tel:022 50998100

"""
