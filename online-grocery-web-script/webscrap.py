#import the library used to query a website
import urllib2

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import csv


driver = webdriver.Chrome(executable_path=r"../chromedriver")
driver.get("http://www.publix.com/pd/ritz-crackers/RIO-PCI-145295?ch=9.13.")

try:
    title = driver.find_element_by_class_name("fda-title").text
except NoSuchElementException:
    title = ""

try:
    size = driver.find_element_by_class_name("size-description").text
except NoSuchElementException:
    size = ""

try:
    showMore = driver.find_element_by_class_name("morelink")
    showMore.send_keys('\n')
    driver.implicitly_wait(0.25)
    description = driver.find_element_by_class_name("shortened").text + driver.find_element_by_class_name("nomoregaps").text
except NoSuchElementException:
    description = ""

try:
    image = driver.find_element_by_class_name("main-image").get_attribute("src")
except NoSuchElementException:
    image = ""

try:
    nutritionButton = driver.find_element_by_id("ui-id-3")
    nutritionButton.send_keys('\n')
    driver.implicitly_wait(0.25)
    try:
        nutritionFacts = driver.find_element_by_class_name("nutritionLabel").text
    except NoSuchElementException:
        nutritionFacts = ""
    try:
        ingredients = driver.find_element_by_id("content_0_NutritionalFactsRepeater_FactName_0").text
    except NoSuchElementException:
        ingredients = ""
    try:
        allergens = driver.find_element_by_id("content_0_NutritionalFactsRepeater_FactName_1").text
    except NoSuchElementException:
        allergens = ""
except NoSuchElementException:
    nutritionFacts = ""
    ingredients = ""
    allergens = ""


print title + '\n' + size + '\n' + description + '\n' + image + '\n' + nutritionFacts + '\n' + ingredients + '\n' + allergens