from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")

register = driver.find_element(By.XPATH, "//a[@class='ico-register']")
register.click()

male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
male.click()

first_name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
first_name.send_keys("Singanallur")

second_name = driver.find_element(By.XPATH, "//input[@id='LastName']")
second_name.send_keys("Muthuraj")

email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.send_keys("singanallur.muthuraj@gmail.com")

password = driver.find_element(By.XPATH, "//input[@id='Password']")
password.send_keys("mayura")

confirm_password = driver.find_element(
    By.XPATH, "//input[@id='ConfirmPassword']")
confirm_password.send_keys("mayura")

register_submit = driver.find_element(
    By.XPATH, "//input[@id='register-button']")
register_submit.click()

sleep(10)
