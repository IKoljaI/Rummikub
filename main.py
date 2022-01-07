from SameRow import SameRow
from StreetRow import StreetRow
from chip import Chip
from StreetRow import StreetRow
from SameRow import SameRow

listOfAllRows = []
listOfOwnChips = []

chip1 = Chip(5,"blue")
chip2 = Chip(5,"red")
chip3 = Chip(3, "green")


listOfOwnChips.append(chip1)
listOfOwnChips.append(chip2)

#if type(listOfOwnChips[0]) == Chip: TODO so kannst du die Klasse vom objekt checken obs ne Street oder Same ist zb
#    print("yea its a chip")

print(listOfOwnChips[0].color)
print(listOfOwnChips[1].color)

list =[chip1,chip2]

list.remove(chip1)

for chips in list:
    print(chips.color)



print(" NEWWWw")





