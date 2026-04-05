class Solution:
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        y=9
        x=9
        map_list_rows=[{} for _ in range(9)]
        map_list_cols=[{} for _ in range(9)]
        map_list_squares=[{} for _ in range(9)]
        for i in range(y):
            for ii in range(x):
                if board[i][ii]!='.':
                    if board[i][ii] not in map_list_rows[i]:
                        map_list_rows[i][board[i][ii]]=1
                    else:
                        return False
                    if board[i][ii] not in map_list_cols[ii]:
                        map_list_cols[ii][board[i][ii]]=1
                    else:
                        return False
                    if board[i][ii] not in map_list_squares[(ii//3)+3*(i//3)]:
                        map_list_squares[(ii//3)+3*(i//3)][board[i][ii]]=1
                    else:
                        return False
                    # if !valid(ii,i,board[y][x]):
                    #     return False
        print(map_list_rows)
        print(map_list_cols)
        print(map_list_squares)
        return True

# def valid(x: int, y: int, val) -> bool:
#     if 