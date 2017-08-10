from selenium import webdriver

browser = webdriver.Chrome(service_args=["--log-path=./chromedriver.log"])
browser.get('http://localhost:8000')

assert 'Django' in browser.title
