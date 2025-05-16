from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")


    try:
        more_info_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://www.iana.org/help/example-domains']"))
        )
        print("Элемент найден, кликаем по нему...")
        more_info_button.click()


        time.sleep(3)
        assert driver.current_url == "https://www.iana.org/help/example-domains", "Перенаправление не произошло"
        print("Тест прошел успешно!")

    except Exception as e:
        print(f"Ошибка при поиске элемента: {e}")

except Exception as e:
    print(f"Ошибка при запуске драйвера: {e}")

finally:
    driver.quit()
