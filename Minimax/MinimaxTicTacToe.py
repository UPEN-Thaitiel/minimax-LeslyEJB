# number of rows and number of columns
BOARD_SIZE = 3
# this is the reward of winning a game
REWARD = 10


class TicTacToe:

    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Computer starts...")

        while True:
            self.move_computer()
            self.move_player()

    def print_board(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print("Can't insert there!")
            self.move_player()

    def check_game_state(self):
        self.print_board()

        if self.is_draw():
            print("Draw!")
            exit()

        if self.is_winning(self.player):
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()

    def is_winning(self, player):
        # Diagonals
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True

        # Rows and columns
        for i in range(BOARD_SIZE):
            if self.board[3*i+1] == player and self.board[3*i+2] == player and self.board[3*i+3] == player:
                return True
            if self.board[i+1] == player and self.board[i+4] == player and self.board[i+7] == player:
                return True

        return False

    def is_draw(self):
        return all(self.board[key] != ' ' for key in self.board)

    def move_player(self):
        position = int(input("Enter the position for 'O':  "))
        self.update_player_position(self.player, position)

    def move_computer(self):
        best_score = -float('inf')
        best_move = 0

        for position in self.board:
            if self.board[position] == ' ':
                self.board[position] = self.computer
                score = self.minimax(0, False)  # Simple minimax
                self.board[position] = ' '
                if score > best_score:
                    best_score = score
                    best_move = position

        self.board[best_move] = self.computer
        self.check_game_state()

    def minimax(self, depth, is_maximizer):
        if self.is_winning(self.computer):
            return REWARD - depth
        elif self.is_winning(self.player):
            return -REWARD + depth
        elif self.is_draw():
            return 0

        if is_maximizer:
            best_score = -float('inf')
            for position in self.board:
                if self.board[position] == ' ':
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, False)
                    self.board[position] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for position in self.board:
                if self.board[position] == ' ':
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[position] = ' '
                    best_score = min(best_score, score)
            return best_score


if __name__ == '__main__':
    board = {i: ' ' for i in range(1, 10)}
    game = TicTacToe(board)
    game.run()
