test = 1

def soft_assert(a,b):
	result = None
	try:
		assert a == b
		result = "test passed"
	except AssertionError:
		result = "test failed"
	print(result)

soft_assert(test, 0)
