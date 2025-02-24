from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill email, password and click 'Login' button
6. Verify 'Logged in as username' at top
7. Add products to cart
8. Click 'Cart' button
9. Verify that cart page is displayed
10. Click Proceed To Checkout
11. Verify Address Details and Review Your Order
12. Enter description in comment text area and click 'Place Order'
13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
14. Click 'Pay and Confirm Order' button
15. Verify success message 'Your order has been placed successfully!'
16. Click 'Delete Account' button
17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase16(user):
    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items('Signup / Login')
            self.enter_Email("pawankalyan18092002@gmail.com", 'login')
            self.enter_password('sivaarun@123')
            self.submit_button('Login')
            self.validated_logged_in_as_username("Siva Arun")
            self.scroll_down(700)
            self.click_product(1)
            self.add_to_cart()
            self.click_menu_items('Home')
            self.scroll_down(700)
            self.click_product(2)
            self.add_to_cart()
            self.click_menu_items('Cart')
            self.validate_cart_page()
            self.proceed_to_checkout()
            self.validate_address_details_and_review_order()
            self.scroll_down(200)
            self.enter_description('Hi')
            self.place_order()
            self.card_details('Arun', '82545300245', '525', '07', '2052')
            self.submit_button('Pay and Confirm Order')
            self.click_continue()
            self.click_menu_items('Delete Account')
            self.validate_ACCOUNT_DELETED_is_visible()
            self.click_continue()

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase16()
    testcase.execute_testcase()
