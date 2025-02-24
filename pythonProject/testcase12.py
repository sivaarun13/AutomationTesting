import time

from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price
"""

class Testcase12(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.click_menu_items('Products')
            self.scroll_down(500)
            self.click_product('1')
            time.sleep(5)
            # self.scroll_down(500)
            self.add_to_cart()
            self.continue_shopping()
            self.click_menu_items('Products')
            self.scroll_down(500)
            self.click_product('2')
            time.sleep(10)
            # self.driver.switch_to.default_content()
            self.add_to_cart()
            self.continue_shopping()
            self.click_menu_items('Cart')
            products = self.get_cart_products()
            if products:
                print(products)
            else:
                print("products are not found")

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__=="__main__":
    testcase = Testcase12()
    testcase.execute_testcase()



