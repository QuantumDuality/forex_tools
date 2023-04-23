from selenium import webdriver
from bs4 import BeautifulSoup
from textblob import TextBlob
url = "https://www.reuters.com/search/news?blob=fed"

# create a new firefox browser instance
browser = webdriver.Firefox()
browser.get(url)

# wait for the page to load
browser.implicitly_wait(10)

# get the page source after the page has loaded
html = browser.page_source

# use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# find all elements with class "search-result-indiv"
results = soup.find_all("h3", {"class": "search-result-title"})
print(results)
# create an empty list to store the scraped data
data = []

# iterate over the search results and follow each link
for result in results:
    # get the link element
    link = result.find("a", href=True)

    # follow the link using the Selenium webdriver
    browser.get("https://www.reuters.com" + link["href"])

    # wait for the page to load
    browser.implicitly_wait(10)

    # get the page source after the page has loaded
    html = browser.page_source

    # use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # scrape the desired data from the page and append to the data list
    # for example, to extract the title and summary of the article:
    title = soup.find("h1").get_text()
    article = soup.find("div", {"class": "article-body__container__3ypuX"})
    paragraphs = article.find_all("p")
    text = ""
    for paragraph in paragraphs:
        text += paragraph.get_text()
    #summary = soup.find("p", {"data-testid": "paragraph-2"}).get_text()

# iterate over the scraped data

    data.append((title, text))
    for item in data:
    # create a TextBlob object from the article content
       blob = TextBlob(item[1])
       
    # get the sentiment polarity (-1 to 1)
       sentiment = blob.sentiment.polarity
       
    # print the sentiment polarity and the article content
       print("Title: ", item[0])
       print("Sentiment polarity:", sentiment)
       print("\n")
# close the browser
browser.quit()

# print the scraped data
