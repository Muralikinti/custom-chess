WHITE_PIECES = ['♙','♖','♘','♗','♕','♔']
BLACk_PIECES = ['♟','♜','♞','♝','♛','♚']


class ChessVar:
    """
    This class represents an implementation of a simplified chess games which keeps track of the chess board, state of
    the game which can be won by white or black, tie, or unfinished and the turn of the player. It also has various
    methods with different functionality which allow the move system to work within the rules of our version of chess.
    """

    def __init__(self):


        # Creating the empty board.
        self._board = [
            ['-'] * 8 for _ in range(8)
        ]

        # Setting up the piece in the chessboard.
        
        """
        self._board[6][0] = '♙'
        self._board[6][1] = '♙'
        self._board[6][2] = '♙'
        self._board[6][3] = '♙'
        self._board[6][4] = '♙'
        self._board[6][5] = '♙'
        self._board[6][6] = '♙'
        self._board[6][7] = '♙'
        """

        self._board[7][0] = '♖'
        self._board[7][1] = '♘'
        self._board[7][2] = '♗'
        self._board[7][3] = '♕'
        self._board[7][4] = '♔'
        self._board[7][5] = '♗'
        self._board[7][6] = '♘'
        self._board[7][7] = '♖'


        
        """
        self._board[1][0] = '♟'
        self._board[1][1] = '♟'
        self._board[1][2] = '♟'
        self._board[1][3] = '♟'
        self._board[1][4] = '♟'
        self._board[1][5] = '♟'
        self._board[1][6] = '♟'
        self._board[1][7] = '♟'
        """

        self._board[0][0] = '♜'
        self._board[0][1] = '♞'
        self._board[0][2] = '♝'
        self._board[0][3] = '♛'
        self._board[0][4] = '♚'
        self._board[0][5] = '♝'
        self._board[0][6] = '♞'
        self._board[0][7] = '♜'

        self._turn = 'white'
        self._game_state = 'UNFINISHED'

    def get_game_state(self):
        """
        Returns the current state of the game.
        :return: The game state: 'UNFINISHED' or 'WHITE_WON' or 'BLACK_WON' or 'TIE'
        """
        return self._game_state

    def make_move(self, from_square, to_square):
        """
        Helps the users make a move on the chessboard.
        :param from_square: The starting square of the move. E.g. - 'e5'
        :param to_square: The ending square of the move.
        :return: True if the move was successful, False otherwise.
        """

        # Checking if the game has already been won.
        if self._game_state != 'UNFINISHED':
            return False

        if not from_square or not to_square:
            print("Both starting square and ending square must be provided.")
            return False

        if to_square.lower() == 'u':
            print("Move undone.")
            return False

        # Converting the given squares into row and column indices.
        from_col, from_row = ord(from_square[0]) - ord('a'), 8 - (int(from_square[1]))
        to_col, to_row = ord(to_square[0]) - ord('a'), 8 - (int(to_square[1]))

        if (
                # Checking for validity of squares entered.
                not self.is_valid_square(from_row, from_col) or
                not self.is_valid_square(to_row, to_col) or

                # Checking if the from_square contains a piece to be moved.
                self._board[from_row][from_col] == '-' or

                # Checking if the piece being moved is the player's piece.
                (self._board[from_row][from_col] in WHITE_PIECES) != (self._turn == 'white')
        ):
            return False

        # Checking the legality of the move made.
        if not self.is_legal_move(from_row, from_col, to_row, to_col):
            print("ha")
            return False

        # Performing the move on the board.
        captured_piece = self._board[to_row][to_col]
        self._board[to_row][to_col] = self._board[from_row][from_col]
        self._board[from_row][from_col] = '-'

        # Updating the game state and turn of the user once the move is successful.
        
        # self.update_game_state()
        self._turn = 'black' if self._turn == 'white' else 'white'

        return True

    def is_valid_square(self, row, col):
        """
        Checks if the given square is within the boundaries of a chess board.
        :param row: Row index of the square.
        :param col: Column index of the square.
        :return: True if the row and column indices represent a square within the chess board, false otherwise.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def is_legal_move(self, from_row, from_col, to_row, to_col):
        """
        Checks if an entered move is a legal move according to our version of chess.
        :param from_row: The row index of the starting position.
        :param from_col: The column index of the starting position.
        :param to_row: The row index of the ending position.
        :param to_col: The column index of the ending position.
        :return: True if move is legal, False otherwise.
        """

        # Getting the piece being moved and the row and column attributes of path.
        piece = self._board[from_row][from_col]
        print(piece)
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        target_piece = self._board[to_row][to_col]

        # Checking if the piece being moved is a pawn.
        if piece in ['♙', '♟']:
        # Pawns can only move forward.
            direction = 1 if piece == '♙' else -1
            # Moving forward.
            if from_row + direction == to_row:  
                if from_col == to_col:
                    # The destination must be empty.
                    if target_piece == '-':  
                        return True
                # Moving diagonally.
                elif col_diff == 1:  
                    # Must capture an enemy piece.
                    if target_piece != '-' and (target_piece in WHITE_PIECES) != (piece in WHITE_PIECES):  
                        return True
            # Both the destination and the square in between must be empty.
            elif from_row + 2 * direction == to_row and from_col == to_col:
                if target_piece == '-' and self._board[from_row + direction][from_col] == '-': 
                    return True

                    
        # Checking if the piece being moved is a knight.
        if piece in ['♘', '♞']:
            # Checking if the path aligns with movements of knight.
            if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):

                # Checking if ending position is empty or contains enemy piece.
                if target_piece == '-' or ((target_piece in WHITE_PIECES) != (piece in WHITE_PIECES)):
                    return True

        # Checking if the piece being moved is a rook.
        if piece in ['♖', '♜']:
            # Checking if the path aligns with movements of rook.
            if (from_row == to_row and from_col != to_col) or (from_col == to_col and from_row != to_row):
                # Checking for obstacles along the path.
                if from_row == to_row:  # if the movement is horizontal.
                    step = 1 if from_col < to_col else -1
                    for col in range(from_col + step, to_col, step):
                        if self._board[from_row][col] != '-':
                            return False
                else:  # if the movement is horizontal.
                    step = 1 if from_row < to_row else -1
                    for row in range(from_row + step, to_row, step):
                        if self._board[row][from_col] != '-':
                            return False

                # Checking if ending position is empty or contains enemy piece.
                if target_piece == '-' or (target_piece in WHITE_PIECES) != (piece in WHITE_PIECES):
                    return True

        # Checking if the piece being moved is a bishop or a queen.
        if piece in ['♗', '♝']:
            # Checking if the path aligns with movements of bishops.
            if abs(from_row - to_row) == abs(from_col - to_col):
                # Checking for obstacles along the path.
                row_step = 1 if from_row < to_row else -1
                col_step = 1 if from_col < to_col else -1

                row = from_row + row_step
                col = from_col + col_step

                while row != to_row:
                    if self._board[row][col] != '-':
                        return False
                    row += row_step
                    col += col_step

                # Checking if ending position is empty or contains enemy piece.
                if target_piece == '-' or (target_piece in WHITE_PIECES) != (piece in WHITE_PIECES):
                    return True

        # Checking if the piece being moved is a queen.
        if piece in ['♕', '♛']:
        # Checking if the path aligns with movements of queen.
            if (from_row == to_row and from_col != to_col) or (from_col == to_col and from_row != to_row) or abs(from_row - to_row) == abs(from_col - to_col):
                # Checking for obstacles along the path.
                if from_row == to_row:  # if the movement is horizontal.
                    step = 1 if from_col < to_col else -1
                    for col in range(from_col + step, to_col, step):
                        if self._board[from_row][col] != '-':
                            return False
                elif from_col == to_col:  # if the movement is vertical.
                    step = 1 if from_row < to_row else -1
                    for row in range(from_row + step, to_row, step):
                        if self._board[row][from_col] != '-':
                            return False
                else:  # if the movement is diagonal.
                    row_step = 1 if from_row < to_row else -1
                    col_step = 1 if from_col < to_col else -1

                    row = from_row + row_step
                    col = from_col + col_step

                    while row != to_row:
                        if self._board[row][col] != '-':
                            return False
                        row += row_step
                        col += col_step

            # Checking if ending position is empty or contains enemy piece.
            if target_piece == '-' or (target_piece in WHITE_PIECES) != (piece in WHITE_PIECES):
                return True


        # Checking if the piece being moved is a king.
        if piece in ['♔', '♚']:
            # Checking if from and to positions are same.
            if row_diff + col_diff == 0:
                return False

            # Checking if the path aligns with movements of king.
            if row_diff <= 1 and col_diff <= 1:
                if target_piece == '-' or (target_piece in WHITE_PIECES) != (piece in WHITE_PIECES):
                    return True

        return False

    def update_game_state(self):
        """
        Updates the current state of the game based on the king positions and rules of our version of chess.
        """
        # Initializing king positions.
        self._game_state = 'UNFINISHED'


    def are_kings_in_check(self):
        """
        Checks if either king is in check at the moment.
        :return: True if either of them are in check, False otherwise.
        """
        # Initializing king positions.
        white_king_position = None
        black_king_position = None

        # Finding the positions of both kings.
        for row in range(8):
            for col in range(8):
                if self._board[row][col] == '♚':
                    white_king_position = (row, col)
                elif self._board[row][col] == '♔':
                    black_king_position = (row, col)

        # Checking if either king is under threat.
        for row in range(8):
            for col in range(8):
                piece = self._board[row][col]

                # Considering squares with pieces only.
                if piece == '-':
                    continue
                else:
                    target_color = 'white' if piece.isupper() else 'black'

                    # Checking if the target piece is of the enemy user.
                    if target_color == 'white':

                        # Checking if the current piece can legally move to attack black king's position.
                        if self.is_legal_move(row, col, black_king_position[0], black_king_position[1]):
                            return True
                    else:
                        # Checking if the current piece can legally move to attack white king's position.
                        if self.is_legal_move(row, col, white_king_position[0], white_king_position[1]):
                            return True
        return False

    def print_board(self):
        """
        Prints the current state of the chessboard.
        """
        for row in self._board:
            print(' '.join(row))
        print()

    def play_game(self):
        """
        Allows players to make moves and plays the game until it's finished.
        """
        while self._game_state == 'UNFINISHED':
            self.print_board()
            print(f"It's {self._turn}'s turn.")
            from_square = input("Enter the starting square (e.g., 'e2'): ")
            to_square = input("Enter the ending square (or enter 'u' to enter new starting square): ")

            if self.make_move(from_square, to_square):
                self.update_game_state()
            else:
                print("Invalid move. Try again.")

        self.print_board()
        print("Game over. Result: " + self._game_state)


if __name__ == "__main__":
    game = ChessVar()
    game.play_game()
