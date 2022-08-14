
from game_objects.move import Move

class PentagoBoard:
    
    #----- Constructor -----
    def __init__(self, old_board = None) -> None:

        # represents the board by a 6x6 array.
        # 0 is a blank space, 1 is a position held by player 1, 2 is a position
        # held by player 2

        # default constructor for new game
        if old_board == None:
            self.board = [[0] * 6] * 6

        # if an old board is passed in... (assuming it is a 6x6 array of ints)
        elif type(old_board) == list:
            self.board = old_board
        
        elif type(old_board) == int:
            #TODO hash is passed in
            pass

        else:
            raise TypeError(f"The type {type(old_board)} not supported in constructor.")
    
    # ----- Dunder Methods -----
    def __str__(self) -> str:
        DIM = 6
        out = ""
        for row in range(DIM):
            if row == DIM // 2:
                out += "\n"
            for col in range(DIM):
                if col == DIM // 2:
                    out += " "
                out += str(self.board[row][col])
            out += "\n"
        return out.strip()

    def __repr__(self) -> str:
        return str(self)
    
    # hash is a one-to-one method. Every board yeilds a unique hash
    # and every hash represents a unique board.
    def __hash__(self) -> int:
        #TODO hashcode 
        pass

    def __eq__(self, other : object) -> bool:
        #TODO equal to
        pass

    def __lt__(self, other : object) -> bool:
        #TODO less than
        pass

    def __gt__(self, other : object) -> bool:
        return not (self < other ) and not (self == other)

    def __ge__(self, other : object) -> bool:
        return self == other or self > other

    def __le__(self, other : object) -> bool:
        return self == other or self < other
    
    # ----- Game decision-making methods -----
    def check_win(self, player_num : int) -> bool:
        #TODO check win
        pass

    def check_draw(self) -> bool:
        #TODO check draw 
        pass

    # ----- "Immutable" transformation methods -----
    # Note: all return a new instance of PentagoBoard

    def copy(self):
        return PentagoBoard(old_board = [move_array.copy() for move_array in self.board])

    def make_move(self, move : Move):
        #TODO make move -> PentaoBoard
        pass

    # ----- Useful public methods for other usages -----
    def linearize(self) -> list[int]:
        ret = []
        for row in self.board:
            for col in row:
                ret.append(col)
        return ret

    # ----- Helper "private" methods -----

# prod() is new-ish as of python 3.8, don't make the user get a new version
# of python just for this one function
try:
    from math import prod
except ImportError as ex:
    from functools import reduce
    def prod(arr : list[int]) -> int:
        return reduce(lambda x, y : x * y, arr)