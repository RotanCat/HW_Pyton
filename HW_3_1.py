cities_n = []
number = 0
def ask():
    try:
        number = int(input("Enter population: "))
        return number
    except:
        ask()


def cities(number = 0):
    try:
        with open("cities.txt", "r") as cities:
            cities = cities.readlines()
            for i in cities:
                cities_n.append(i.rstrip("\n").split(":"))
            cities = []
            for i in range(len(cities_n)):
                if int(cities_n[i][1])>=number:
                    cities.append(cities_n[i][0])
            cities.sort()
            with open("filtered_cities.txt", "w") as file:
                for i in cities:
                    file.write(i+"\n")
    except FileNotFoundError:
        print("No file found")

number = ask()
cities(number)