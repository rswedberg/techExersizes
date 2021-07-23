import unittest
from flask import current_app
from app import app, create_app

class SampleTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app()
    self.app_context = self.app.test_request_context()
    self.app_context.push()
    self.client = self.app.test_client(use_cookies=True)

  def test_value(self):
    tester = app.test_client(self)
    response = tester.post("/", data={
      'number': '5',
    }, follow_redirects=True)
    self.assertTrue(b'10' in response.data)

  def test_app_exists(self):
    self.assertFalse(current_app is None)

  def tearDown(self):
    self.app_context.pop()

if __name__ == "__main__":
    unittest.main()
