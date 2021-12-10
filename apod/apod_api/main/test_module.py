import sys

def test(did_pass):
	line_num = sys._getframe(1).f_lineno
	if did_pass:
		return f'Test at line {line_num} is OK.'
	else: return f'Test at line {line_num} has FAILED.'
