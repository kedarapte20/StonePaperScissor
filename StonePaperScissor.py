import random
def user_choice():
    global x
    if x==1:
        return('User has chosen Rock'.upper())
        return x
    elif x==2:
        return('User has chosen Paper'.upper())
        return x
    elif x==3:
        return('User has chosen Scissors'.upper())
        return x
    else:
        while True:
            x=int(input('Choose Correct Option: '))
            if x in (1,2,3):
                if x==1:
                    return('User has chosen Rock'.upper())
                    return x
                elif x==2:
                    return('User has chosen Paper'.upper())
                    return x
                elif x==3:
                    return('User has chosen Scissors'.upper())
                    return x
                    break
                else:
                    continue
def comp_choice():
    global c
    print('Now its Computers turn'.upper())
    if c==1:
        return('Computer has chosen Rock'.upper())
        return c
    elif c==2:
        return('Computer has chosen Paper'.upper())
        return c
    elif c==3:
        return('computer has chosen Scissors'.upper())
        return c
def win(x,c):
    if x==1 and c==1:
        print('user-rock v/s computer-rock'.upper())
        return('its a tie!!'.upper())
    elif x==1 and c==2:
        print('user-rock v/s computer-paper'.upper())
        return('computer wins!!'.upper())
    elif x==1 and c==3:
        print('user-rock v/s computer-scissors'.upper())
        return('user wins!!'.upper())
    elif x==2 and c==1:
        print('user-paper v/s computer-rock'.upper())
        return('user wins!!'.upper())
    elif x==2 and c==2:
        print('user-paper v/s computer-paper'.upper())
        return('its a tie!!'.upper())
    elif x==2 and c==3:
        print('user-paper v/s computer-scissors'.upper())
        return('computer wins!!'.upper())
    elif x==3 and c==1:
        print('user-scissors v/s computer-rock'.upper())
        return('computer wins!!'.upper())
    elif x==3 and c==2:
        print('user-scissors v/s computer-paper'.upper())
        return('user wins!!'.upper())
    elif x==3 and c==3:
        print('user-scissors v/s computer-scissors'.upper())
        return('its a tie!!'.upper())


def play_again():
    global z
    option=True
    while True:
        z=input('Type Y for Yes and N for No: '.upper())     
        if z=='N':
            print('the end!!'.upper())
            game_Play=False
            option=False
            return ''
            break
        elif z=='Y':
            game_Play=True
            return ''
            break        
        else:
           print('Choose Correct Option: ')
           continue 

game_Play=True
while game_Play:
    print('Welcome to Rock-Paper-Scissors: '.upper())
    print('The Options Are:\n1)Rock\n2)Paper\n3)Scissors\n'.upper())
    print('Its Users turn\n'.upper())
    x=int(input('Choose Your Option: '.upper()))
    print(user_choice())
    c=random.randint(1,3)
    print(comp_choice())
    print(win(x,c))
    print('Do you Want to Play Again? '.upper()) 
    print(play_again())
    if (z=='N'):
        break
    else:
        continue