#Puzzle: Day 03 ____________________
#Rucksack Reorganization

#PART 1 _____
abcGrHalf = lambda data: map(lambda x: list( set(x[:len(x)//2]) & set(x[len(x)//2:]) )[0], data)

#PART 2 _____
abcGr3Line = lambda data: map(lambda x: list( set(data[x]) & set(data[x+1]) & set(data[x+2]) )[0], range(0,len(data),3))

def totalPoints(abcData):
    alphabets = map(chr, list(range(97, 123))+list(range(65, 91)))
    letter_points = dict(map(lambda x: (x[1],x[0]+1) , enumerate(alphabets)))
    return sum(map(lambda letter: letter_points[letter], abcData))


if __name__ == '__main__':
    data = open('03-Puzzle_Inputs.txt','r')
    data = list(map(lambda val: val.split()[0], data))
   
    print(f'Points for Half-Line: {totalPoints(abcGrHalf(data))}')
    print(f'Points for 3 Line:    {totalPoints(abcGr3Line(data))}')

    
    