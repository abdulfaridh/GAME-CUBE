word='Secret' 
allowed_errors=6 
guesses=[] 
done=False
while not done:
    for letter in word: 
        if letter.lower() in guesses: 
            print(letter,end=" ")
        else: 
            print("_",end=" ")
print("")
guess=input(f"Allowed Errors Left {allowed_errors}, Next guess:: ")
guesses.append(guess.lower())
if guess.lower() not in word.lower():
    allowed_errors-=1
    if allowed_errors == 0:
        breakpoint
    
done=True
for letter in word: 
    if letter.lower() not in guesses: 
        done=False
        
if done: 
    print(f"You Found the word!!!...It was {word}!!") 
else: 
    print(f"Game over!! The word was {word}!!")

