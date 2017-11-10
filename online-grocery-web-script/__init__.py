#import the library used to query a website
import urllib2

from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"../chromedriver")
browser.get("http://www.publix.com/product-catalog/productlisting?ch=9.13.&page=1&count=96")


#Specify the url
## NOTE: MUST DO THIS FOR EVERY PRODUCT PAGE (96 at a time)
linkToLoad = "http://www.publix.com/pd/ritz-crackers/RIO-PCI-145295?ch=9.13."

# f = opener.open(wiki)
page = urllib2.urlopen(linkToLoad)

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

    ## TODO: sydneypalumbo PUT ALL OF YOUR STUFF HERE ##

listOfCategories = driver.find_elements_by_class_name("unstyled")

for y in listOfCategories:
    if y.get_attribute('href') != None :
       print y.get_attribute('href')
