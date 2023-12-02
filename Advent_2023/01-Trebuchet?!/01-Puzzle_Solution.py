#Puzzle: Day 01 ____________________
#Trebuchet?1
file = open("01-Puzzle_Inputs.txt","r")
import re

#PART 1_____
def calibrationDigitSum(data):
    digits = list(map(lambda word: list(filter(lambda char: char.isdigit(),list(word))), data))
    digits = list(filter(lambda x: x != [], digits))
    calibration_values = list(map(lambda x: int(x[0]+x[-1]), digits))
    return sum(calibration_values)

#PART 2_____
def calibrationNumSum(data):
    str_digits = ['one','two','three','four','five','six','seven','eight','nine']
    digits = ['o1e','t2o','t3e','f4r','f5e','s6x','s7n','e8t','n9e']
    
    dataline = ["_".join(data)]
    list(map(lambda i: dataline.append(re.sub(str_digits[i],digits[i],dataline[-1])), range(9)))
    
    return calibrationDigitSum(dataline[-1].split('_'))


if __name__ == '__main__':    
    data = list(map(lambda x: x.split()[0], file))
    
    print("Digital Calibration Sum:",calibrationDigitSum(data))
    print("True Calibration Sum:",calibrationNumSum(data))
