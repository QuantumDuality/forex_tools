from selenium import webdriver
from bs4 import BeautifulSoup

# set up the webdriver
driver = webdriver.Firefox()
driver.get('https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&importance=2,3&features=datepicker,timezone&countries=72,17,4,5&calType=dayk&timeZone=40&lang=1')

# wait for the page to load
driver.implicitly_wait(10)

# get the page source and parse it with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# get the row with the date
date_row = soup.find('td', {'class': 'theDay'})

# extract the date from the row
date = date_row.text.strip()

# print the date
print('date:', date)

table = soup.find('table', {'class': 'genTable closedTable ecoCalTable'})
rows = table.find_all("tr")

speeches = []
economic_data = []

for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        time = cells[0].get_text(strip=True)
        currency = cells[1].get_text(strip=True)
        event = cells[3].get_text(strip=True)
        actual = cells[4].get_text(strip=True)
        forecast = cells[5].get_text(strip=True)
        previous = cells[6].get_text(strip=True)
        #importance = cells[].find('div')['title']
        if previous == '':
            speeches.append({'Time': time, 'Cur.': currency, 'Event': event})
        else:
            economic_data.append({'Time': time, 'Cur.': currency, 'Event': event, 'Actual': actual, 'Forecast': forecast, 'Previous': previous})


# close the webdriver
print("Speeches: ")
print(speeches)
print("Economic data: ")
print(economic_data)
driver.quit()


