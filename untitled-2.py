# Introduction 
print("welcome to Text Monster Game. In this game, there are 3 floors and 15 rooms in total and you will be stationed in one of the rooms and your task is to find the prize. But you will also find each of the 3 monsters, boss monster, a magic stone, and 4 swords.  Your job is to get through all of them, and in order to do that you will type in the keys left, right, up, down, kill, and grab. Good luck!" )

#create variables
# Build a map with lists - 1 list per floor
floor_1 = ['monster', 'sword', 'upstairs', 'sword', 'nothing']
floor_2 = ['sword', 'magic stone', 'sword', 'upstairs', 'monster']
floor_3 = ['prize', 'boss monster', 'sword', 'monster', 'downstairs']

# User variables 
user_room = 4
user_floor = floor_1
game_over = False # keeps track of game play
user_items = [] # keeps track of what user has; cannot be more than 3 items
last_command = ""


# while loop for the game (game is over when user grabs prize or monster defeats user)
while (game_over==False): 

  
  
  # asks the user for an input/prompt user 
  user_input = (input(" what would you like to do? "))
  

  # left command 
  if user_input == "left":
    if user_room == 0:
      print("there are no more rooms")
    elif user_floor[user_room] == "monster" and last_command == "left" :
      print("you lost")
      game_over = True
    else:
      user_room = user_room - 1
     
      
    # right command 
  elif user_input == "right":
    if user_room == 4:
      print("there are no more rooms")
    elif user_floor[user_room] == "monster" and last_command == "right" :
      print("you lost")
      game_over = True 
    else:
      user_room = user_room + 1 

    
  # up command
  elif user_input == "up":
    if user_floor[user_room] == "upstairs":
      if user_floor == floor_1:
        user_floor = floor_2
      else:
        user_floor = floor_3 
    else:
      print("there is no staircase to go upstairs")
        
  
  # down command
  elif user_input == "down":
    if user_floor[user_room] == "downstairs":
      if user_floor == floor_3:
        user_floor = floor_2
      else: 
        user_floor = floor_1
    else:
      print("there is no staircase to go downstairs")
  
  # grab command
  elif user_input == "grab":
    if len(user_items) < 3:
      if user_floor[user_room] == "sword" or user_floor[user_room] == "magic stone":
        user_items.append(user_floor[user_room])
        user_floor[user_room] = "nothing"
      elif user_floor[user_room] == "prize":
        print("you won the game!")
        game_over = True
      else:
        print("you can't grab")
    else:
      print("you can't grab more than 3 items")
  
  # fight command
  elif user_input == "fight":
    if user_floor[user_room] == "monster":
      if "sword" in user_items:
        user_floor[user_room] = "nothing"
        user_items.remove("sword")
      else: 
        print("you lost ")
        game_over = True 
    if user_floor[user_room] == "boss monster":
      if "sword" in user_items and "magic stone" in user_items:
        user_floor[user_room] = "nothing"
        user_items.remove("sword")
        user_items.remove("magic stone")
      else: 
        print("you lost")
        game_over = True 
      
      
       
    
    
  #elif user_input == "fight"
    
  
  # update
  print ("this room has: " + user_floor[user_room])
  
  last_command = user_input 
