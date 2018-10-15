from flyapi import app
import unittest

"""
Simple Flask API Server Unit Test

https://docs.python.org/3/library/unittest.html#test-discovery
"""

class TheAPITest(unittest.TestCase):
    """
    The simplest unit test for the simplest Flask app
    """
    def test_api_out(self):
        """
        Test getting JSON out from an API
        """
        client = app.test_client()
        r = client.get('/example/api/endpoint')
        assert r.status_code==200


    def test_api_in(self):
        """
        Test getting JSON in from an API
        """
        client = app.test_client()
        data = {
                'color':'red'
        }
        r = client.post('/example/api/receiver', data=data)
        assert r.status_code==200

