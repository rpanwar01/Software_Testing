import unittest
from yarn.api import env, cd, run 

env.host_string = 'pythonanywhere.com'
env.user = 'rpanwar01'
env.password = 'XXXXXX'

class Test_000_yarn_testing(unittest.TestCase):
	
	def test_000_python3(self):
		pass

if __name__ == "__main__":
    unittest.main()
	