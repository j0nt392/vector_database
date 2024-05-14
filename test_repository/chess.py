class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "white"

    def create_board(self):
        # Create and initialize the chess board
        board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                 ["P", "P", "P", "P", "P", "P", "P", "P"],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 ["p", "p", "p", "p", "p", "p", "p", "p"],
                 ["r", "n", "b", "q", "k", "b", "n", "r"]]
        return board

    def print_board(self):
        # Print the current state of the chess board
        for row in self.board:
            print(" ".join(row))

    def play(self):
        # Main game loop
        while True:
            self.print_board()
            # TODO: Implement game logic here
            break

if __name__ == "__main__":
    game = ChessGame()
    game.play()