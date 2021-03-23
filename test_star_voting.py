""" Test code for INST 326 take-home midterm 1. """


from contextlib import contextmanager
from io import StringIO
from pathlib import Path
import sys
import unittest

import star_voting as sv


testdata1 = """C1:2,C2:4,C3:4,C4:2
C1:2,C2:2,C3:1,C4:2
C1:4,C2:1,C3:0,C4:2
C1:4,C2:1,C3:2,C4:1
C1:2,C2:1,C3:2,C4:3
C1:2,C2:1,C3:1,C4:3
C1:3,C2:1,C3:2,C4:3
C1:1,C2:4,C3:4,C4:2
"""
winner1 = "C4"

testdata2 = """C1:2,C2:2,C3:3,C4:4
C1:2,C2:3,C3:2,C4:4
C1:1,C2:2,C3:1,C4:5
C1:2,C2:1,C3:1,C4:5
C1:2,C2:1,C3:1,C4:4
C1:1,C2:2,C3:2,C4:2
C1:4,C2:3,C3:3,C4:1
C1:4,C2:2,C3:2,C4:3
"""
winner2 = "C4"

testdata3 = """C1:2,C2:4,C3:2,C4:3
C1:2,C2:3,C3:0,C4:2
C1:4,C2:1,C3:4,C4:2
C1:3,C2:1,C3:3,C4:0
C1:1,C2:2,C3:1,C4:1
C1:3,C2:4,C3:0,C4:3
C1:3,C2:3,C3:1,C4:3
C1:2,C2:2,C3:5,C4:2
"""
winner3 = "C2"


class TestBallot(unittest.TestCase):
    """ Test the Ballot class, its methods __init__, parse_votes, and
    preference, and its attribute votes.
    """
    def test_ballot_class(self):
        self.longMessage = False
        if not hasattr(sv, 'Ballot'):
            self.fail("Ballot class is not defined")
        b = sv.Ballot('C1:3,C2:4,C3:1,C4:2,C5:3')
        self.assertTrue(hasattr(b, 'votes'), "Ballot has no votes attribute"
                        " after initialization")
        self.assertEqual(b.votes, {'C1': 3, 'C2': 4, 'C3': 1, 'C4': 2, 'C5': 3},
                         "votes attribute has incorrect value after __init__()")
        v = b.votes.copy()
        d = b.parse_votes('C1:5,C2:1')
        self.assertEqual(d, {'C1': 5, 'C2': 1}, "unexpected result from"
                         " Ballot.parse_votes()")
        self.assertEqual(v, b.votes, "Ballot.parse_votes() should not alter"
                            " the votes attribute")
        self.assertEqual(b.preference('C1', 'C4'), 'C1',
                         "Ballot.preference() returned incorrect result")
        self.assertEqual(b.preference('C2', 'C3'), 'C2',
                         "Ballot.preference() returned incorrect result")
        self.assertIsNone(b.preference('C1', 'C5'),
                          "Ballot.preference() returned incorrect result when"
                          " voter did not express a preference")

class TestFunctions(unittest.TestCase):
    """ Test functions read_ballots, find_winner, and main.
    """
    def setUp(self):
        """ Create a temporary file of ballots to read in.
        """
        self.temp_path = Path("temp_file__ok_to_delete.txt")
        with self.temp_path.open('w', encoding='utf-8') as f:
            f.write(testdata1)

    def tearDown(self):
        """ Try to delete the temporary file.
        """
        try:
            self.temp_path.unlink()
        except Exception:
            pass

    def test_read_ballots(self):
        """ Test the read_ballots function.
        """
        self.longMessage = False
        if not hasattr(sv, 'read_ballots'):
            self.fail("read_ballots() function is not defined")
        ballots = sv.read_ballots(str(self.temp_path))
        self.assertIsInstance(ballots, list,
                              "read_ballots() did not return a list")
        self.assertIsInstance(ballots[0], sv.Ballot,
                              "read_ballots() did not return a list of"
                              " Ballet objects")

        
        self.assertEqual(len(ballots), len(testdata1.splitlines()),
                         "read_ballots() returns wrong number of items")

        self.assertEqual(ballots[0].votes, {'C1':2,'C2':4,'C3':4,'C4':2},
                         "read_ballots() returns Ballot objects with"
                         " incorrect votes")

    def test_find_winner(self):
        """ Test the find_winner function.
        """
        self.longMessage = False
        if not hasattr(sv, 'find_winner'):
            self.fail("find_winner() function is not defined")
        b1 = [sv.Ballot(line) for line in testdata1.splitlines()]
        b2 = [sv.Ballot(line) for line in testdata2.splitlines()]
        b3 = [sv.Ballot(line) for line in testdata3.splitlines()]
        self.assertEqual(sv.find_winner(b1), winner1,
                         "find_winner() identified incorrect winner")
        self.assertEqual(sv.find_winner(b2), winner2,
                         "find_winner() identified incorrect winner")
        self.assertEqual(sv.find_winner(b3), winner3,
                         "find_winner() identified incorrect winner")

    def test_main(self):
        """ Test the main function.
        """
        if not hasattr(sv, 'main'):
            self.fail("main() function is not defined")

        # the following code is based on
        # https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
        @contextmanager
        def captured_output():
            new_out = StringIO()
            old_out = sys.stdout
            try:
                sys.stdout = new_out
                yield sys.stdout
            finally:
                sys.stdout = old_out

        self.longMessage = False
        with captured_output() as out:
            sv.main(str(self.temp_path))
        output = out.getvalue()
        self.assertEqual(output, winner1 + "\n",
                         "main() function does not print the winner"
                         " as specified in the assignment")


if __name__ == '__main__':
    unittest.main()
