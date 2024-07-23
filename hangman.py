import random
import hang_pics
somewords=['apple', 'banana','orange']
lives=6
word=random.choice(somewords)
print("guess the word:Hint!! it is a name of a fruit")

display=[]
for i in word:
    display+='_'
print(display)
game=False
while not game and lives>0:
   guessw=input('enter a guess\n')
   for position in range(len(word)):
       if guessw==word[position]:
           display[position]=guessw
   print(display)
   
   if guessw not in word:
       print('ooops! wrong guess')
       lives=lives-1
       print("No worries you have ",lives,"lives")
       print(hang_pics.HANGMANPICS[5-lives])
   if '_' not in display:
       break
if '_' not in display:
    print("You won! congratulations") 
else:
    print('You lost better luck next time')    
      

print('the word is',word)