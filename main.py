import numpy as np

from lib.np_debug import np_debug


if __name__ == '__main__':
	a = np.array([
		[
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12]
		],
		[
			[13, 14, 15, 16],
			[17, 18, 19, 20],
			[21, 22, 23, 24]
		]
	])
	b = np.zeros((2,3,1))

	np_debug()

	print('after debug')