import unittest
from app import app

class TestMainPage(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'<p>Hello, World!</p>')  #b'' converts string to binary 

    def test_register(self):
        rv = self.app.get('/register')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'<p>Fail</p>')

if __name__ == '__main__':
    unittest.main()
