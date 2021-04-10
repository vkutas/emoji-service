import unittest
from src.app import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_welcome_endpoint(self):
        r = self.app.get('/welcome')
        self.assertEqual(r.data, "<h1 style='color:#323232'>Welcome to Enterprise Emoji Service!</h1>'")

    def test_post_welcome_endpoint(self):
        r = self.app.post('/welcome')
        self.assertEqual(r.status_code, 405)

    def test_get_say_hello_endpoint(self):
        r = self.app.get('/say_hello')
        self.assertEqual(r.data, "Hello World!")

    def test_post_say_hello_endpoint(self):
        r = self.app.post('/say_hello')
        self.assertEqual(r.status_code, 405)
    
if __name__ == '__main__':
    unittest.main()