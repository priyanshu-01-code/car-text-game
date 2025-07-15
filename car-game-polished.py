#This is the polished version of the original car game I created.

print("""You can type 'start','stop', or 'quit'. Quit would stop the game.
      NOTE: The instructions are case insensitive.
      """)

started = False
stopped = False

while True:
    begin = input('>').upper()

    if begin == 'START':
        if started:
            print("The car is already started.")
        else:
            started = True
            print("The car has started.")
    elif begin == 'STOP':
        if stopped:
            print("The car is already stopped.")
        else:
            stopped = True
            print("The car has stopped.")
    elif begin == 'QUIT':
        started = True
        print("Hope it was fun.")
        break
    else:
        print('I do not quite understand that.')

#I took a bit of help of chatgpt to understand boolean use in these situations.

    






























        
