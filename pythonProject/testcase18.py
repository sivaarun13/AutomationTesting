from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that categories are visible on left side bar
4. Click on 'Women' category
5. Click on any category link under 'Women' category, for example: Dress
6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
7. On left side bar, click on any sub-category link of 'Men' category
8. Verify that user is navigated to that category page
"""

class Testcase18(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            self.scroll_down(500)
            self.validate_category()
            self.click_category('Women', 'Tops')
            self.validate_category_page_is_displayed('Women - Tops Products')
            self.click_category('Men', 'Tshirts')
            self.validate_category_page_is_displayed('Men - Tshirts Products')

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase18()
    testcase.execute_testcase()


