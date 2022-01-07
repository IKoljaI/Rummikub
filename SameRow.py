class SameRow:
    def __init__(self):
        color = "unknown"
        row = []

    def addChip(self, chip):
        if len(self.row) == 0:
            self.row.append(chip)
            self.color = chip.color

        if len(self.row) < 4 and chip.color == self.color:
             self.row.append(chip)

        else:
            print("too many chips or chip is wrong color")

    def removeChip(self,chip):
        for chips in self.row:
            if chip.color == chips.color and chip.number == chips.number:
                self.row.remove(chips)
