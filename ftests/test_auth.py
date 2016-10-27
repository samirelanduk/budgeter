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
         self.live_server_url + "/users/signup/"
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
         self.live_server_url + "/users/me/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h1").text,
         "Account"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h2").text,
         "Joe Blow"
        )



class AccountLoginTests(FunctionalTest):

    def test_can_login(self):
        # User goes to the home page
        self.browser.get(self.live_server_url + "/")

        # There is the option to create an account and login
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Sign Up")
        self.assertEqual(auth_links[1].text, "Log In")

        # User clicks the log in and is taken to the log in page
        auth_links[1].click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/login/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h1").text,
         "Log in to your account"
        )

        # User enters their details
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p1@s.com")
        inputs[1].send_keys("secret1")
        inputs[-1].click()

        # The user is back on the home page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")

        # There is a logout link now
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log Out")

        # There is a link to the account page
        account_div = self.browser.find_element_by_id("account")
        account_link = account_div.find_element_by_tag_name("a")
        self.assertEqual(account_link.text, "Your Account")
        account_link.click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/me/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h2").text,
         "Persona Una"
        )


    def test_invalid_credentials_wont_login(self):
        # User goes to login page
        self.browser.get(self.live_server_url + "/users/login/")

        # They try to login in with an incorrect email
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("wrong@s.com")
        inputs[1].send_keys("secret1")
        inputs[-1].click()

        # They are stll on the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/login/"
        )

        # There is an error message
        errors = self.browser.find_element_by_id("login_errors")
        self.assertEqual(
         errors.text,
         "Credentials incorrect."
        )

        # They try again with an incorrect password
        self.browser.get(self.live_server_url + "/users/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p1@s.com")
        inputs[1].send_keys("wrongpassword")
        inputs[-1].click()

        # They are stll on the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/login/"
        )

        # There is an error message
        errors = self.browser.find_element_by_id("login_errors")
        self.assertEqual(
         errors.text,
         "Credentials incorrect."
        )


    def test_can_logout(self):
        # User logs in
        self.browser.get(self.live_server_url + "/users/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p2@s.com")
        inputs[1].send_keys("secret2")
        inputs[-1].click()

        # They are on the home page and there is a logout link
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log Out")

        # They click it and are logged out
        auth_links[0].click()
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Sign Up")
        self.assertEqual(auth_links[1].text, "Log In")
