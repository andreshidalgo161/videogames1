from random import randint
import os           
status_menu = True



def main_menu():
      global status_opts
      status_opts = True
      print(":::MAIN MENU:::")
      print("[1]. Start game")
      print("[2]. Help")
      print("[3]. Exit")
      while status_opts:
        opt= int(input("Press any option: "))
        if opt <1 or opt >3:
            print ("Error. Press any option between 1 and 3")
        else :
            status_opts = False
      return opt
      opt=int(input("press any option: "))
      exit            
                        
while status_menu:
    os.system('clear')
    op = main_menu()
    if op == 1:
        os.system('clear')
        print("Welcome to number race")
        players = int(input("Press number of players [1:4]"))
        
        print (":::Level menu:::")
        print("[1]. Basic")
        print("[2]. Intermediate")
        print("[3]. Advance")
        print("[4]. Expert")
        opt = int(input("Pess any option"))
        
        if opt ==1:
            pos =20
        elif opt ==2:
            pos = 30
        elif opt ==3:
            pos = 50
        else:
            pos = 100
        
        #Star game
        status_game = True
        roll_count = 0
        roll_acum = 0
        while status_game:
            os.system('clear')
            key = input("Press any key to roll dice...")

            dice1 = randint(1,6)
            dice2 = randint(1,6)


            print (f"dice 1:{dice1}")
            print (f"dice 2:{dice2}")    
            total = dice1 + dice2
            print(f"Total roll: {total}")
            roll_count += 1 #roll_count = roll_count +1 (forma basica)
            roll_acum += total
            print(f"Total game:{roll_acum}")
            
            if roll_acum >= pos:
                print (":::YOU WIN!, CONGRATULATIONS:::")
                status_game = False
                
            os.system('pause')    
                
        print(":::STATITICS:::")
        print(f"TOTAL rolls: {roll_count}")
        print(f"TOTAL rolls: {roll_acum}")        
                         
        
        
        
        key = input("Press any key to go the main menu...")
    elif op == 2:
        print("Help under construction")
        key = ("Press any key to go the main menu...")
    else:
        print ("See you later")
        key = ("Press any key to exit...")
        break
                  
'''

'''