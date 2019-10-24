def aunty_response(userinput):
    if userinput == "I love you aunty, I have to go now":
        return 4
    elif userinput.islower():
        return 1
    elif userinput.isupper():
        return 2
    # elif userinput.istitle():
    else:
        return 3
    return 0


print("What's your name?")
name = input()

count = 0

while True:
    print('Say something:')
    userinput = input()

    if len(userinput) == 0:
        if count == 1:
            count += 1        
        elif count == 2:
            print("ok. Goodbye")
            break
        else:
            continue
    elif userinput == "exit":
        break
    else:
        count = 0
        result = aunty_response(userinput)
        if result == 1:
            print("WHAT? SPEAK UP!")
        elif result == 2:
            print("YOU ARE VERY RUDE!")
        elif result == 3:
            print("SHOW SOME RESPECT!")
        elif result == 4:
            print("ok. Goodbye")
            print(f"{name}, are you there?")
            count = 1
        else:
            print("ERROR!!!")
            break


