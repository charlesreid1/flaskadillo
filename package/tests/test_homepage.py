from simple.webapp import app
import unittest

class TheSimplestFlaskTest(unittest.TestCase):
    def test_simple_flask_package(self):
        client = app.test_client()

        r = client.get('/')
        assert b'Hello world!' in r.data

        r = client.get('/florence')
        assert b'Hello florence!' in r.data

