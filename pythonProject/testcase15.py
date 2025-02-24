from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify ' Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify Address Details and Review Your Order
13. Enter description in comment text area and click 'Place Order'
14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
15. Click 'Pay and Confirm Order' button
16. Verify success message 'Your order has been placed successfully!'
17. Click 'Delete Account' button
18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase15(user):
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
            self.enter_name("Siva Arun")
            self.enter_Email("pawankalyan18092002@gmail.com", "signup")
            self.submit_button("Signup")
            self.radio_button("Mr")
            self.enter_password("sivaarun@123")
            self.Day_Month_year("13", "11", "2000")
            self.scroll_down(500)
            self.Checkbox("newsletter")
            self.Enter_Details(
                "Siva",
                "Arun",
                "Commvault",
                "Bangame Tech Park",
                "Tin Factory",
                "India",
                "Karnataka",
                "Bangalore",
                "561203",
                "901443046"
            )
            self.scroll_down(500)
            self.submit_button("Create Account")
            self.validate_account_created_is_visible()
            self.click_continue()
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
    testcase = Testcase15()
    testcase.execute_testcase()
