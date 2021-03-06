from .base import FunctionalTest

class AccountCreationTests(FunctionalTest):

    def test_account_creation(self):
        # User goes to the home page
        self.browser.get(self.live_server_url + "/")

        # There is a form to signup, which they fill in
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
         self.live_server_url + "/profile/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h1").text,
         "Account"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h2").text,
         "Joe Blow"
        )


    def test_cannot_create_account_with_existing_email(self):
        # The user goes to the signup page
        self.browser.get(self.live_server_url + "/")

        # User fills out form with a pre-existing email address
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("Joe")
        inputs[1].send_keys("Blow")
        inputs[2].send_keys("p1@s.com")
        inputs[3].send_keys("secret_shhh")
        inputs[-1].click()

        # They are still on the home page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )

        # There is a message telling them the email already exists
        # (This is probably fine for now - no real harm I don't think)
        form = self.browser.find_element_by_tag_name("form")
        email_error_div = form.find_element_by_id("email_error")
        self.assertEqual(
         email_error_div.text,
         "There is already a user account with that email."
        )

        # The supplied data is still there (but not the password)
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("value"), "Joe")
        self.assertEqual(inputs[1].get_attribute("value"), "Blow")
        self.assertEqual(inputs[2].get_attribute("value"), "p1@s.com")
        self.assertEqual(inputs[3].get_attribute("value"), "")


    def test_cannot_sign_up_without_fields(self):
        # The user goes to the signup page
        self.browser.get(self.live_server_url + "/")

        # User fills out form with no first name
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[1].send_keys("Blow")
        inputs[2].send_keys("testemail@samireland.com")
        inputs[3].send_keys("secret_shhh")
        inputs[-1].click()

        # They are still on the home page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )

        # There is a message telling them they need a first name
        form = self.browser.find_element_by_tag_name("form")
        firstname_error_div = form.find_element_by_id("firstname_error")
        self.assertEqual(
         firstname_error_div.text,
         "You need to supply a first name."
        )

        # The supplied data is still there (but not the password)
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("value"), "")
        self.assertEqual(inputs[1].get_attribute("value"), "Blow")
        self.assertEqual(inputs[2].get_attribute("value"), "testemail@samireland.com")
        self.assertEqual(inputs[3].get_attribute("value"), "")

        # They try again without the last name
        self.browser.get(self.live_server_url + "/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("Joe")
        inputs[2].send_keys("testemail@samireland.com")
        inputs[3].send_keys("secret_shhh")
        inputs[-1].click()

        # There is a message telling them they need a last name
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )
        form = self.browser.find_element_by_tag_name("form")
        lastname_error_div = form.find_element_by_id("lastname_error")
        self.assertEqual(
         lastname_error_div.text,
         "You need to supply a last name."
        )

        # The supplied data is still there (but not the password)
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("value"), "Joe")
        self.assertEqual(inputs[1].get_attribute("value"), "")
        self.assertEqual(inputs[2].get_attribute("value"), "testemail@samireland.com")
        self.assertEqual(inputs[3].get_attribute("value"), "")

        # They try again without the email
        self.browser.get(self.live_server_url + "/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("Joe")
        inputs[1].send_keys("Blow")
        inputs[3].send_keys("secret_shhh")
        inputs[-1].click()

        # There is a message telling them they need an email
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )
        form = self.browser.find_element_by_tag_name("form")
        email_error_div = form.find_element_by_id("email_error")
        self.assertEqual(
         email_error_div.text,
         "You need to supply an email."
        )

        # The supplied data is still there (but not the password)
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("value"), "Joe")
        self.assertEqual(inputs[1].get_attribute("value"), "Blow")
        self.assertEqual(inputs[2].get_attribute("value"), "")
        self.assertEqual(inputs[3].get_attribute("value"), "")

        # They try again without the password
        self.browser.get(self.live_server_url + "/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("Joe")
        inputs[1].send_keys("Blow")
        inputs[2].send_keys("testemail@samireland.com")
        inputs[-1].click()

        # There is a message telling them they need an password
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )
        form = self.browser.find_element_by_tag_name("form")
        password_error_div = form.find_element_by_id("password_error")
        self.assertEqual(
         password_error_div.text,
         "You need to supply a password."
        )

        # The supplied data is still there (but not the password)
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("value"), "Joe")
        self.assertEqual(inputs[1].get_attribute("value"), "Blow")
        self.assertEqual(inputs[2].get_attribute("value"), "testemail@samireland.com")
        self.assertEqual(inputs[3].get_attribute("value"), "")

        # In protest they try sending the form with no data at all
        self.browser.get(self.live_server_url + "/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[-1].click()

        # There are error messages for each missing field
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/"
        )
        form = self.browser.find_element_by_tag_name("form")
        firstname_error_div = form.find_element_by_id("firstname_error")
        self.assertEqual(
         firstname_error_div.text,
         "You need to supply a first name."
        )
        lastname_error_div = form.find_element_by_id("lastname_error")
        self.assertEqual(
         lastname_error_div.text,
         "You need to supply a last name."
        )
        email_error_div = form.find_element_by_id("email_error")
        self.assertEqual(
         email_error_div.text,
         "You need to supply an email."
        )
        password_error_div = form.find_element_by_id("password_error")
        self.assertEqual(
         password_error_div.text,
         "You need to supply a password."
        )



class AccountLoginTests(FunctionalTest):

    def test_can_login(self):
        # User goes to the home page
        self.browser.get(self.live_server_url + "/")

        # There is the option to create an account and login
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log In")

        # User clicks the log in and is taken to the log in page
        auth_links[0].click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
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
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Log Out")
        self.assertEqual(auth_links[1].text, "Your Account")

        # There is a link to the account page
        account_div = self.browser.find_element_by_id("account")
        account_link = account_div.find_element_by_tag_name("a")
        self.assertEqual(account_link.text, "Your Account")
        account_link.click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/profile/"
        )
        self.assertEqual(
         self.browser.find_element_by_tag_name("h2").text,
         "Persona Una"
        )

        # The signup form is gone from the hone page
        self.browser.get(self.live_server_url + "/")
        forms = self.browser.find_elements_by_tag_name("form")
        self.assertEqual(len(forms), 0)


    def test_invalid_credentials_wont_login(self):
        # User goes to login page
        self.browser.get(self.live_server_url + "/login/")

        # They try to login in with an incorrect email
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("wrong@s.com")
        inputs[1].send_keys("secret1")
        inputs[-1].click()

        # They are stll on the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
        )

        # There is an error message
        errors = self.browser.find_element_by_id("login_errors")
        self.assertEqual(
         errors.text,
         "Credentials incorrect."
        )

        # They try again with an incorrect password
        self.browser.get(self.live_server_url + "/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p1@s.com")
        inputs[1].send_keys("wrongpassword")
        inputs[-1].click()

        # They are stll on the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
        )

        # There is an error message
        errors = self.browser.find_element_by_id("login_errors")
        self.assertEqual(
         errors.text,
         "Credentials incorrect."
        )


    def test_can_logout(self):
        # User logs in
        self.browser.get(self.live_server_url + "/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p2@s.com")
        inputs[1].send_keys("secret2")
        inputs[-1].click()

        # They are on the home page and there is a logout link
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Log Out")

        # They click it and are logged out
        auth_links[0].click()
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log In")



class AccountPageTests(FunctionalTest):

    def test_cannot_access_account_page_without_logging_in(self):
        # The user tries to access the account page
        self.browser.get(self.live_server_url + "/profile/")

        # They have been redirected to the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
        )



class AccountDeletionTests(FunctionalTest):

    def test_can_delete_account(self):
        # User logs in
        self.browser.get(self.live_server_url + "/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p2@s.com")
        inputs[1].send_keys("secret2")
        inputs[-1].click()

        # They go to their account page
        self.browser.get(self.live_server_url + "/profile/")

        # There is a delete button - they click it
        delete_section = self.browser.find_element_by_id("delete_section")
        delete_button = delete_section.find_element_by_tag_name("a")
        self.assertEqual(delete_button.text, "Delete Account")
        delete_button.click()

        # They are on the delete account page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/delete/"
        )

        # There is a warning that this cannot be undone
        form = self.browser.find_element_by_tag_name("form")
        self.assertIn("Warning", form.text)
        inputs = form.find_elements_by_tag_name("input")
        self.assertEqual(inputs[0].get_attribute("type"), "password")
        back_button = form.find_element_by_tag_name("a")
        self.assertEqual(
         back_button.get_attribute("href"),
         self.live_server_url + "/profile/"
        )

        # They enter their password and delete the account
        inputs[0].send_keys("secret2")
        inputs[-1].click()

        # They are logged out and on the home page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log In")

        # They cannot log back in
        self.browser.get(self.live_server_url + "/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p2@s.com")
        inputs[1].send_keys("secret2")
        inputs[-1].click()
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
        )
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 1)
        self.assertEqual(auth_links[0].text, "Log In")


    def test_need_password_to_delete_account(self):
        # User logs in
        self.browser.get(self.live_server_url + "/login/")
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        inputs[0].send_keys("p2@s.com")
        inputs[1].send_keys("secret2")
        inputs[-1].click()

        # The user goes to delete their account
        self.browser.get(self.live_server_url + "/profile/")
        delete_section = self.browser.find_element_by_id("delete_section")
        delete_button = delete_section.find_element_by_tag_name("a")
        self.assertEqual(delete_button.text, "Delete Account")
        delete_button.click()
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")

        # THe enter the wrong password and try to delete
        inputs[0].send_keys("wrong")
        inputs[-1].click()

        # They are still on the delete page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/users/delete/"
        )
        form = self.browser.find_element_by_tag_name("form")
        password_error_div = form.find_element_by_id("password_error")
        self.assertEqual(
         password_error_div.text,
         "Credentials invalid."
        )

        # They are still logged in
        auth_div = self.browser.find_element_by_id("auth")
        auth_links = auth_div.find_elements_by_tag_name("a")
        self.assertEqual(len(auth_links), 2)
        self.assertEqual(auth_links[0].text, "Log Out")
        self.assertEqual(auth_links[1].text, "Your Account")


    def test_cannot_access_account_deletion_page_without_logging_in(self):
        # The user tries to access the account page
        self.browser.get(self.live_server_url + "/users/delete/")

        # They have been redirected to the login page
        self.assertEqual(
         self.browser.current_url,
         self.live_server_url + "/login/"
        )
