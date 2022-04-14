from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')
driver.get("https://shopee.sg/search?keyword=cheese%20board&trackingId=searchhint-1624559471-59d502eb-d51a-11eb-87d8-08f1ea7dd290")
new_list = []
elem = driver.find_element_by_xpath('//*[contains(string(), "shopee-checkbox__label")]').text


print(elem)
assert "No results found." not in driver.page_source
driver.close()

