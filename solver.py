from main import listOfOwnChips
from main import listOfAllRows
from main import chipsToRemove
import solver

def solve():

    for chip in listOfOwnChips:
        for row in listOfAllRows:
            if row.addChip(chip):
                chipsToRemove.append(chip)
