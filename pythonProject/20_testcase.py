import time

from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Enter product name in search input and click search button
6. Verify 'SEARCHED PRODUCTS' is visible
7. Verify all the products related to search are visible
8. Add those products to cart
9. Click 'Cart' button and verify that products are visible in cart
10. Click 'Signup / Login' button and submit login details
11. Again, go to Cart page
12. Verify that those products are visible in cart after login as well
"""

class Testcase20(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.click_menu_items('Products')
            self.validate_all_products_page()
            self.search_bar('winter top')
            self.validate_searched_product_is_visible()
            self.scroll_down(500)
            self.click_product()
            self.add_to_cart()
            self.view_cart()
            self.get_cart_products()
            self.click_menu_items('Signup / Login')
            self.enter_Email("pawankalyan18092002@gmail.com", "login")
            self.enter_password('sivaarun@123')
            self.click_menu_items('Cart')
            self.get_cart_products()

        except Exception as exp:
            print(f'Error During Test Execution:{exp}')

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase20()
    testcase.execute_testcase()
