# This is a simple guess game, player has to guess the name of the element when a number is displayed.

from random import randint

element_name = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium']
b = ['', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt']
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
        
        print("\n1. Display periodic table")
        print("2. Practice")
        print("3. Quiz - Guess the name of Element")
        print("4. Quiz - Guess the Atomic Number")
        print("5. Exit\n")

        while True:

            try:
                select_game = int(input("Choose what you like to do (enter 1 to 5): "))
            except ValueError:
                print("Please choose a game and enter it's number")
                continue
            if select_game not in (1, 2, 3, 4, 5):
                print("Please choose a game and enter it's number")
                continue
            else:
                break

        if select_game == 1:
            
            print('\n')
            print(b[1] + '\t'*17 + b[2])
            print(b[3] + '\t' + b[4] + '\t'*11 + '\t'.join([b[n] for n in range(5, 11)]))
            print(b[11] + '\t' + b[12] + '\t'*11 + '\t'.join([b[n] for n in range(13, 19)]))
            print('\t'.join([b[n] for n in range(19, 37)]))
            print('\t'.join([b[n] for n in range(37, 55)]))
            print('\t'.join([b[n] for n in range(55, 58)]) + '\t' + '\t'.join([b[n] for n in range(72, 87)]))
            print('\t'.join([b[n] for n in range(87, 90)]) + '\t' + '\t'.join([b[n] for n in range(104, 110)]))
            print('\n')
            print('\t'*3 + '\t'.join([b[n] for n in range(58, 72)]))
            print('\t'*3 + '\t'.join([b[n] for n in range(90, 104)]))
            print('\n')

            while True:

                try:
                    x = input("Please press anything to exit: ")
                except:
                    print("I am not using this")
                if x != "I don't think you will type this!":
                    guesselement1.guess_element()
                    break
                else:
                    print("I did't think you will type this string!\n")
                    break
                    
        while select_game == 2:

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

        while select_game == 3:
            
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

        while select_game == 4:
            
            n = 1

            while score >= 0:

                rand_num = randint(0, 108)

                while True:

                    try:
                        playerguess = int(input(f"Guess the atomic number for {element_name[rand_num]}: "))
                    except ValueError:
                        print("please enter the atomic number\n")
                        continue
                    else:
                        break
                
                if playerguess == element_dict_rev[element_name[rand_num]]:

                    score = score + 10
                    print("Correct!")
                    print(f"Score: {score}")

                    n += 1

                else:

                    score = score - 1
                    print(f"Incorrect! It's {element_dict_rev[element_name[rand_num]]}")
                    print(f"Score: {score}")
                    
                    continue

        if select_game == 5:
            print("See you later!")          

guesselement1 = GuessElement()
guesselement1.guess_element()
