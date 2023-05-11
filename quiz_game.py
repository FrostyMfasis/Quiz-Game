print ("Welcome to my music quiz!")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print ("Okay! Let's GO!")
score = 0
    
answer = input("What is Michael Jackson's highest selling album?")
if answer.lower() == "thriller":
    print("Correct! WOOHOO!!!!! LET'S GO!")
    score += 25
else:
    print("False!") 
answer = input("What is Drake's first Number 1 song?")
if answer.lower() == "one dance":
    print("Correct! WOOHOO!!!!! LET'S GO!")
    score += 25
else:
    print("False!")
answer = input("What is the name of the Raggae artist who sang 'One Love'?")
if answer.lower() == "bob marley":
    print("Correct! WOOHOO!!!!! LET'S GO!")
    score += 25
else:
    print("False!")
answer = input("Which rapper released the hit song 'Can't touch this.' in 1990?")
if answer.lower() == "mc hammer":
    print("Correct! WOOHOO!!!!! LET'S GO!")
    score += 25
else:
    print("False!") 

Score = 0

print("You got a score of "   + str(score) +  " out of 100!")
