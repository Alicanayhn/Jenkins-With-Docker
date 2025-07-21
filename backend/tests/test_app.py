import unittest
from app import app # varsayalım ki app.py'de Flask app tanımlı

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 404)  # ← hata vermesi için yanlış status

if __name__ == '__main__':
    unittest.main()
