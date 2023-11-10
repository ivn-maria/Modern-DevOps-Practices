import unittest
import socket
from src.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 200)
        expected_message = f'Hello! I am a Flask application running on \
{socket.gethostname()}'
        self.assertEqual(response.data.decode('utf-8'), expected_message)


if __name__ == '__main__':
    unittest.main()
