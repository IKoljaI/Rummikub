class SameRow:
    def __init__(self):

        self.color = "unknown"
        self.row = []

    def addChip(self, chip):
        if len(self.row) == 0:
            self.row.append(chip)
            self.color = chip.color
            return True

        elif 4 > len(self.row) and chip.color is not self.color:
            self.row.append(chip)
            return True

        else:
            print("too many chips or chip is same color")

    def removeChip(self, chip):
        for chips in self.row:
            if chip.color == chips.color and chip.number == chips.number:
                self.row.remove(chips)
                return True
