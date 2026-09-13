#!/usr/bin/env python3

import unittest

from src.sudoku_block import block_correct


SUDOKU = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
]

# A second grid used to exercise both valid and invalid 3x3 blocks. Block
# top-left corners are given as (row_no, column_no), both multiples of 3.
CHECK_SUDOKU = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 1, 0, 0, 8, 0, 0, 2],
]


class TestBlockCorrect(unittest.TestCase):

    def test_worked_example(self):
        result = block_correct(SUDOKU, 0, 0)
        self.assertIsInstance(
            result, bool,
            msg="block_correct(sudoku, 0, 0) should return a bool, not %s. "
                "Got %r." % (type(result).__name__, result))

    def test_valid_blocks(self):
        for row, col in [(0, 3), (0, 6), (3, 0), (3, 3), (6, 6)]:
            with self.subTest(row=row, column=col):
                result = block_correct(CHECK_SUDOKU, row, col)
                self.assertEqual(
                    result, True,
                    msg="block_correct(sudoku, %d, %d) should be True: the "
                        "3x3 block starting at row %d, column %d has no "
                        "repeated nonzero digit." % (row, col, row, col))

    def test_invalid_blocks(self):
        for row, col in [(0, 0), (3, 6), (6, 3), (6, 0)]:
            with self.subTest(row=row, column=col):
                result = block_correct(CHECK_SUDOKU, row, col)
                self.assertEqual(
                    result, False,
                    msg="block_correct(sudoku, %d, %d) should be False: "
                        "the 3x3 block starting at row %d, column %d has a "
                        "repeated nonzero digit." % (row, col, row, col))

    def test_block_of_all_zeros_is_valid(self):
        blank_sudoku = [[0] * 9 for _ in range(9)]
        result = block_correct(blank_sudoku, 3, 3)
        self.assertEqual(
            result, True,
            msg="block_correct(sudoku, 3, 3) should be True when that 3x3 "
                "block is all zeros: an empty block has no repeated "
                "nonzero digit.")


if __name__ == "__main__":
    unittest.main()
