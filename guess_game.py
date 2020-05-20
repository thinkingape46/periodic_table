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
        
        print("1. Practice\n2. Quiz")
        try:
            select_game = int(input("Choose what you like to do (1 or 2): "))
        except ValueError:
            print("Please enter either 1 or 2")
        if select_game not in (1, 2):
            print("Please enter either 1 or 2")
        
        while select_game == 1:

            print("\nSelect the range of atomic numbers: ")
            
            try:
                z1 = int(input("Enter the start of range for practice: "))
            except ValueError:
                print("Please enter a number between 1 and 108")
            if z1 not in list(range(1, 109)):
                print("Please enter a number between 1 and 108")            
            
            try:
                z2 = int(input("Enter the end of range for practice (last element: 109): "))
            except ValueError:
                print("Please enter a number between 2 and 109")
            if z2 not in list(range(2, 110)):
                print("Please enter a number between 2 and 109")

            game = 'on'

            while game == 'on':

                rand_num = randint(z1, z2)

                playerguess = input(f"\nGuess the name of the element with the atomic number {rand_num}: ") 
                
                if playerguess.lower() == element_dict[rand_num].lower():
                    print("Correct!")
                    continue

                else:
                    print(f"Incorrect! It's {element_dict[rand_num]}")                      
                    continue       

        while select_game == 2:
            
            n = 1

            while score >= 0:

                rand_num = randint(1, 109)
                playerguess = input(f"Guess the name of the element with the atomic number {rand_num}: ")
                
                if playerguess.lower() == element_dict[rand_num].lower():

                    score = score + 10
                    print("Correct!")
                    print(f"Score: {score}")

                    n += 1

                else:

                    score = score - 1
                    print(f"Incorrect! It's {element_dict[rand_num]}")
                    print(f"Score: {score}")
                    
                    continue

guesselement1 = GuessElement()
guesselement1.guess_element()





