import selenium.webdriver.common.devtools.v108.input_
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestSaucedemo:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")
    #    return driver.find_element(By.ID, "login-button")

    def empty_username_and_password(self):
        login_button=self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text

        if error_message == "Epic sadface: Username is required":
            print("True")
        else:
            print("False")

    def empty_password_only(self):
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("username")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        if error_message == "Epic sadface: Password is required":
            print("True")
        else:
            print("False")

    def locked_out_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("locked_out_user")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        if error_message == "Epic sadface: Sorry, this user has been locked out.":
            print("True")
        else:
            print("False")

    def error_button(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        login_button.click()
        sleep(1)
        error_button=self.driver.find_element(By.CLASS_NAME, "error-button")
        error_button.click()
        sleep(1)

    def standard_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        sleep(3)

    def number_of_products(self):
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        products=self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(products) == 6:
            print("True")
        else:
            print("False")

TestSaucedemo().empty_username_and_password()
TestSaucedemo().empty_password_only()
TestSaucedemo().locked_out_user()
TestSaucedemo().error_button()
TestSaucedemo().standard_user()
TestSaucedemo().number_of_products()