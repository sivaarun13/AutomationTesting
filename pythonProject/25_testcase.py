import time
from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user
from selenium.webdriver.common.by import By


"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify 'SUBSCRIPTION' is visible
6. Click on arrow at bottom right side to move upward
7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
"""

class Testcase25(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            element = self.driver.find_element(By.XPATH, "//h2[text()='Subscription']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.validate_subscription_is_visible()
            time.sleep(5)
            self.click_arrow_button()
            time.sleep(5)
            self.validate_home_page_is_visible_successfully()

        except Exception as exp:
            print(f'Error during test execution{exp}')

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase25()
    testcase.execute_testcase()