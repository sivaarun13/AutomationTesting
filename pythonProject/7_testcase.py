from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Test Cases' button
5. Verify user is navigated to test cases page successfully
"""

class Testcase7(user):
    def execute_testcase(self):
        try:
            """Initialize browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items('Test Cases')
            self.validate_entered_test_case_page()

        except Exception as exp:
            print(f"Error during Test Execution:{exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase7()
    testcase.execute_testcase()






















# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://automationexercise.com")
# home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
# if home.is_displayed():
#     print('Home page is visible')
# else:
#     print("Home is not visible")
#
# driver.find_element(By.XPATH, "//a[text()=' Test Cases']").click()
# verify = driver.find_element(By.XPATH, "//h2/b[text()='Test Cases']")
# if verify.is_displayed():
#     print("Test Cases is visible")
# else:
#     print("Test case is not visible")
