import time

from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click 'X' button corresponding to particular product
8. Verify that product is removed from the cart
"""

class Testcase17(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            self.scroll_down(700)
            self.click_product(1)
            self.add_to_cart()
            self.click_menu_items('Home')
            self.scroll_down(700)
            self.click_product(2)
            self.add_to_cart()
            self.click_menu_items('Cart')
            self.validate_cart_page()
            self.remove_product_from_cart(1)
            self.remove_product_from_cart(2)
            self.validate_cart_is_empty()

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase17()
    testcase.execute_testcase()