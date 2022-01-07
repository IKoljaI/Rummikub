class StreetRow:
    def __init__(self, first_chip):
        self.first_chip = first_chip
        self.chip_count = 1
        self.color = self.first_chip.color

    def insert_chip(self, chip):

        # TODO check if chip is valid wellllllllllll again what if its not the second chip?
        # TODO maybe do this with a list after all
        if chip.color == self.color and (chip.number == self.first_chip.number +1 or self.first_chip.number -1):
            print("chip valid")
        else:
            print("chip not valid, wrong color or number")


  ### TEST



