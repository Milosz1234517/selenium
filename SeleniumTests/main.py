from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()


driver.get('http://automationpractice.com/index.php')

search_field = driver.find_element(By.ID, 'search_query_top')
search_field.send_keys('dress')
search_field.submit()

try:
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "center_column"))
    )
    result2 = result.find_element(By.CLASS_NAME, 'product_list.grid.row')
    x = result2.find_elements(By.CLASS_NAME, 'right-block')
    for r in x:
        y = r.find_element(By.CLASS_NAME, 'product-name')
        z = r.find_element(By.CLASS_NAME, 'price.product-price')
        print(y.text + " " + z.text)
finally:
    driver.quit()
