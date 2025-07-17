import unittest
import sys
import os

from backend.app import app

class BasicFlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Uygulama Calisiyor!', response.data)

    def test_api_control_route(self):
        response = self.app.get('/api/v1/users/control')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'data': 1500})

if __name__ == '__main__':
    unittest.main()