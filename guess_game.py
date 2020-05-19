# This is a simple guess game, player has to guess the name of the element when a number is displayed.

from random import randint

element_name = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium']
element_num = range(1, 110)

element_dict = {num: name for name, num in zip(element_name,element_num)}
element_dict_rev = {name: num for name, num in zip(element_name,element_num)}

print("\nGUESS THE NAME OF THE ELEMENT!\n")

class GuessElement():

    def __init__(self, chem_num = 1):

        self.chem_num = chem_num

        pass

    def guess_element(self, score = 10):
        
        '''This method display the atomic number and asks for the name of the element'''

        self.score = score

        n = 1

        while score >= 0:

            rand_num = randint(1, 109)
            playerguess = input(f"Guess the name of the element with the atomic number {rand_num}: ")
            
            if playerguess.upper() == element_dict[rand_num].upper():

                score = score + 10
                print("You are right!")
                print(f"Score: {score}")

                n += 1

            else:

                score = score - 1
                print(f"Incorrect! It's {element_dict[rand_num]}")
                print(f"Score: {score}")
                
                continue


guesselement1 = GuessElement()
guesselement1.guess_element()





