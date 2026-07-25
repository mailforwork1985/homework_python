from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    start_url = "https://httpbin.qa-territory.online/forms/post"

    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.find_element(By.NAME, "custname").send_keys("Olga")
    driver.find_element(By.TAG_NAME, "button").click()

    assert driver.current_url == start_url
    driver.quit()
