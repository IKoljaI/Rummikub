from SameRow import SameRow
from StreetRow import StreetRow
from chip import Chip


chip1 = Chip(5,"blue",0,0)
chip2 = Chip(5,"red",chip1,0)
chip3 = Chip(3, "green",chip2,0)



print(chip1.next_chip.color)
print(chip2.prev_chip.color)
print(chip3.prev_chip.prev_chip.color)

