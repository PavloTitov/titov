#1 задача
for i in range(7,30,7):
    print('i=', i) 
#2 задача
count=0
for i in range (0,30):
    print('i=', i)
print()
for i in reversed(range (0,30)):
    print('i=', i)
print()
for i in range(0,30):
    if i % 7== 0:
        print('i=', i)
print()
for i in range(0,30):
    if i % 5 ==0:
        count +=1
print(count)
#3 задача
count=0
for i in range(0,50):
    if i%7==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

