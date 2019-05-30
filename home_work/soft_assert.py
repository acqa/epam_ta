test = 1

def soft_assert(a,b):
	result = None
	try:
		assert a == b
		result = "test passed"
	except AssertionError:
		result = "test failed, but has been resumed"
	print(result)

soft_assert(test, 0)
