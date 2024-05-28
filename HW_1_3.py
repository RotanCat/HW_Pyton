number = -1
sum = 0

while (number <0):
    number = input("Enter a number: ")
    if number.isdigit() or (number[0]=='-' and number[1:len(number)].isdigit()):
        number = abs(int(number))
    else: number = -1

sum = str(number)
number = 0

while(len(sum) > 1):
    for i in sum:
        number = number + int(i)
    sum = str(number)
    number = 0

print(sum)