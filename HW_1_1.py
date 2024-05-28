hight = 0

while not(hight > 0 ):
    hight = input('Please enter hight: ')
    if hight.isdigit():
        hight = int(hight)
    else:
        hight = 0

for i in range(hight):
    print(" "*(hight-i-1) + "*"*(2*i+1) + " "*(hight-i-1))
