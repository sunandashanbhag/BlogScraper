# import requests
import selenium
from selenium import webdriver

url = 'https://www.trolleytours.com/san-diego/hidden-gems'
driver = webdriver.Chrome()
driver.get(url)

all_headers = driver.find_elements_by_tag_name('h2')
all_text = driver.find_elements_by_tag_name('p')

for header in all_headers:
    # header_txt = header.find_elements_by_tag_name('p')
    # for ht in header_txt:
    #     print(ht.text)
    print(header.text)

for txt in all_text:
    print(txt.text)

if __name__ == "__main__":
    main()
