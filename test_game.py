game = __import__('2048')
from nose.tools import ok_, eq_

def test_process_move():
	"""Testing process_move"""
	ok_(game.process_move(1)==False)
	ok_(game.process_move("a"))
