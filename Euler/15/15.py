def findlength():
    grid = []
    print grid
    
    for i in range(21):
        grid.append([])
        for j in range(21):
            above = 0
            right = 0
            if j > 0:
                above = grid[i][j-1]
            if i > 0:
                right = grid[i-1][j]
            if i == 0 and j == 0:
                above = 1
            grid[i].append(above + right)
    print grid

findlength()
