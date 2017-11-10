#import the library used to query a website
import urllib2
import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import scrapy


from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"../chromedriver")
browser.get("http://www.publix.com/product-catalog/productlisting?ch=9.13.&page=1&count=96")


#Specify the url
linkToLoad = "http://www.publix.com/pd/ritz-crackers/RIO-PCI-145295?ch=9.13."


#opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie', 'bzip=95030'))
# opener.addheaders.append(('Cookie', 'gzip=95030'))
# f = opener.open(wiki)
page = urllib2.urlopen(linkToLoad)

# use selenium to get the entire page

#class ProductSpider(scrapy.Spider)
   # name = "product_spider"

   # def __init__(self):
   #     self.driver = browser

  #  def parse(self, response):
  #      self.driver.get(response.url)

  #      while True:
#print browser.find_element_by_class_name("fda-title").text
#print browser.find_element_by_class_name("size-description").text
#print browser.find_element_by_class_name("shortened").text
#print browser.find_element_by_class_name("image").text
#print browser.find_element_by_id("ui-id-3").click()

browser.implicitly_wait(3)

refList = browser.find_elements_by_class_name("toggle-qv")

urlList = []

for x in refList:
    if x.get_attribute('href') != None :
        print x.get_attribute('href')
        urlList.append(x.get_attribute('href'))

i = 0
for y in urlList:
    driver = webdriver.Chrome(executable_path=r"../chromedriver")
    driver.get(y)
    print driver.find_element_by_class_name("fda-title").text
    print driver.find_element_by_class_name("size-description").text
    if i > 40:
        break
    else:
        i = i + 1

listOfCategories = driver.find_elements_by_class_name("unstyled")

for y in listOfCategories:
    if y.get_attribute('href') != None :
       print y.get_attribute('href')



# browser.switch_to.frame(0);
#browser.implicitly_wait(3);
# print browser.find_element_by_id("content_0_NutritionalFactsRepeater_FactName_1").text
#print browser.find_element_by_css_selector("content_0_NutritionalFactsRepeater_FactName_1").text

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html.parser")

# letters = soup.find_all("href="/pd/")

# print soup.prettify()
