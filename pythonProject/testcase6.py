from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Contact Us' button
5. Verify 'GET IN TOUCH' is visible
6. Enter name, email, subject and message
7. Upload file
8. Click 'Submit' button
9. Click OK button
10. Verify success message 'Success! Your details have been submitted successfully.' is visible
11. Click 'Home' button and verify that landed to home page successfully
"""

class Testcase6(user):
    def execute_testcase(self):
        try:
            """Initialize browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items('Contact us')
            self.validate_get_in_touch_is_visible()
            self.enter_name("Siva Arun")
            self.enter_Email('pawankalyan18092002@gmail.com', 'email')
            self.enter_subject('error')
            self.enter_message('hi')
            self.upload_file('C://Users//arunc//Downloads//OG_INSTA POST')
            self.input_submit()
            self.click_alert()
            self.validate_success_message()
            self.click_home()
            self.validate_home_page_is_visible_successfully()

        except Exception as exp:
            print(f"Error during Test Execution:{exp}")

if __name__ == "__main__":
    testcase = Testcase6()
    testcase.execute_testcase()






























# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
#
# Name = "Siva Arun"
# Email = "pawankalyan18092002@gmail.com"
# Subject = "Error"
# Message = "Hi"
# File_path = "C://Users//arunc//Downloads//IMG_6626.jpg"
# print(File_path)
#
# driver = webdriver.Chrome()
# driver.get("http://automationexercise.com")
# home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
# if home.is_displayed():
#     print('Home page is visible')
# else:
#     print("Home is not visible")
# driver.find_element(By.XPATH, "//a/i[@class='fa fa-envelope']").click()
# Touch = driver.find_element(By.XPATH, "//div/h2[text()='Get In Touch']")
# if Touch.is_displayed():
#     print("Get In Touch Is Visible")
# else:
#     print("Get In Touch Is Visible is not visible")
# driver.find_element(By.XPATH, "//input[@data-qa = 'name']").send_keys(Name)
# driver.find_element(By.XPATH, "//input[@data-qa = 'email']").send_keys(Email)
# driver.find_element(By.XPATH, "//input[@data-qa = 'subject']").send_keys(Subject)
# driver.find_element(By.XPATH, "//textarea[@data-qa = 'message']").send_keys(Message)
# driver.find_element(By.XPATH, "//input[@name='upload_file']").send_keys(File_path)
# driver.find_element(By.XPATH, "//input[@data-qa ='submit-button']").click()
# alert= Alert(driver)
# alert.accept()
# verify = driver.find_element(By.XPATH, "//div[@class='status alert alert-success']")
# if verify.is_displayed():
#     print("Success! Your details have been submitted successfully is visible ")
# else:
#     print("Success! Your details have been submitted successfully is not visible ")
#
# driver.find_element(By.XPATH, "//i[@class='fa fa-angle-double-left']").click()
# home = driver.find_element(By.XPATH, "//div[@class = 'header-middle']")
# if home.is_displayed():
#     print('Home page is visible')
# else:
#     print("Home is not visible")