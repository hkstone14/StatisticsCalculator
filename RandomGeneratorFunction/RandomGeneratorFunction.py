import random

print("Generate a random number without a seed between a range of two numbers - Both Integer and Decimal")

print("1.1 Both Integer : ",random.randint(2,25))

print("1.2 Both decimal : ",round(random.uniform(2.5,4.7),2))

print("2 Generate a random number with a seed between a range of two numbers - Both Integer and Decimal")

random.seed(27)
print("2.1 Both Integer : ",random.randint(2,25))

random.seed(27)
print("2.2 Both Decimal : ",round(random.uniform(2.7,5.7),2))

print("3 Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal")

randomIntList = []
for i in range(0, 10):
    random.seed(i)
    x = random.randint(0,25)
    randomIntList.append(x)
print("3.1 Printing list of 10 random integer numbers : ",randomIntList)

randomFloatList = []
for i in range(0, 10):

    random.seed(i)
    x = round(random.uniform(0.0,25.5),2)
    randomFloatList.append(x)
print("3.2 Printing list of 10 random decimal numbers :", randomFloatList)

print("4. Select a random item from a list")

numberList = [57,21,27,97,25,2]
print("random item from list is: ", random.choice(numberList))

print("5. Set a seed and randomly.select the same value from a list")

numberList = [57,21,27,97,25,2,8,47]
random.seed(4)
random_item = random.choice(numberList)
print("random item with seed : ", random_item)

print("6. Select N number of items from a list without a seed")

randomIntList = []
for i in range(0, 10):
    y = random.randint(15,50)
    randomIntList.append(y)

print("Printing list of 10 random numbers without a seed :",randomIntList)

print("7. Select N number of items from a list with a seed")

numberList1 = [57,21,27,97.6,25,2,8,47,5.8]
randomList = []
for i in range(0, 7):
    random.seed(i)
    x = random.choice(numberList1)
    randomList.append(x)

print("Printing list of N random numbers with a seed :",randomList)



