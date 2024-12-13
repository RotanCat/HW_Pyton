products = dict({})
shop = ""

def counter():
    try:
        with open("input.txt", "r") as file:
            file = file.read().strip("{}").split("},\n")
        for i in file:
            i = i.split('{')
            i = i[1].replace("}\n", "").split(",")
            for fruit in i:
                fruit = fruit.split(":")
                fruit[0] = fruit[0].strip("\n").strip('"')
                fruit[1] = fruit[1]
                if fruit[0] not in products.keys():
                    products[fruit[0]] = int(fruit[1])
                else:
                    products[fruit[0]] += int(fruit[1])
        with open("output.txt", "w") as file:
            for i in products.keys():
                file.write(f'{i} was bought {products[i]} times\n')

    except FileNotFoundError:
        print("File not found")

counter()
