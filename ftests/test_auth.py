from .base import FunctionalTest

class AccountCreationTests(FunctionalTest):

    def test_account_creation(self):
        # User goes to the home page
        self.browser.get(self.live_server_url + "/")

        # There is the option to create an account and login
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Sign Up")
        self.assertEqual(auth_links[1].text, "Log In")

        # User clicks the sign up link and is taken to the sign up page
        auth_links[0].click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/accounts/signup/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h1").text,
         "Create an account."
        )

        # User fills out form
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("Joe")
        inputs[1].send_keys("Blow")
        inputs[2].send_keys("testemail@samireland.com")
        inputs[3].send_keys("secret_shhh")
        inputs[-1].click()

        # The user is taken to the account page for their new account
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/myaccount/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h1"),
         "Account"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h2"),
         "Joe Blow"
        )
