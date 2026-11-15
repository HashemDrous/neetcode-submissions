class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        (list) -> bool
        Arranges the
        '''
        # get list for row, column, and box, if all: true else false
        # Row:
        for row in board:
            if self.is_group_true(row) == False:
                return False
        
        # Column:
        for j in range(len(board[0])):
            column = []
            for i in range(len(board)):
                column.append(board[i][j])
            if self.is_group_true(column) == False:
                return False
        
        # 3x3
        for k in range(0, 9, 3):
            for j in range(0,9,3): # 0 3 6. 3, :3 + 4, :3 + 5, :3
                box = [] # [[1,2,3], [1,2,3], [1,2,3]]
                for i in range(j, j + 3): # range(0, 3)
                    box.append(board[i][k:k + 3]) 
                
                new_d = []
                for nested in box:
                    for num in nested:
                        new_d.append(num)
                if self.is_group_true(new_d) == False:
                    return False

        return True
                

    def is_group_true(self, nums):
        ''' 
        (list) -> bool
        returns true if a given list has no duplicates
        '''
        counter = dict.fromkeys(nums, 0) 

        for num in nums:
            counter[num] += 1
        for k in counter:
            if counter[k] > 1 and k != '.':
                return False

        return True
            
    
