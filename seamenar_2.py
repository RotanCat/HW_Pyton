rolls = []
sum = 0.0

def calc(rolls = []):
    global sum
    sum = 0
    print(f"Lowest value is: {min(rolls)}")
    print(f"Highest value is: {max(rolls)}")
    for i in rolls:
        sum +=i
    print(f"Average is {sum/len(rolls)}")


def longest_up(rolls = []):
    longest_list = []
    current_list = []
    prev = 0
    for num, i in enumerate(rolls):
        if i >= prev:
            current_list.append(i)
        else:
            longest_list.append(current_list)
            current_list = [i]

        if num == len(rolls)-1:
            longest_list.append(current_list)

        prev = i
    current_list = []

    for i in longest_list:
        if len(i) > len(current_list):
            current_list = i
    print(f"Longest ascending sequence is {current_list}")



def roll():
    global rolls
    while 1:
        dice = input("Put in dice rolls, separated by spaces:")

        dice = (dice.split(' '))
        for i in dice:
            if i.isdigit() and int(i) in range(1,7):
                rolls.append(int(i))
            elif i == "r":
                rolls = []
            elif i == "stop":
                return True
            else:
                print(f"value '{i}' not registered")
        return False
        if (len(rolls) > 0):
            break

while True:
    if roll():
        break
    calc(rolls)
    longest_up(rolls)
    print(rolls)
