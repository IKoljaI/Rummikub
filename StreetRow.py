class StreetRow:
    def __init__(self):
        self.color = "unknown"
        self.row = []

    def addChip(self,chip):

        if len(self.row) == 0:
            self.row.append(chip)
            self.color = chip.color
            return True
        elif chip.color == self.color and (self.row[0].number > chip.number or chip.number > self.row[len(self.row)-1].number):
                                                                        ##ja funktioniert nur chips mit gleicher farbe und zahl kommen rein

            self.row.append(chip)
            self.row.sort(key=lambda x: x.number, reverse=False) ##https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
            return True
        else:
            return False
        #for chip in self.row:  #TEST
        #    print(chip.number)


    # def insert_chip(self, chip):
    #
    #     # TODO Straße voll??? kann man hinten anlegen?

    #     if chip.color == self.color and (chip.number == self.first_chip.number +1 or self.first_chip.number -1):
    #         print("chip valid")
    #     else:
    #         print("chip not valid, wrong color or number")


  ### TESTss



