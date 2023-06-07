from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

driver_path = r"C:\Users\admin\development\chromedriver.exe"
option = ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=driver_path, options=option)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(By.ID, "cookie")
selector_list = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]
five_sec_ahead = time.time()+5
time_out = time.time()+(60*5)
while True:
    cookie_button.click()
    if time.time() > five_sec_ahead:
        addon_details_elements = driver.find_elements(By.CSS_SELECTOR, "div #store div b")
        addon_details_elements.pop()
        cost_list = []
        for element in addon_details_elements:
            cost_list.append(int(element.text.split(" - ")[1].replace(",", "", 3)))
        money = int(driver.find_element(By.ID, "money").text)
        while len(cost_list) != 0:
            addon_rate = max(cost_list)
            if addon_rate < money:
                index = cost_list.index(addon_rate)
                selector = selector_list[index]
                break
            else:
                cost_list.pop()
        driver.find_element(By.ID, selector).click()
        five_sec_ahead = time.time() + 5
    if time.time() > time_out:
        break