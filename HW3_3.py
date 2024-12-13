courses = dict({})

def rishum(ask = ""):
    try:
        with open("input.txt", "r") as file:
            file = file.readlines()
        for i in file:
            i = i.split(":")
            j = i[1].strip(" .\n,").split(", ")
            for course in j:
                if course not in courses.keys():
                    courses[course] = [(i[0]).strip(" .\n,").strip()]
                else:
                    courses[course].append((i[0]).strip(" .\n,").strip())
        if ask in courses.keys():
            for i in courses[ask]:
                print(i)
        else:
            print("No info found")


    except FileNotFoundError:
        print("File not found")

ask = input("Type the Course Name: ")
rishum(ask)

