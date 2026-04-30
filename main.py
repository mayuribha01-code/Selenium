from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.maximize_window()

wait = WebDriverWait(driver, 15)

# Search box
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)

search_box.send_keys("iphones")
search_box.send_keys(Keys.RETURN)

wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
)

products = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//h2//span"))
)

print(str(len(products)) + " products found")

for i in products:
    print(i.text)

driver.quit()