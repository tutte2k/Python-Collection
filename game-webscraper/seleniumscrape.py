
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc
driver = uc.Chrome(use_subprocess=True)
driver.get('https://dura-online.com/?online')
driver.implicitly_wait(time_to_wait=10)

try:
    element = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.ID, "ContentHelper"))
    )
finally:
    driver.quit()