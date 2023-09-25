#Puzzle: Day 01 ____________________
#Calorie Counting
file = open("01-Puzzle_Inputs.txt","r")

#Return True Integer to the List
def trueNumber(val):
    if val.isdigit():
        return int(val)
    elif val == '\n':
        return ''
    else:
        return int(val[:len(val)-1])

#Group Calories Together into a List
def groupIt(raw_list):
    true_list = []
    for i in range(raw_list.count("")):
        true_list.append(raw_list[:raw_list.index("")])
        raw_list = raw_list[raw_list.index("")+1:]
    true_list.append(raw_list)
    return true_list

#PART 1_____
def highestCalories(true_list): 
    return max(map(sum,true_list))

#PART 2_____
def topThreeCalories(true_list): 
    temp = list(map(sum,true_list))
    temp.sort()
    return sum(temp[len(temp)-3:])


if __name__ == '__main__':        
    raw_list = list(map(lambda val:trueNumber(val), file))
    true_list = groupIt(raw_list)
    
    print(f'Highest Total Calories: {highestCalories(true_list)}')
    print(f'Top 3 Total Calories:   {topThreeCalories(true_list)}')


        