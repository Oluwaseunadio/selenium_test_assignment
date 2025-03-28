import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

# declare variables
email = "seun@gmail.com"
password  = "Test@1234"
Time = 3
URL = "https://automationplayground.com/crm/login.html"
firstname = "seun"
lastname = "Adio"
city = "lagos"



#initializing browser
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(Time)

# fill login details
Email = driver.find_element(By.ID, "email-id")
Email.send_keys(email)

Password = driver.find_element(By.ID, "password")
Password.send_keys(password)

Remember = driver.find_element(By.ID, "remember")
Remember.click()

Submit = driver.find_element(By.ID, "submit-id")
Submit.click()
time.sleep(Time)

# add new customer
NewCustomer = driver.find_element(By.ID, "new-customer")
NewCustomer.click()

Email = driver.find_element(By.ID, "EmailAddress")
Email.send_keys(email)

FirstName = driver.find_element(By.ID, "FirstName")
FirstName.send_keys(firstname)

LastName = driver.find_element(By.ID, "LastName")
LastName.send_keys(lastname)

City = driver.find_element(By.ID, "City")
City.send_keys(city)

State_Dropdown = Select(driver.find_element(By.ID, "StateOrRegion"))
State_Dropdown.select_by_visible_text("Colorado")

Gender = driver.find_element(By.NAME, "gender")
Gender.click()

Check = driver.find_element(By.NAME, "promos-name" )
Check.click()
time.sleep(Time)

submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
submit.click()
time.sleep(Time)

# SignOut
sign_out = driver.find_element(By.LINK_TEXT, "Sign Out")
sign_out.click()
time.sleep(Time)