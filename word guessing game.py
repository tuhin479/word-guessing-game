word='apple'
chances=10
GuessAdd=[]
done=False
while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end =' ')
        else:
            print('_',end='')
            
    myguess=input(f'your chances is {chances}, Guess the letter:')       
    GuessAdd.append(myguess.lower())
    if myguess. lower() not in word.lower():
         chances = chances-1
         if chances==0:
             break
    done =True
    for letter in word:
             if letter.lower() not in GuessAdd:
              done=False

if done:
    print('yes,u have won the game,the word is {word}')
else:
   print(' You lose the game')















