def RAY ():
	file = open("grid.txt").readlines()
	
	matrix = []
	
	for line in file :
		matrix.append(line.strip().split())
	
	max = 0

	
	for i, vert in enumerate(matrix):
		for j, horiz in enumerate(vert):
			if i < 17 and j < 17:
				diag = int(matrix[i][j]) * int(matrix[i+1][j+1]) * int(matrix[i+2][j+2]) * int(matrix[i+3][j+3])
				if diag > max:
					max = diag
			if i < 17:
				diag = int(matrix[i][j]) * int(matrix[i+1][j]) * int(matrix[i+2][j]) * int(matrix[i+3][j])
				if diag > max:
					max = diag
			if j < 17:
				diag = int(matrix[i][j]) * int(matrix[i][j+1]) * int(matrix[i][j+2]) * int(matrix[i][j+3])
				if diag > max:
					max = diag	
			if i < 17 and j > 2:
				diag = int(matrix[i][j]) * int(matrix[i+1][j-1]) * int(matrix[i+2][j-2]) * int(matrix[i+3][j-3])
				if diag > max:
					max = diag	
	print max
			
			

RAY()
	