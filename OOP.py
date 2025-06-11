class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #Intro Function

    def intro(self):
        print("hello, I am", self.name)

# Object Creation Of Fruit

apple = fruit('Apple', 'Red')

# Calling Function Intro

apple.intro()

#obj

obj = fruit('Banana', 'Yellow')
obj.intro()
#   