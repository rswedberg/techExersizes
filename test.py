from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

import unittest

class HelloWorldTest(unittest.TestCase):
  def setUp(self):
    #create a headless Chrome browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    self.driver = webdriver.Chrome("C:\\Users\\Michelle\\Downloads\\chromedriver_win32\\chromedriver.exe", options=op)

  def test(self):
    # Get homepage
    self.driver.get("https://HelloWorld.mzietlow.repl.co")

    # Find textbox and enter integer to test
    textbox = self.driver.find_element_by_name("number")
    textbox.clear()
    textbox.send_keys("5")
    textbox.submit()

    # Find the value in the next textbox to test
    result = self.driver.find_element_by_name("result").get_attribute("value")
    self.assertEqual(int(result.strip()), 10)


  def tearDown(self):
    #close the browser window
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()