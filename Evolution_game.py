#Creat class "kind"
#with attributes: name, size, food (plant / kind name), enviroment (water / ground / air), lifespan
#Create 12 spicies (subclasses of the class)

#User adds objects of each spicies
#with attributes: age, saturation, sex
#User can increase plant base;
#check each objects attributes
#initiate sexual reprodaction
#initiate timeskip of 1 year

import random
description = [name := '', size := 0, food := [], enviroment := 'ground', lifespan := 1]
kind_list = []
food_list = ['plant']
parameters = [name := 0, age := 0, saturation := 100, sex := 'M']
entities = []
plants = 0                                                  #amount of plant food avaliable

class Kind:
    def __init__(self, description):
        self.name = description[0]
        self.size = description[1]
        self.food = description[2]
        self.enviroment = description[3]
        self.lifespan = description[4]

    def __str__(self):
        return f'name: {self.name},\tsize: {self.size},\tfood: {self.food},\tenviroment: {self.enviroment},\tlifespan: {self.lifespan}'

    def print_kind(self, name):
        print(self.__str__())


class Entity:
    def __init__(self, parameters):
        self.name = parameters[0]
        self.age = parameters[1]
        self.saturation = parameters[2]
        self.sex = parameters[3]

    def __str__(self):
        return f'name: \033[1m{self.name}\033[22m,\tage: \033[1m{self.age}\033[22m,\tsaturation: \033[1m{self.saturation}\033[22m,\tsex: \033[1m{self.sex}\033[22m'

    def reproduction(self, amount, saturation, name):
        try:
            print(f"{amount} entities with {saturation}% saturation  were successfully created")
            create_entity(name, entities, amount, saturation)
        except:
            print("Error1")



def year_pass():
    global plants
    global entities
    destroy = []
    prey_list = entities.copy()
    for entity in entities:
        kind = kind_list[int(entity.name)]
        entity.age += 1
        if entity.age > kind.lifespan:                                          #too old die
            plants += kind.size
            destroy.append(entity)
        else:
            ate = False
            destroy_prey = []
            if "plant" in kind.food and plants > 0:                              #Herbivores
                plants -= 1
                entity.saturation = min(entity.saturation + 26, 100)
                ate = True

            else:                                                               #Carnivores (and omnivores if plants are over)
                for i in kind.food:
                    for prey in prey_list:
                        if str(i) == str(prey.name):
                            if random.choice((True,False)):
                                entity.saturation = min(entity.saturation + 53, 100)
                                destroy_prey.append(prey)
                                destroy.append(prey)
                                ate = True
                            else:
                                entity.saturation -= 16
                            break
            for prey in destroy_prey:
                prey_list.remove(prey)

            if not ate:
                entity.saturation -= 9                                                                 #Hunger for not eating

            if entity.saturation <=0:
                plants += kind.size
                destroy.append(entity)

    for entity in destroy:
        entities.remove(entity)



def create_kind(food_list):
    for i in range(0, 12):
        description[0] = i
        description[1] = random.choice(range(1,5))
        #skipping the food
        description[3] = random.choice(['ground', 'water', 'air'])
        description[4] = random.choice(range(1,20))
        kind_name = Kind(description)
        kind_list.append(kind_name)

    for i in kind_list:
        food_list.append(i.name)
        food_list.append('plant')

    for i in kind_list:
        i.food = []
        j = random.randint(1, 4)
        while j>0:
            j-=1
            food = random.choice(food_list)
            i.food.append(food)
        i.food = list(set(i.food))
        print(i)

def recall_kind():
    try:
        name = int(input('Enter a kind name to recall (0 to 11): '))
        return kind_list[name]
    except:
        print('Invalid number')
        recall_kind()

def create_entity(name, entities, amount, saturation = 100): #ADD ATTRIBUTES
    try:
        parameters[0] = name
        parameters[1] = 0
        parameters[2] = saturation
        for i in range(amount):
            parameters[3] = random.choice(('M','F'))
            i = Entity(parameters)
            entities.append(i)
    except:
        print('Invalid number3')


def recall_entity(name, entities = entities):
    try:
        kind = []
        for i in entities:
            if i.name == name:
                kind.append(i)
        return kind

    except:
        print('Invalid number')
        return []




def main():
    ### Creating entities ###
    name = input('\nDo you want to \033[31mCreate\033[0m entities? (Enter to pass, kind name (0 to 11) to go): ')
    try:
        if len(name) == 0:
            pass
        elif (int(name) in range(0, 12)):
            amount = int(input('Enter amount of entities to create: '))
            create_entity(name, entities, amount)
        else:
            print('Invalid number1')
    except:
        print('Invalid number2')


    ### Printing out entities of specified kind ###
    name = input('\nDo you want to \033[32mRecall\033[0m entities (Enter to pass, kind name (0 to 11) or "ALL" to go): ')
    if len(name) >= 1:
        if name == 'ALL':
            print("Here are all living entities:")
            for name in range(0,12):
                if len(recall_entity(str(name), entities)) == 0:
                    pass
                else:
                    print(*(recall_entity(str(name), entities)), sep='\n')
        elif len(recall_entity(name, entities)) == 0:
            print('No entities of this kind were found')
        else:
            print(*(recall_entity(name, entities)), sep='\n')


    name = input('\nDo you want to \033[33mInitiate reproduction\033[0m? (Enter to pass, kind name (0 to 11) to go): ')
    if len(name) >= 1:
        kind = recall_entity(name, entities)
        if len(kind) <=1:
            print('Not enough entities to breed!')
        else:
            for i in range(len(kind)):
                print(f'{i}: {kind[i]}')
            try:
                entity_1 = kind[int(input('\nPlease, choose \033[33mFirst\033[0m entity to breed:'))]
                entity_2 = kind[int(input('Please, choose \033[33mSecond\033[0m entity to breed:'))]
                if entity_1.sex != entity_2.sex:
                    print('You are allowed to breed!')
                    enviroment = kind_list[int(name)].enviroment
                    if enviroment == "water":
                        if entity_1.saturation > 50 and entity_2.saturation > 50:
                            amount = 10
                            saturation = 23
                            entity_1.reproduction(amount, saturation, entity_1.name)
                        else:
                            print("Hungry entities can't breed")

                    elif enviroment == "air":
                        if entity_1.saturation > 42 and entity_2.saturation > 42 and entity_1.age >3 and entity_2.age >3:
                            amount = 4
                            saturation = 64
                            entity_1.reproduction(amount, saturation, entity_1.name)
                        else:
                            print("Hungry or young entities can't breed")
                    elif enviroment == "ground":
                        if entity_1.saturation > 20 and entity_2.saturation > 20 and entity_1.age > 5 and entity_2.age > 5:
                            amount = 2
                            saturation = 73
                            entity_1.reproduction(amount, saturation, entity_1.name)
                        else:
                            print("Hungry or young entities can't breed")
                else:
                    print('You are NOT allowed to breed (gay)!')

            except:
                print('Invalid number4')


    years = input('\nDo you want to \033[34mInitiate TimeSkip\033[0m? (Enter to pass, Number of years to go): ')
    if len(years) >= 1:
        try:
            name = input('\nDo you want to \033[35mIncrease food supplies\033[0m? (Enter to pass, amount of food to go): ')
            if len(name) >= 1:
                global plants
                plants += int(name)
            for n in range(int(years)):
                year_pass()
        except:
            print('Invalid number5')

    name = ''




create_kind(food_list)              #initiating programm by creating 12 spicies

while True:                         #main gameloop
    main()

#print(recall_kind())               #shows a specified kind properties

