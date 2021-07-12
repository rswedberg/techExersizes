import unittest
from flask import current_app
from app import create_app

class SampleTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    self.app_context.pop()

  def test_value(self):
    response - self.client.post(url_for('index'), data={
      'number': '5',
    }, follow_redirects=True)
    self.assertTrue('10' in double.data)

  def test_app_exists(self):
    self.assertFalse(current_app is None)

  def test_app_is_testing(self):
    self.assertTrue(current_app.config['TESTING'])