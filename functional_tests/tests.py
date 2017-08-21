from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Chrome(service_args=["--log-path=./chromedriver.log"])

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a cool new online to-do app. She goes to check out its homepage
    self.browser.get(self.live_server_url)

    # She is invited to enter a to-do item straight away
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text

    self.assertIn('To-Do', header_text)

    # She is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    # She types "Buy peacock feathers" into a text box
    inputbox.send_keys('Buy peacock feathers')

    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

    # There is still a text box for adding another item. She enters use peacock
    # feathers to make a fly.
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    # The page updates and displays both items in the table
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
    self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

    self.fail('Finish the test!')
