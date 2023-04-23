from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

service = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# create an instance of the sentiment analyzer
sia = SentimentIntensityAnalyzer()

driver.get('https://www.federalreserve.gov/newsevents/speeches.htm')

checkbox1 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[1]/label/input')
checkbox1.click()

checkbox2 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[2]/label/input')
checkbox2.click()

checkbox3 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[3]/label/input')
checkbox3.click()

checkbox4 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[4]/label/input')
checkbox4.click()

checkbox5 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[5]/label/input')
checkbox5.click()

checkbox6 = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/form/div[4]/div[6]/label/input')
checkbox6.click()


submit = driver.find_element("xpath","/html/body/div[3]/div[2]/div/div[1]/form/div[5]/a")
submit.click()

driver.implicitly_wait(10)

# find all link elements with class "itemTitle"
links = driver.find_elements("xpath","//p[@class='itemTitle']/em/a")
# iterate through the list of links and extract the URLs
urls = []
for link in links:
    url = link.get_attribute("href")
    urls.append(url)

# follow the links
for url in urls:
    driver.get(url)
    driver.implicitly_wait(3)
    # find all paragraph elements that contain the article title and text
    title_object = driver.find_elements("xpath","/html/body/div[3]/div[2]/div/div[1]/h3")
    paragraphs = driver.find_elements("xpath", "//div[@class='col-xs-12 col-sm-8 col-md-8']/p")

    
    # concatenate the text content of all the paragraphs into a single string
    article = ""
    for p in paragraphs:
        article += p.text + " "

    # remove any extra whitespace from the string
    article = article.strip()
    
   
    # get the sentiment of the article text using the sentiment analyzer
    sentiment = sia.polarity_scores(article)
    title = title_object[0].text
    print(f"title: {title}")
    # print the sentiment scores
    #print(f"Sentiment for article: {article}")
    print(f"Positive sentiment: {sentiment['pos']}")
    print(f"Negative sentiment: {sentiment['neg']}")
    print(f"Neutral sentiment: {sentiment['neu']}")
    print(f"Compound sentiment: {sentiment['compound']}\n")
    
    blob = TextBlob(article)

    # get the sentiment polarity (-1 to 1)
    sentiment = blob.sentiment.polarity

    # print the sentiment polarity and the article content
    print("Title: ", title)
    print("Sentiment polarity:", sentiment)
    print("\n")
# close the browser
driver.quit()







