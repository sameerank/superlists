from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome(service_args=["--log-path=./chromedriver.log"])

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a cool new online to-do app. She goes to check out its homepage
    self.browser.get('http://localhost:8000')

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
    self.assertTrue(
      any(row.text == '1: Buy peacock feathers' for row in rows),
      "New to-do items do not appear in table"
    )

    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')
