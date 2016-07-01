#All characters will start with these stats
money = 80
skill = 30
strength = 40
personal_inventory = ['- Hammer', '- Shirt']


#Living Room (Sanctuary after Mountains)        
def living_room():
    global strength, money, skill
    print "<<Living Quarters>>"
    print "You enter a quiet room with various sofas and beds."
    print "An old man approaches you."
    print "He says, 'Would you like to rest here to regain your strength?'"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
    
    choice = raw_input(">> ").lower()
    if choice == "yes":
        strength +=150
        print "You have regained some strength."
        mountain_room_rerun()
                    
    elif choice =="no":
        dead("You succumb to your injuries.")
        
    else:
        print "Please enter 'yes' or 'no'."
        
        
def mountain_room_rerun():
    global money, strength
    print "Would you like to fight the lion again?"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
    
    choice = raw_input(">> ").lower()
    
    if choice == "yes": 
        mountain_room()
    elif choice =="no":
        print "OK fair enough. Train up and improve your swordsmanship first!"
        arena_room()
    else:
        print "Please enter 'yes' or 'no'."

#The City Shop (South of the Welcome Room)                                              
def shop_room():
    global money, strength, personal_inventory
    shop_inventory = ['- Tunic', '- Sword', '- Boots']
    print "<<City Shop>>"
    print "A friendly merchant greets you as you enter room with an assortment of items."
    print "He says, 'Greetings %s! What would you like to buy?" % name
    for i in shop_inventory:
        print "%s" % i
    print "[Money: %d dirums, Strength: %d]" % (money, strength)

    choice = raw_input(">> ").lower()
    
    if choice == "tunic":
        money -= 50
        personal_inventory.append('- Tunic')
        shop_inventory.remove('- Tunic')
        print ">>>>>>>>"
        print "You have bought a Tunic!"
        print "You now have these in your inventory:"
        for i in personal_inventory:
            print "%s" % i
        print "These are the items left in the shop:"
        for j in shop_inventory:
            print "%s" % j
        print "Thank you for shopping! Goodbye."
        exit(0)
            
    elif choice == "sword":
        money -= 100
        personal_inventory.append('- Sword')
        shop_inventory.remove('- Sword')
        print ">>>>>>>>"
        print "You have bought a Sword!"
        print "You now have these in your inventory:" 
        for i in personal_inventory:
            print "%s" % i
        print "You are now ready to train!"
        training_room()
            
    elif choice == "boots":
        money -= 30
        personal_inventory.append('- Boots')
        shop_inventory.remove('- Boots')
        print ">>>>>>>>"
        print "You have bought Boots!"
        print "You now have these in your inventory:" 
        for i in personal_inventory:
            print "%s" % i
        print "You are now ready to train!"
        training_room()
    else:
        print "Please select an item."

#The Kitchens (North of the Welcome Room)                     
def kitchens_room():
    global strength, money
    print "<<The Kitchens>>"
    print "The smell of garlic wafts over you."
    print "A long queue has already formed for dinner."
    print "A young woman tells you that having a good meal will help you increase your strength."
    print "Will you eat?"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
    
    choice = raw_input(">> ").lower()
        
    if choice == "yes":
        strength += 50
        money -= 10
        print "You gobble up a plate of hot ribs and regain some strength."
        print "Oops, did the woman forget to tell you you have to pay? That will be 10 dirums."
        print "[Money: %d dirums, Strength: %d]" % (money, strength)
        kitchens_to_shop()
                
    elif choice == "no":
        dead ("That's too bad! Hunger pangs hit you.")
            
    else:
        print "Please tell us your choice: 'yes' or 'no."

def kitchens_to_shop():
    print "Would you like to go shopping now?"
    
    choice = raw_input(">> ").lower()
    
    if choice == "yes":
        shop_room()
    if choice == "no":
        print "Let's try some training then!"
        training_room()
    else:
        print "Please say hi"

#Training Room (East of the Welcome Room)     
def training_room():
    global money, strength
    print "<<Training Room>>"
    print "The room is spartan, barring the weapons that decorate its walls."
    print "An old man smiles and asks, 'Good day %s! What would you like to learn today? Swordsmanship or Boxing?' " % name
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
  
    while True:
        choice = raw_input(">> ").lower()
        
        if choice == "swordsmanship":
            arena_room()
        elif choice == "boxing":
            mountain_room()
        else:
            print "Please select either 'Swordsmanship' or 'Boxing'."
 
#Arena (After the Training Room)    
def arena_room():
    global money, strength
    print "<<Throne Arena>>"
    print "As you step into the arena, you stand facing two knights."
    print "Sir Davos and Lady Sansa."
    print "Who would you like to train with?"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)

    while True:
        choice = raw_input(">> ").lower()
    
        if "davos" in choice:
            davos()
        elif "sansa" in choice:
            sansa()
        else:
            print "Please select either Sir Davos or Lady Sansa."

def davos():
    global personal_inventory, strength
    print "Sir Davos throws an axe onto the ground."
    print "'Go on, pick it up, he says.'"
    print "Do you pick up the axe?"
    axe_wielded = False
    
    while True:
        choice = raw_input(">> ").lower()
    
        if choice == "no":
            print "Sir Davos spits at you and kicks you out of the arena in anger."
            training_room()
        elif choice == "yes" and not axe_wielded:
            personal_inventory.append('Axe')
            print "You pick up the axe."
            print "'Now, try it. Swing the axe,' Sir Davos says."
            axe_wielded = True
        elif choice == "swing axe" and axe_wielded:
            strength += 1000
            print "Sir Davos says, 'Great work, %s. You're ready to fight the lion.'" % name
            mountain_room()
        else:
            print "Try entering that again!"
                
       
def sansa():
    global money, strength, personal_inventory
    print "Lady Sansa wields a double-edged sword."
    print "She looks at you up and down and says, 'Your education will cost you money, %s,'" % name
    print "'How much will you pay me?'"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
    
    try:
        choice = int(raw_input(">> "))
        
        if choice <= 100:
            print "'Are you kidding me? %s dirums. That's nothing.'" % choice
            print "'I cannot teach you. Please leave the arena,' Lady Sansa says coolly."
            training_room()
        if choice > 100 and money <= choice:
            print "'You don't have enough. You only have %d dirums.'" % money
            print "'I cannot teach you. Please leave the arena,' Lady Sansa says coolly."
            training_room()
        else:
            money -= choice
            strength += 400
            print "Lady Sansa bows to you."
            print "'Thank you, %s. We can begin your lesson,' she says." % name
            print "Lady Sansa demonstrates how to wield a sword and passes you her sword."
            print "'Here you go, %s. Now you are ready to fight the lion.'" % name
            personal_inventory.append('Sword')
            mountain_room()
        
            
    except ValueError:
        print "'Are you joking? That's not a number. Come back later when you have something to offer,' Lady Sansa says coolly."
        training_room()
        

def mountain_room():
    global money, strength
    print "<<Misty Mountains>>"
    print "A chilly gust of wind sweeps across as you stand before snow-capped peaks."
    print "Suddenly, a lion jumps out at you."
    print "What do you do?"
    print "1. Fight it"
    print "2. Flee"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)

    lion_dead = False
    
    while True:
        choice = raw_input(">> ")
    
        if choice == "1" and strength >= 100:
            print "You have defeated the lion and gained the title of knight. Congrats!"
            exit(0)
        elif choice == "1" and strength <100:
            strength -=30
            print "The lion leaps at you and knocks you to the ground."
            print "What will you do?"
            print "1. Continue to fight"
            print "2. Flee"
            print "[Money: %d dirums, Strength: %d]" % (money, strength)

            
            fight_choice = raw_input(">> ")
            if fight_choice == "1":
                dead("The lion disembowels you.")
            elif fight_choice == "2":
                living_room()
            else: 
                print "Please enter '1' for attack or '2' for flee."
            
        elif choice == "2":
            training_room()
        else: 
            print "Please enter '1' for fight or '2' for flee."
            

def welcome_room():
    global money, strength
    print "<<Welcome Room>>"
    print "You're surrounded by lush green and a flowing stream."
    print "A young man in a tunic smiles at you."
    print "He says, 'Welcome to the Land of Dreams, %s. Feel free to explore!'" % name
    print "(You can go 'N', 'S', 'E' from here)"
    print "[Money: %d dirums, Strength: %d]" % (money, strength)
    
    while True: 
        choice = raw_input(">> ").lower()
        
        if choice == "n":
            kitchens_room()
        elif choice == "s":
            shop_room()
        elif choice == "e":
            training_room()
        else:
            print "Please select a direction."
            
def dead(why):
    print why, "Your consciousness fades away as you collapse."
    exit(0)
   
    
name = raw_input("Welcome to the Land of Dreams! May we have your name? >> ")

print "Greetings %s!" % name
print "-----------------------------------"

welcome_room()
    
