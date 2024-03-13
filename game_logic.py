class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Represents the 3x3 game board
        self.current_winner = None  # Tracks the winner of the game

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, player):
        if self.board[square] == ' ':
            self.board[square] = player
            if self.check_winner(square, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, square, player):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == player for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == player for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right
            if all([spot == player for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left
            if all([spot == player for spot in diagonal2]):
                return True
        return False

    def game_over(self):
        return self.current_winner is not None or ' ' not in self.board
