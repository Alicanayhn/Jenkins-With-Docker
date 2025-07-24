import unittest
from app import app 

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_home_status_code(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.tester.get('/')
        print('Uygulama Calisiyor')
        self.assertEqual(response.data.decode("utf-8"), "Uygulama Calisiyor!")

    def test_api_control_status_code(self):
        response = self.tester.get('/api/v1/users/control')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
