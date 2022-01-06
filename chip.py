class Chip:
    def __init__(self, number, color, prev_chip, next_chip):
        self.prev_chip = prev_chip
        # TODO maybe you dont need linked chips since you put them in a list anyways
        try:
            self.prev_chip.next_chip = self
        except:
            print("no prev Chip found")
        self.next_chip = next_chip
        try:
            self.next_chip.prev_chip = self
        except:
            print("no next Chip found")

        self.color = color
        self.number = number

        ##test
