
# The test file for pentago_board.py

import unittest

from game_objects.pentago_board import PentagoBoard

class TestPentagoBoard(unittest.TestCase):

    def __init__(self, methodName: str = "TestPentagoBoard") -> None:
        super().__init__(methodName)

        self.pentagoBoardNew = PentagoBoard()
        self.pentagoBoard0 = PentagoBoard([
                                            [0,1,2,1,1,0],
                                            [2,1,0,2,1,0],
                                            [0,2,1,1,1,0],
                                            [0,0,0,1,2,1],
                                            [1,1,1,2,2,2],
                                            [2,1,0,0,0,1],
                                            ])
    
    def test_init_default(self):
        
        self.assertEqual(self.pentagoBoardNew.board, [[0,0,0,0,0,0],
                                                      [0,0,0,0,0,0],
                                                      [0,0,0,0,0,0],
                                                      [0,0,0,0,0,0],
                                                      [0,0,0,0,0,0],
                                                      [0,0,0,0,0,0]])
        self.assertNotEqual(self.pentagoBoardNew.board, [])
    
    def test_init(self):
        pass
    
    def test_str(self):
        pass

    def test_hash(self):
        pass

    def test_eq(self):
        pass

    def test_lt(self):
        pass

    def test_gt(self):
        pass

    def test_ge(self):
        pass

    def test_le(self):
        pass

    def test_check_win(self):
        pass

    def test_check_draw(self):
        pass

    def test_copy(self):
        pass

    def test_make_move(self):
        pass

    def test_linearize(self):
        self.assertEqual(
        [0,1,2,1,1,0,2,1,0,2,1,0,
        0,2,1,1,1,0,0,0,0,1,2,1,1,
        1,1,2,2,2,2,1,0,0,0,1],
        self.pentagoBoard0.linearize())