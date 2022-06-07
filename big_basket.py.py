from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl


driver = webdriver.Chrome("//india.eclerx.com/ctrxdata/ARRDATA/Akshay.Deokar/Desktop/Re/chromedriver.exe")
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
time.sleep(2)

category = driver.find_element(by=By.XPATH, value='//*[@id="store-entry"]/div[1]/div/div[4]/div/div/a')
category.click()
time.sleep(2)


product_name = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/a ')
product_mrp = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]')
product_wt = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[2]/div/span/button/span/span[1]')

name, mrp, wt = [],[],[]

for x in product_name:
    name.append(x.text)
for y in product_mrp:
    mrp.append(y.text)
for z in product_wt:
    wt.append(z.text)


final_sheet = zip(name, mrp, wt)

wb = openpyxl.Workbook()
sheet = wb.active
for i in list(final_sheet):
    sheet.append(i)
    wb.save("Ayurved_Data.xlsx")
    wb.save("Ayurved_Data.csv")

driver.quit()
