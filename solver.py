

def solve(listOfOwnChips,listOfAllRows,chipsToRemove):

    for chip in listOfOwnChips:
        for row in listOfAllRows:
            if row.addChip(chip):
                chipsToRemove.append(chip)
