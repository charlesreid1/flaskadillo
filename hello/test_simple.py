from simple import app
import unittest

"""
Simple Flask Server Unit Test

https://docs.python.org/3/library/unittest.html#test-discovery
"""

class TheSimplestTest(unittest.TestCase):
    """
    The simplest unit test for the simplest Flask app
    """
    def test_simple_route(self):
        """
        Test the / route
        """
        # Get a test client
        client = app.test_client()
        
        # Test route /
        r = client.get('/')
        assert b'Hello world!' in r.data
        
        # Test route /foo
        r = client.get('/foo')
        assert b'Hello foo!' in r.data
        
        # Test route /bar/qwerty
        r = client.get('/bar/qwerty')
        assert b'Hello qwerty!' in r.data

