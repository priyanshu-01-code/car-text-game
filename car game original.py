
instructions_to_start_the_car = """type 'START' to start the car
type 'STOP' to stop the car
type 'QUIT' to end the game
(you can actually type the same words in any case. It is just representational.)"""

print(instructions_to_start_the_car)

A = 1
while A <= 1:
    y = input('>').upper()

    if y == 'START':
        print("The car has started. VROOOOOOOM!!!")
    elif y == 'STOP':
        print('The car has stopped.')
    elif y == 'QUIT':
        print('Hope you had a nice session.')
        A += 2
        
    else:
        print("Are you blind? Can't you read the instructions?")


 
        
