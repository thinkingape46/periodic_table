# This is a simple guess game, player has to guess the name of the element when a number is displayed.

from random import randint

element_name = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium']
element_num = range(1, 110)

element_dict = {num: name for name, num in zip(element_name,element_num)}
element_dict_rev = {name: num for name, num in zip(element_name,element_num)}

print(element_dict)

class GuessElement():

    def __init__(self, chem_num = 1):

        self.chem_num = chem_num

        pass

    def guess_element(self):

        '''This method display the atomic number and asks for the name of the element'''

        while True:

            rand_num = randint(1, 10)
            playerguess = input(f"Guess the name of the element with the atomic number {rand_num}: ")
            
            if playerguess.upper() == element_dict[rand_num].upper():
                print("You are right!")

            else:
                print("Incorrect!")
                print(f"Right answer is {element_dict[rand_num]}")
                continue


guesselement1 = GuessElement()
guesselement1.guess_element()





