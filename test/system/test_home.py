import sys
from unittest import TestCase

sys.path.append("/home/riyan678/TSHOOT_WebApp_docker/src")
from app import app


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp= c.get('/')

#            self.assertEqual(resp.text, {"home": "Hello Networkers"})
            self.assertEqual(resp.status_code, 200)
