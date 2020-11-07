import random

print("1.1 random number without a seed between a range of two numbers - Both Integer")
print (random.randint(2,25))
print("1.2 random number without a seed between a range of two numbers - Both decimal")
print (round(random.uniform(2.5,4.7)),2)
print("2.1 Generate a random number with a seed between a range of two numbers - Both Integer")
random.seed(27)
print (random.randint(2,25))
print("2.2 Generate a random number with a seed between a range of two numbers - Both Decimal")
random.seed(27)
print (round(random.uniform(2.7,5.7)),2)
print("3.1 Generate a list of N random numbers with a seed and between a range of numbers - Both Integer")
randomIntList = []
for i in range(0, 10):
    # any random float between 50.50 to 500.50
    # don't use round() if you need number as it is
    random.seed(i)
    x = random.randint(0,25)
    randomIntList.append(x)

print("Printing list of 10 random int numbers :",randomIntList)

print("3.2 Generate a list of N random numbers with a seed and between a range of numbers - Both decimal")
randomFloatList = []
for i in range(0, 10):

    random.seed(i)
    x = round(random.uniform(0.0,25.5),2)
    randomFloatList.append(x)

print("Printing list of 10 random decimal numbers :",randomFloatList)
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
# sampling = random.choices(numberList1, k=5)
# print("Randomly selected multiple choices using random.choices() ", sampling)


