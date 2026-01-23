import unittest
from app import app


class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def unit_test_example(self):
        tester = app.test_client(self)
        response = tester.get("/unit-test-example")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Unit Test Example", response.data)

    def control_endpoint_test(self):
        tester = app.test_client(self)
        response = tester.get("/control-endpoint")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Control Endpoint", response.data)


if __name__ == "__main__":
    unittest.main()
