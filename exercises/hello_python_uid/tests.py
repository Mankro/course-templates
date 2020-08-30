import unittest, graderunittest

class TestHelloPython(unittest.TestCase):

    def test_import(self):
        """Import the functions module (1p)"""
        # If this fails, it indicates the file is not a proper Python
        # program.
        import functions

    def test_function(self):
        """Check hello function exists (1p)"""
        # Does the same as test_import, but also check that the module
        # "functions" defines the name "hello" which refers to a function.
        import functions
        def protofunction():
            pass
        self.assertTrue(type(functions.hello), type(protofunction))

    def test_return(self):
        """Check hello function return value (3p)"""
        # Calls the function "hello" and examines its return value.
        import functions
        with open('/submission/uid', 'r') as uid_file:
            uid = uid_file.read().strip()
        correct_retval = "Hello {uid}!".format(uid=uid)
        self.assertEqual(functions.hello(), correct_retval)

if __name__ == '__main__':
    unittest.main(testRunner=graderunittest.PointsTestRunner(verbosity=2))
