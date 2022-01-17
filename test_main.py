from unittest import TestCase
from chip import Chip
from StreetRow import StreetRow
from SameRow import SameRow
import solver


listOfAllRows = []
listOfOwnChips = []
chipsToRemove = []
originalListOfOwnChips = listOfOwnChips

chip1 = Chip(5, "blue")
chip2 = Chip(6, "blue")
chip3 = Chip(5, "blue")
chip4 = Chip(7, "blue")
chip5 = Chip(8, "blue")
chip6 = Chip(5, "red")

SameRow1 = SameRow()

SameRow1.addChip(chip1)
SameRow1.addChip(chip2)
SameRow1.addChip(chip3)

listOfOwnChips.append(chip4, chip5, chip6)


class TestSolve(TestCase):
    def test_solve(self):
        solver.solve()
        self.assertFalse(len(chipsToRemove) == 0)

    def test_something(self):
        self.assertTrue(1 == 1)
