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
url = 'https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&importance=2,3&features=datepicker,timezone&countries=72,17,4,5&calType=week&timeZone=40&lang=1" width="650" height="467" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"'
# Load the economic calendar page in Firefox
driver.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table element containing the economic calendar data based on its class name
table = soup.find('table', {'class': 'genTable closedTable ecoCalTable'})

# Get all the rows in the table
rows = table.find_all('tr')

# Initialize a list to hold the table data as tuples
table_data = []

# Loop through each row in the table
for row in rows:
    # Get all the columns in the row
    cols = row.find_all('td')
    
    # Check if the row contains data (i.e., is not a header row)
    if cols:
        # Extract the text content of each cell in the row
        row_data = [col.get_text().strip() for col in cols]
        # Convert the row data to a tuple and append it to the table data list
        table_data.append(tuple(row_data))

# Print the table data as a list of tuples
print(table_data)

# Close the Firefox driver instance
driver.quit()
