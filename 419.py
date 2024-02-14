class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i:
                        if board[i - 1][j] == 'X':
                            continue
                    if j:
                        if board[i][j - 1] == 'X':
                            continue
                    res += 1

        return res


if __name__ == '__main__':
    b = [["X", ".", "X", ".", "X"], [".", "X", ".", "X", "."]]
    s = Solution()
    print(s.countBattleships(b))
