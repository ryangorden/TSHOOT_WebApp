import sys
from unittest import TestCase


sys.path.append("/src")
from app import app


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp= c.get('/')

#            self.assertEqual(resp.text, {"home": "Hello Networkers"})
            self.assertEqual(resp.status_code, 200)
