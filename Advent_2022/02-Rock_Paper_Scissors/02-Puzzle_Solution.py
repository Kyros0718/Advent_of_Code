#Puzzle: Day 02 ____________________
#Rock Paper Scissors
file = open("02-Puzzle_Inputs.txt","r")

#PART 1_____
def addPoints(choice):
    points = 0
    shape = {'X':1,'Y':2,'Z':3}
    points+= shape[choice[1]]
    
    tie_win = {'X':['A','C'],'Y':['B','A'],'Z':['C','B']}
    print
    if  tie_win[choice[1]][0] ==choice[0]:
        points+=3
    elif tie_win[choice[1]][1] ==choice[0]:
        points+=6
    
    return points

#PART 2_____
def cheatPoints(choice): 
    cheat_choice = {'X':'LOSE','Y':'DRAW','Z':'WIN'}
    win_tie_lose = {'A':[8,4,3],'B':[9,5,1],'C':[7,6,2]}

    if cheat_choice[choice[1]] == 'WIN':
        points = win_tie_lose[choice[0]][0]
    elif cheat_choice[choice[1]] == 'DRAW':
        points = win_tie_lose[choice[0]][1]
    else:
        points = win_tie_lose[choice[0]][2]
    
    return points


if __name__ == '__main__':
    combinations = list(map(lambda choice: choice.split(),file))
    print(f'Normal Score: {sum(map(lambda choice: addPoints(choice), combinations))}') 
    print(f'Cheat Score:  {sum(map(lambda choice: cheatPoints(choice), combinations))}')