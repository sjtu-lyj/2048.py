__author__ = 'church-father'
import random,copy,sys,os
from numpy import transpose
from colorama import Fore,Back

def reduceLeft_each(ss):
    def fun(ss,interger):
        if(len(ss)==0):
            ss.append(interger)
        elif(ss[-1]==interger):
            ss[-1]*=2
            ss.append(0)
        else:
            ss.append(interger)
        return ss
    ss=filter(lambda x:x!=0,ss)
    ss=filter(lambda x:x!=0,reduce(fun,ss,[]))
    ss.extend([0 for i in range(4-len(ss))])
    return ss

def reduceRight_each(ss):
    return reduceLeft_each(ss[::-1])[::-1]

def reduceLeft(game):
    return map(reduceLeft_each,game)

def reduceRight(game):
    return map(reduceRight_each,game)

def reduceUp(game):
    return transpose(reduceLeft(transpose(game))).tolist()

def reduceDown(game):
    return transpose(reduceRight(transpose(game))).tolist()

def add_random(game):
    ss=[2,2,2,4]
    x=random.randint(0,3)
    y=random.randint(0,3)
    if(game[x][y]==0):
        game[x][y]=ss[random.randint(0,3)]
    else:
        add_random(game)

def clear():
    if(os.name in ('ce','ne','dos')):
        os.system('cls')
    elif('posix' in os.name):
        os.system('clear')

def pretty_print(game):
    def color(x):
        if x == 0:    return Fore.RESET + Back.RESET
        if x == 2:    return Fore.RED + Back.RESET
        if x == 4:    return Fore.GREEN + Back.RESET
        if x == 8:    return Fore.YELLOW + Back.RESET
        if x == 16:   return Fore.BLUE + Back.RESET
        if x == 32:   return Fore.MAGENTA + Back.RESET
        if x == 64:   return Fore.CYAN + Back.RESET
        if x == 128:  return Fore.RED + Back.BLACK
        if x == 256:  return Fore.GREEN + Back.BLACK
        if x == 512:  return Fore.YELLOW + Back.BLACK
        if x == 1024: return Fore.BLUE + Back.BLACK
        if x == 2048: return Fore.MAGENTA + Back.BLACK
        if x == 4096: return Fore.CYAN + Back.BLACK
        if x == 8192: return Fore.WHITE + Back.BLACK
    clear()
    # os.system("clear")
    for i in game:
        for j in i:
            print(color(j)+'{:<4}'.format(str(j))+color(0)),
        print('\n')
    sys.stdout.write('\r')

def new_game():
    game=[[0 for i in range(4)]for j in range(4)]
    add_random(game)
    add_random(game)
    pretty_print(game)
    while True:
        game_back=copy.deepcopy(game)
        indictor=raw_input()
        if indictor=="a":
            game=reduceLeft(game)
        elif indictor=="d":
            game=reduceRight(game)
        elif indictor=="w":
            game=reduceUp(game)
        elif indictor=="s":
            game=reduceDown(game)
        else:
            print("invalid input")

        if(game==game_back):
            print("no change")
        else:
            add_random(game)
            pretty_print(game)

if __name__ == '__main__':
    new_game()
