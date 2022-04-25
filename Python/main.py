import collections

class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = {}
        nextGeneration = set()

        for r, c in live: # for each live cell coordinate 
            for I in range(r-1, r+2): # check neighbouring rows from the top left
                 for J in range(c-1, c+2): # check neighbouring columns to the bottom right of the 9 cell matrix
                     if I!=r or J != c: # as we are dealing with an infinite board space, we ignore checking for bounds and only check if the neighbouring cell is not the same cell we are observing
                        ctr[(I,J)] = ctr.get((I,J),0) + 1

        print(ctr)


        for ij in ctr:
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live:
                nextGeneration.add(ij)

        print(nextGeneration)

        # maxRow = max(nextGeneration, key = lambda x:x[0])[0] # processing the maximum bounds of the array to render board
        # maxCol = max(nextGeneration, key = lambda x:x[1])[1] 
        # board = [[0 for _ in range(maxCol+1)] for _ in range(maxRow+1)]


        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if (r,c) in nextGeneration:
        #             board[r][c] = 1
        
        # print(board)


        # ctr = collections.Counter((I, J) for i, j in live for I in range(i-1, i+2) for J in range(j-1, j+2) if I != i or J != j)



    def gameOfLife(self, liveCells):
        liveCells = board
        liveCells = self.gameOfLifeInfinite(liveCells)
        
        return liveCells

# board = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (-2000000000000, -2000000000000), (-2000000000001, -2000000000001),(-2000000000002, -2000000000002)}
# board = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2000000000000, 2000000000000), (2000000000001, 2000000000001),(2000000000002, 2000000000002)}
board = {(0, 1), (1, 2), (2, 1), (2, 0), (2, 2)} 

sol = Solution()
print(sol.gameOfLife(board))

