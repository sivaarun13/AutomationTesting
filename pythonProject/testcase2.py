from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Delete Account' button
10. Verify that 'ACCOUNT DELETED!' is visible
"""


class Testcase2(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url= "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items("Signup / Login")
            self.validate_Login_to_your_account_is_visible()
            self.enter_Email("pawankalyan18092002@gmail.com", "login")
            self.enter_password("sivaarun@123")
            self.submit_button("Login")
            self.validated_logged_in_as_username('Siva Arun')
            self.click_menu_items('Delete Account')
            self.validate_ACCOUNT_DELETED_is_visible()

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase2()
    testcase.execute_testcase()