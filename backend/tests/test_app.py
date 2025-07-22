import unittest
from backend.app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
<<<<<<< HEAD
        self.assertEqual(response.status_code, 404) 
=======
        print('test merge deneme icin eklendi')
        self.assertEqual(response.status_code, 200) 
>>>>>>> test

if __name__ == '__main__':
    unittest.main()
