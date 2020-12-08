import datetime


print("Hello world!")
now = datetime.datetime.now()
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))

i = 0
numberArray = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numberArray)  + 1):
    print(numberArray[i])
    i += 1
