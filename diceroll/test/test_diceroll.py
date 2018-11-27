import unittest

from diceroll import random

class TestDiceRoll(unittest.Testcase):	
	def test_random(self):
		assert diceroll.run() == range(1,6)
		
if __name__ == '__main__':
	unittest.main()