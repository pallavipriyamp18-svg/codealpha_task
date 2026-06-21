import random
words=["avengers","jarvis","bridgertona","summera","warma"]
chance=6
w=random.choice(words)
print(w)#line for testing.
while(chance>0):
    print("enter your guess: ")
    guess=input()
    if guess in w:
       print("Congragulations!. you have guessed correctly")
       for i in w :
           if guess==i:
               index=w.index(i)
               index=index+1
               print(f"The position you have guessed correctly is {index}")
           
    #continue
    else:
        print("Incorrect guess.")
        chance=chance-1
        if(chance<=0):
            print("sorry mate ;( you lost.")
        print(f" you can guess {chance} more times")
print(f"The word is {w}")

    
   
