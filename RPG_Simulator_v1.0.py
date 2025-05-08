#characters = ["Knight", "Wizard"]
#Knight = {"str": 5, "int": 2, "HP": 150, "MP": 50}
#Wizard = {"str": 1, "int": 5, "HP": 50, "MP": 150}

characters = {"Knight": {"str": 5, "int": 2, "HP": 150, "MP": 50}, "Wizard": {"str": 1, "int": 5, "HP": 50, "MP": 150}}

enemies = {"Fox": {"str": 2, "int": 2, "HP": 50, "MP": 0}, "Dragon": {"str": 20, "int": 20, "HP": 500, "MP": 500}}


def show_menu():
    print("\n===== RPG SIMULATOR v1.0 =====")
    print("1. Easy mode") # vs. Fox
    print("2. Hard mode") # vs. Dragon
    print("3. Exit")

def character_menu():
    print("\n ===== Select your character =====")
    print("1. Knight")
    print("2. Wizard")
    print("3. Exit")

def battle_menu():
    print("\n***** BATTLE *****")
    print("1. Attack")
    print("2. Spell")

# attack = character's str*4
# spell = character's int*6, use 10 MP

while True:
    show_menu()
    mode = input("Enter a number which you want to paly : ")

    if mode == "1":
        mob = "Fox"
        enemy = enemies[mob]
        attack_m = enemy["str"]*4
        spell_m = enemy["int"]*6 # Fox can't use
        HP_m = enemy["HP"]
        MP_m = enemy["MP"]

        while True:
            character_menu()
            character = input("Select your character 1~2 : ")

            if character == "1":
                selected = "Knight"
                you = characters[selected]
                attack = you["str"]*4
                spell = you["int"]*6
                HP = you["HP"]
                MP = you["MP"]
        
                print("\n**********************************************")
                print("\nWild", mob, "appeared!")
                while HP_m>0 and HP>0:
                    print("\nEnemy :", mob, "| HP :", HP_m, "| MP :", MP_m)
                    print("\nYou :", selected,"| HP :", HP, "| MP :", MP)
                    battle_menu()
                    choice = input("\nChoose your next action 1-2 : ")
        
                    if choice == "1":
                        print("\nYou attacked", mob+"!")
                        print("Fox damaged ", attack)
                        HP_m = HP_m-attack

                        if HP_m<0:
                            print(mob,"is defeated!")
                            break

                        print("\n"+mob+"'s attack!")
                        print("You damaged", attack_m)
                        HP = HP-attack_m

                    elif choice == "2":
                        if MP<10:
                            print("Not enough MP!")
                        else:
                            print("\nYou recited sepll to", mob)
                            print(mob, "damaged", spell)
                            HP_m = HP_m-spell
                            MP = MP-10

                            if HP_m<0:
                                print(mob,"is defeated!")
                                break

                            print("\n"+mob+"'s attack!")
                            print("You damaged", attack_m)
                            HP = HP-attack_m
                if HP_m<=0:
                    print("You Win!")
                    break

                elif HP<=0:
                    print("You died...")
                    break               

            if character == "2":
                selected = "Wizard"
                you = characters[selected]
                attack = you["str"]*4
                spell = you["int"]*6
                HP = you["HP"]
                MP = you["MP"]
        
                print("\n**********************************************")
                print("\nWild", mob, "appeared!")
                while HP_m>0 and HP>0:
                    print("\nEnemy :", mob, "| HP :", HP_m, "| MP :", MP_m)
                    print("\nYou :", selected,"| HP :", HP, "| MP :", MP)
                    battle_menu()
                    choice = input("\nChoose your next action 1-2 : ")
        
                    if choice == "1":
                        print("\nYou attacked", mob,"!")
                        print("Fox damaged ", attack)
                        HP_m = HP_m-attack

                        if HP_m<0:
                            print(mob,"is defeated!")
                            break

                        print("\n"+mob+"'s attack!")
                        print("You damaged", attack_m)
                        HP = HP-attack_m

                    elif choice == "2":
                        if MP<10:
                            print("Not enough MP!")
                        else:
                            print("\nYou recited sepll to", mob)
                            print(mob, "damaged", spell)
                            HP_m = HP_m-spell
                            MP = MP-10

                            if HP_m<0:
                                print(mob,"is defeated!")
                                break

                            print("\n"+mob+"'s attack!")
                            print("You damaged", attack_m)
                            HP = HP-attack_m
                if HP_m<=0:
                    print("You Win!")
                    break

                elif HP<=0:
                    print("You died...")
                    break

    elif mode == "2":
        mob = "Dragon"
        enemy = enemies[mob]
        attack_m = enemy["str"]*4
        spell_m = enemy["int"]*6 # Fox can't use
        HP_m = enemy["HP"]
        MP_m = enemy["MP"]

        while True:
            character_menu()
            character = input("Select your character 1~2 : ")

            if character == "1":
                selected = "Knight"
                you = characters[selected]
                attack = you["str"]*4
                spell = you["int"]*6
                HP = you["HP"]
                MP = you["MP"]
        
                print("\n**********************************************")
                print("\nWild", mob, "appeared!")
                while HP_m>0 and HP>0:
                    print("\nEnemy :", mob, "| HP :", HP_m, "| MP :", MP_m)
                    print("\nYou :", selected,"| HP :", HP, "| MP :", MP)
                    battle_menu()
                    choice = input("\nChoose your next action 1-2 : ")
        
                    if choice == "1":
                        print("\nYou attacked", mob+"!")
                        print("Fox damaged ", attack)
                        HP_m = HP_m-attack

                        if HP_m<0:
                            print(mob,"is defeated!")
                            break

                        print("\n"+mob+"'s attack!")
                        print("You damaged", attack_m)
                        HP = HP-attack_m

                    elif choice == "2":
                        if MP<10:
                            print("Not enough MP!")
                        else:
                            print("\nYou recited sepll to", mob)
                            print(mob, "damaged", spell)
                            HP_m = HP_m-spell
                            MP = MP-10

                            if HP_m<0:
                                print(mob,"is defeated!")
                                break

                            print("\n"+mob+"'s attack!")
                            print("You damaged", attack_m)
                            HP = HP-attack_m
                if HP_m<=0:
                    print("You Win!")
                    break

                elif HP<=0:
                    print("You died...")
                    break               

            if character == "2":
                selected = "Wizard"
                you = characters[selected]
                attack = you["str"]*4
                spell = you["int"]*6
                HP = you["HP"]
                MP = you["MP"]
        
                print("\n**********************************************")
                print("\nWild", mob, "appeared!")
                while HP_m>0 and HP>0:
                    print("\nEnemy :", mob, "| HP :", HP_m, "| MP :", MP_m)
                    print("\nYou :", selected,"| HP :", HP, "| MP :", MP)
                    battle_menu()
                    choice = input("\nChoose your next action 1-2 : ")
        
                    if choice == "1":
                        print("\nYou attacked", mob,"!")
                        print("Fox damaged ", attack)
                        HP_m = HP_m-attack

                        if HP_m<0:
                            print(mob,"is defeated!")
                            break

                        print("\n"+mob+"'s attack!")
                        print("You damaged", attack_m)
                        HP = HP-attack_m

                    elif choice == "2":
                        if MP<10:
                            print("Not enough MP!")
                        else:
                            print("\nYou recited sepll to", mob)
                            print(mob, "damaged", spell)
                            HP_m = HP_m-spell
                            MP = MP-10

                            if HP_m<0:
                                print(mob,"is defeated!")
                                break

                            print("\n"+mob+"'s attack!")
                            print("You damaged", attack_m)
                            HP = HP-attack_m
                if HP_m<=0:
                    print("You Win!")
                    break

                elif HP<=0:
                    print("You died...")
                    break

    elif mode == "3":
        print("Goodbye!")
        break
