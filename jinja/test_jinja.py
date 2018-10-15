from jinja_app import app
import unittest

"""
Flask + Jinja Templates Unit Test

https://docs.python.org/3/library/unittest.html#test-discovery
"""

class TheJinjaTest(unittest.TestCase):
    """
    Simple unit test for Flask + Jinja templates
    """
    def test_jinja(self):
        """
        Test getting JSON out from an API
        """
        client = app.test_client()
        r = client.get('/')
        assert r.status_code==200


