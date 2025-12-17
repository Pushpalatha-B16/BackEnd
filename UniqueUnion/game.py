import random

def number_guess():
  print("-----This is number guessing game------")
  print("Hey guys  guess a number from 1 to 10")
  user1_name=input(" Enter first player name:")
  user2_name=input("Enter second player name:")
  computer=random.randint(1,10)
  user1=0
  user2=0
  while(computer!=user1 and computer!=user2):
    user1=int(input(f"{user1_name} guess a number:"))
    user2=int(input(f"{user2_name} guess a number:"))
    if computer!=user1 and computer!=user2: 
     if computer!=user1:
      if computer>user1:
        print(f"{user1_name} guess a high value")
      elif computer<user1:
        print(f"{user1_name} guess a low value")
     if computer!=user2:
         if computer>user2:
             print(f"{user2_name} guess a high value")
         elif computer<user2:
              print(f"{user2_name} guess a low value")

  if computer==user1 and computer!=user1  :
      print(f"Hey {user1_name} congratulation ,You won the game ,{computer} is correct guess")
  elif computer==user1 and computer==user2:
      print("Draw the match")
  else:
      print(f"Hey {user2_name} congratulation ,You won the game,{computer} is correct guess")
  again_play()


def char_guess():
  print("-----This is character guessing game------")
  print("Hey guys guess a character from A to K")
  user1_name=input("Enter first player name:")
  user2_name=input("Enter second player name:")

  computer1=random.randint(65,75)
  computer=chr(computer1)
  user1=""
  user2=""
  while(computer!=user1 and computer!=user2):
    user1=input(f"{user1_name} guess a character:").upper()
    user2=input(f"{user2_name} guess a character:").upper()
    if computer!=user1 and computer!=user2: 
     if computer!=user1:
        if computer>user1:
            print(f"Hey {user1_name} guess a character that should be greater than the previous character:")
        elif computer<user1:
            print(f"Hey {user1_name} guess a character that should be less than the previous character:")
     if computer!=user2:
        if computer>user2:
            print(f"Hey {user2_name} guess a character that should be greater than the previous character:")
        elif computer<user2:
            print(f"Hey {user2_name} guess a character that should be less than the previous character:")
   

  if computer==user1 and computer!=user2:
      print(f"Hey {user1_name} congratulation ,You won the game,{computer} is correct guess")
  elif computer==user1 and computer==user2:
      print("Draw the match")
  else:
      print(f"Hey {user2_name}congratulation ,You won the game,{computer} is correct guess")

  again_play()

def gk():
   print("-----This is General Knowlesge game------")
   user1_name=input(" Enter first player name:")
   user2_name=input("Enter second player name:")
   question=[
   {"prompt":"1.Find value:1+2+4+7+11+?","options":["A.10","B.12","C.11","D.16"],"answer":"D"},
   {"prompt":"2.The value of pi?","options":["A.22/7","B.12/2","C.2/11","D.4/16"],"answer":"A"},
   {"prompt":"3.What is the national animal of india?","options":["A.Elephant","B.Tiger","C.Lion","D.None"],"answer":"B"},
   {"prompt":"4.What is the color of 'G' in google ","options":["A.Blue","B.Black","C.none","D.orange"],"answer":"A"},
   {"prompt":"5.Which is the capital of india","options":["A.chennai","B.Bangalore","C.Delhi","D.None"],"answer":"C"}]
   user1_score=0
   user2_score=0
   for i in question:
      print(i["prompt"])
      for j in i["options"]:
        print(j)
      user1=input(f"{user1_name} choose the correct option").upper()
      user2=input(f"{user2_name} choose the correct option").upper()
      if i["answer"]==user1 and i["answer"]!=user2:
            print(f"Hey congratuletions {user1_name}")
            user1_score+=2
      elif i["answer"]==user2 and i["answer"]!=user1:
              print(f"Hey congratuletions {user2_name}")
              user2_score+=2
      elif i["answer"]==user1 and i["answer"]==user1:
         print(f"wow super {user1_name} and {user2_name}")
         user1_score+=2
         user2_score+=2
      else:
            print("The correct answer is:",i["answer"])
           

   if user1_score>user2_score:
       print(f"hey {user1_name} super ,you won the game,your score is:",user1_score)
   else:
        print(f"hey {user2_name} super ,you won the game,your score is:",user2_score)
   again_play()       



def word_guess():
  print("-----This is word guessing game------")
  user1_name=input(" Enter first player name:")
  user2_name=input("Enter second player name:")
  words=random.choice(["mango","orange","apple"])
  word_display=["-" for i in words]
  print("hey guys guess a fruit name")
  attempt=8
  score1=0
  score2=0
  while attempt>0 and "-" in word_display:
     print("word:",' '.join(word_display)) #gap between ---
     user1=input(f"{user1_name} guess a letter").lower()
     user2=input(f"{user2_name} guess a letter").lower()
    
     for index,letter in enumerate(words):
          if letter==user1 and letter!=user2: 
            word_display[index]=user1
            
            score1+=2
            print(f"{user1_name} your guessing is correct!+2 points")
          elif letter==user1 and letter==user2:
             word_display[index]=user1
             score1+=2
             score2+=2
             print(f"Both guessing are correct! +2 points")     
          elif letter==user2 and letter!=user1: 
            word_display[index]=user2
            score1+=2
            print(f"{user2_name} your guessing is correct!+2 points")
     print("current word:"," ".join(word_display))
     attempt-=1
     print(f"Attempt left:{attempt}")
  print("Game over")
  if score1>score2:
          print(f"{user1_name} wins!")
  elif score1>score2:
            print(f"{user1_name} wins!")
  else:
      print("Draw the match")
  again_play()          

import textblob as tb
def feedback():
  print("Guys share your feedback")
  user1_name=input(" Enter first player name:")
  user2_name=input("Enter second player name:")
  user1=input(f"{user1_name} Enter your Feedback")
  user2=input(f"{user2_name}  Enter your feedback")
  s=tb.TextBlob(user1)
  s2=tb.TextBlob(user2)
  range1=s.sentiment.polarity
  range2=s2.sentiment.polarity
  if range1>0 and range2>0:
     print("Hey Guys Thanks for your good feedback")
  elif range1>0 and range2<0:
     print(f"Thanks {user1_name}")
     print(f"Ok {user2_name} we improve our quality")
  elif range2>0 and range1<0:
     print(f"Thanks {user2_name}")
     print(f"Ok {user1_name} we improve our quality")
  else:
     print("Okay guys we improve our quality")

def start():
  
  
  print("1.Guess a number,2.Guess a character,3.Guess a word,4.GK questions",sep="\n")
  gname=int(input("Hey beautiful humans choose any one of the game (1,2,3,4):"))
  if gname==1:
    number_guess()
  elif gname==2:
    char_guess()
  elif gname==3:
    word_guess()
  else:
    gk()
    
def again_play():
  a=input("play again (y/n):").lower()
  if a=="y":
      start()
  else:
    feedback()
  
print("Welcome to our Unique Union game")  
start()
      
      

