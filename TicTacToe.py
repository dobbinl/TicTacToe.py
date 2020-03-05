class TicTacToe():

    def __init__(self):
        self.__board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.__current_state = 'UNFINISHED'

    def get_current_state(self):
        """ Evaluate current values in lists. """
        return self.__current_state

    def make_move(self, r, c, val):
        """ check to see if the game is finished """
        if self.__current_state != 'UNFINISHED':
            return False
        # check if row is out of bounds
        if r not in (0, 1, 2):
            return False
        # check if column is out of bounds
        if c not in (0, 1, 2):
            return False
        # check to see if the square is already occupied
        if self.__board[r][c] != '':
            return False
        # record the move
        self.__board[r][c] = val
        # update the state
        self.__update_state()
        # return true
        return True

    def __update_state(self):
        # check if X won
        # check the rows
        for r in (0, 1, 2):
            count = 0
            for c in (0, 1, 2):
                if self.__board[r][c] == 'x':
                    count += 1
            if count == 3:
                self.__current_state = 'X_WON'
                return
        # check the columns
        for c in (0, 1, 2):
            count = 0
            for r in (0, 1, 2):
                if self.__board[r][c] == 'x':
                    count += 1
            if count == 3:
                self.__current_state = 'X_WON'
                return
        # check the diagonal
        if (self.__board[0][0], self.__board[1][1], self.__board[2][2]) == ('x', 'x', 'x'):
            self.__current_state = 'X_WON'
            return
        if (self.__board[0][2], self.__board[1][1], self.__board[2][0]) == ('x', 'x', 'x'):
            self.__current_state = 'X_WON'
            return
        
        # check the rows
        for r in (0, 1, 2):
            count = 0
            for c in (0, 1, 2):
                if self.__board[r][c] == 'o':
                    count += 1
            if count == 3:
                self.__current_state = 'O_WON'
                return
        # check the columns
        for c in (0, 1, 2):
            count = 0
            for r in (0, 1, 2):
                if self.__board[r][c] == 'o':
                    count += 1
            if count == 3:
                self.__current_state = 'O_WON'
                return
        # check the diagonal
        if (self.__board[0][0], self.__board[1][1], self.__board[2][2]) == ('o', 'o', 'o'):
            self.__current_state = 'O_WON'
            return
        if (self.__board[0][2], self.__board[1][1], self.__board[2][0]) == ('o', 'o', 'o'):
            self.__current_state = 'O_WON'
            return
        # check for a draw
        for r in (0, 1, 2):
            for c in (0, 1, 2):
                if self.__board[r][c] == '':
                    return
        self.__current_state = 'DRAW'

    def display(self):
        """ Prints out current board. """
        print()
        for r in (0, 1, 2):
            print(self.__board[r])
        print()