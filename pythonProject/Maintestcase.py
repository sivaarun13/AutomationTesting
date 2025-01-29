from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class user():

    def click_menu_items(self, menu_items):
        self.driver.find_element(By.XPATH, f"//a[contains(text(),'{menu_items}')]").click()

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, f"//input[@name ='name']").send_keys(name)

    def enter_Email(self, Email, email_type):
        self.driver.find_element(By.XPATH, f"//input[@data-qa='{email_type}-email']").send_keys(Email)

    def submit_button(self, Button):
        self.driver.find_element(By.XPATH, f"//button[text()='{Button}']").click()

    def Day_Month_year(self, Day, Month, Year):
        self.driver.find_element(By.XPATH, f"//select[@id='days']/option[@value='{Day}']").click()
        self.driver.find_element(By.XPATH, f"//select[@id='months']/option[@value='{Month}']").click()
        self.driver.find_element(By.XPATH, f"//select[@id='years']/option[@value='{Year}']").click()

    def Checkbox(self, Checkbox):
        self.driver.find_element(By.XPATH, f"//input[@name='{Checkbox}']").click()

    def radio_button(self, Gender):
        self.driver.find_element(By.XPATH, f"//input[@value='{Gender}']").click()

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, f"//input[@id='password' or @name='password']").send_keys(password)

    def Enter_Details(self, first_name, last_name, company_Name, address1, address2, country, state, city, zipcode,
                      mobile_number):
        self.driver.find_element(By.XPATH, f"//input[@name ='first_name']").send_keys(first_name)
        self.driver.find_element(By.XPATH, f"//input[@name ='last_name']").send_keys(last_name)
        self.driver.find_element(By.XPATH, f"//input[@id='company']").send_keys(company_Name)
        self.driver.find_element(By.XPATH, f"//input[@id='address1']").send_keys(address1)
        self.driver.find_element(By.XPATH, f"//input[@id='address2']").send_keys(address2)
        self.driver.find_element(By.XPATH, f"//select[@id='country']/option[@value='{country}']").click()
        self.driver.find_element(By.XPATH, f"//input[@id='state']").send_keys(state)
        self.driver.find_element(By.XPATH, f"//input[@id='city']").send_keys(city)
        self.driver.find_element(By.XPATH, f"//input[@id='zipcode']").send_keys(zipcode)
        self.driver.find_element(By.XPATH, f"//input[@id='mobile_number']").send_keys(mobile_number)

    def validate_home_page_is_visible_successfully(self):
        home = self.driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
        if home.is_displayed():
            print('Home page is visible')
        else:
            print("Home is not visible")

    def validate_New_User_Signup_is_visible(self):
        check = self.driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
        if check.is_displayed():
            print("New User Signup is visible")
        else:
            print("New User Signup is not visible")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def validate_account_created_is_visible(self):
        Account = self.driver.find_element(By.XPATH, "//h2[@class='title text-center']")
        if Account.is_displayed():
            print("Account created")
        else:
            print("Account is not created")

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()

    def validated_logged_in_as_username(self, user_name):
        username = self.driver.find_element(By.XPATH, f"//a[contains(text(),'Logged in as ')]/b[text()='{user_name}']")
        if username.is_displayed():
            print("username is visible")
        else:
            print("username is not visible")

    def validate_ACCOUNT_DELETED_is_visible(self):
        Delete = self.driver.find_element(By.XPATH, "//h2[@class='title text-center']")
        if Delete.is_displayed():
            print("Account Deleted")
        else:
            print("Account not deleted")

    def validate_Login_to_your_account_is_visible(self):
        login = self.driver.find_element(By.XPATH, "//div/h2[text()='Login to your account']")
        if login.is_displayed():
            print("login to your account is visible")
        else:
            print("login to your account is not visible")

    def validate_Your_email_or_password_is_incorrect(self):
        incorrect = self.driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']")
        if incorrect.is_displayed():
            print("Your email or password is incorrect is visible")
        else:
            print("Your email or password is incorrect is not visible")

    def validate_Your_email_or_password_is_incorrect_is_visible(self):
        error = driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']")
        if error.is_displayed():
            print("error message shown")
        else:
            print("error message not shown")

