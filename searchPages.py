import selenium
from selenium import webdriver

browser = webdriver.Chrome()

search_string = 'San diego hidden gems'

for i in range(2):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))
    print(matched_elements)

if __name__ == "__main__":
    print('main')