from .base import FunctionalTest

class HomePageTests(FunctionalTest):

    def test_home_page_heading(self):
        # User goes to the home page
        self.browser.get(self.live_server_url + "/")

        # The site name is in the title and heading
        self.assertEqual("Budgeter", self.browser.title)
        self.assertEqual(
         "Budgeter",
         self.browser.find_element_by_tag_name("h1").text
        )
