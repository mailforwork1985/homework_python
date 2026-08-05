from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://www.gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "NWZlNDBkODktYjZkZC00N2YyLTkxNTMtYmUzMmNhYTczMTI4",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # 3. Обновите страницу.
    driver.refresh()
    # 4. Перейдите на страницу пользователя 1.
    driver.maximize_window()
    driver.get("https://gitflic.ru/user/user1_test")
    # 5. Сохраните текущий URL.
    url_user1 = driver.current_url
    # 6. Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()
    # 7. Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NTBlNjczNzEtNjYwMy00MDY2LWIwNTEtY2EzZWYyMDdiY2Fl",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # 8. Обновите страницу.
    driver.refresh()
    # 9. Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/user2_test")
    # 10. Сохраните текущий URL.
    url_user2 = driver.current_url
    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2

    driver.quit()
