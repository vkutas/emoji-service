"""Application Unit tests"""

import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src import app as tested_app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_welcome_endpoint(self):
        r = self.app.get('/welcome')
        self.assertTrue("Welcome to Enterprise Emoji Service!" in r.data.decode("utf-8"))

    def test_post_welcome_endpoint(self):
        r = self.app.post('/welcome')
        self.assertEqual(r.status_code, 405)

    def test_get_say_hello_endpoint(self):
        r = self.app.get('/say_hello')
        self.assertEqual(r.data, b"Hello World!")

    def test_post_say_hello_endpoint(self):
        r = self.app.post('/say_hello')
        self.assertEqual(r.status_code, 405)

if __name__ == '__main__':
    unittest.main()
