import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.Maintestcase import user


"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Scroll to bottom of page
4. Verify 'RECOMMENDED ITEMS' are visible
5. Click on 'Add To Cart' on Recommended product
6. Click on 'View Cart' button
7. Verify that product is displayed in cart page
"""

class Testcase22(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            element = self.driver.find_element(By.XPATH,
                                               '//h2[@class="title text-center" and contains(text(),"recommended items")]')

            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.validate_recommended_items_is_visible()
            time.sleep(10)
            self.add_to_cart_in_recommended_items(1)
            self.view_cart()
            self.get_cart_products()

        except Exception as exp:
            print(f"error during text execution {exp}")

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase22()
    testcase.execute_testcase()