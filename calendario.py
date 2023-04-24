from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
# Set the options for the Firefox driver
options = webdriver.FirefoxOptions()
options.add_argument('-headless')  # Run Firefox in headless mode (i.e., without a GUI)


# Create a new Firefox driver instance
service = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service)

# Define the URL of the economic calendar
url = 'https://sslecal2.investing.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&importance=2,3&features=datepicker,timezone&countries=72,17,4,5&calType=day&timeZone=40&lang=1%22%20width=%22650%22%20height=%22467%22%20frameborder=%220%22%20allowtransparency=%22true%22%20marginwidth=%220%22%20marginheight=%220%22'
# Load the economic calendar page in Firefox
driver.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table element containing the economic calendar data based on its class name
table = soup.find('table', {'class': 'genTable closedTable ecoCalTable'})

# Get all the rows in the table
rows = table.find_all('tr')

# Get the headers
headers = [header.text.strip() for header in rows[0].find_all("th")]

# Get the data
data = []
for row in rows[1:]:
    values = [value.text.strip() for value in row.find_all("td")]
    d = dict(zip(headers, values))
    if d["Time"] != "":
        d.pop("Imp.", None)
        data.append(d)

print(data)
driver.quit()
