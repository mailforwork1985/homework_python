from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    base_url = "https://httpbin.qa-territory.online"

    driver = webdriver.Chrome()

    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    current_url = driver.current_url
    assert current_url.endswith("/forms/post")

    driver.back()

    assert driver.current_url.rstrip("/") == base_url

    driver.quit()
