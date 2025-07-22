import unittest
from backend.app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200) 

        print('test merge deneme icin eklendi')

def nothing(x):
    pass

if __name__ == '__main__':
    unittest.main()

