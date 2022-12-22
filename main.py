import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)

chrome_path = "C:\\Users\\USER\\Desktop\\my_python\\chromedriver.exe"
game_url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service_log_path=chrome_path, options=options)
driver.get(game_url)
cookie_count = driver.find_element(By.CSS_SELECTOR, "#money")
cookie_but = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
items = [item.text for item in store]

print(items)
# for item in items:
#     list=re.split("\n|-",item)
#     print(list)
#
# money_text = [re.split("\n|-", item)[1].strip() for item in items[:-1]]
# money_int = [int(item.replace(",", "")) for item in money_text]
# print(money_int)

count = 0

timeout = 60  # in seconds

timeout_start = time.time()
print(timeout_start)
diff = 0
while diff <= timeout:
    cookie_but.click()

    if diff%6>=0 and diff%6<=0.05:
        store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        items = [item.text for item in store]
        # print(items)
        # money_text = [re.split("\n|-", item)[1].strip() for item in items[:-1]]
        money_text=[]
        for item in items[:-1]:
            list=re.split("\n|-",item)
            # print(list)
            money_text.append(list[1].strip())

        # print(money_text)
        money_int = [int(item.replace(",","")) for item in money_text]
        # print(money_int)
        max=0
        for i in range(len(money_int)):
            if money_int[i]<=int(cookie_count.text.replace(",","")):
                max=i
        print(max)
        # affordable_id=store[max].get_attribute("id")        #PROBLEM WITH GETTING ID
        # print(affordable_id)
        store[max].click()
        # print(driver.find_element(by=By.ID,value=affordable_id))
        print("clicked")
        count+=1
    diff=time.time()-timeout_start



score = driver.find_element(by=By.CSS_SELECTOR, value="#cps").text
print(score)
print(count)
driver.quit()
