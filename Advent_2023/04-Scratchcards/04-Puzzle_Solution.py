#Puzzle: Day 04 ____________________
#Scratchcards
file = open("04-Puzzle_Inputs.txt","r")

#Data Conversion_____
def dataConvert(file):
    data = list(map(lambda x: x[10:116].split(" | "),file))
    data = list(map(lambda x: [x[0].split(),x[1].split()], data))
    return data


#Part 1_____
def countPoints(data):
    points = list(map(lambda x: int(2**(len(set(x[0])&set(x[1]))-1)),data))
    totalpoints = sum(points)

    return totalpoints

#Part 2_____
def countCards(data):
    points = list(map(lambda x: [1,len(set(x[0])&set(x[1]))],data))
    list(map(lambda x: list(map(lambda y: alterCards(points,y,points[x][0]),range(x+1,x+1+points[x][1]) )), range(len(points)) ))
    cardcopy = list(map(lambda x: x[0],points))
    
    return sum(cardcopy)

def alterCards(array,pos,amount):
    array[pos][0]+=amount


if __name__ == '__main__':    
    data = dataConvert(file)

    print("Total Points of ScratchCards:", countPoints(data))
    print("Total ScratchCards:", countCards(data))
