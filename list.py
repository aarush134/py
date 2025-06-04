fruits = ["Apple", "Banana", "Orange", "Mango", "Litchi"]

length = len(fruits)

print(length)

first_fruit = fruits[0]

print(first_fruit)

last_fruit = fruits[-1]

print(last_fruit)

fruits.append("Guava")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

lst1 = fruits[:3]
print(lst1)

print(fruits*2)

num = [12, 16, 17, 2012, 8, 31]

print(num)

add = [n+3 for n in num]

print(add)