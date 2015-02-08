game = __import__('2048')
from nose.tools import ok_, eq_

def test_process_move():
	"""Testing process_move"""
	ok_(game.process_move(1)==False, "Invalid move")
	# ok_(game.process_move("a") != False, "Valid move")

def test_len_of_board():
	"""Testing length of board"""
	ok_(len(game.x) == 4, "Length must be 4")

def test_type_of_board_variable():
	"""Testing type of board variable"""
	ok_(isinstance(game.x, list), "Instance of list")

def test_initial_max_value():
	"""Testing initial max value"""
	ok_(game.max_value()==2, 
	    "Initial max value always 2")
