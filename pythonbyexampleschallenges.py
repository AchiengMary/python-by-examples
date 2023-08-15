#Challenge 1

#name=input('Input your name:')
#print('Hello,' + name)

#2

#name1=input('Input first name')
#name2=input('Input second name')
#print('Hello ' + name1 + name2)

#3

#joke=input('What do you call a bear with no teeth? \n Gummy bear!')

#4

#num1=int(input('Input a number: '))
#num2=int(input('input another number: '))
#answer=num1 + num2
#print('ans', answer)

#5

#num1=int(input('Input a number: '))
#num2=int(input('Input a second number: '))
#num3=int(input('Input a third number: '))
#answer1=num1+num2
#answer2=answer1*num3
#print('ans', answer2)

#6

#num1=int(input('Input number of slices of pizza you started with: '))
#num2=int(input('Input number of slices of pizza you have ate: '))
#ans=num1-num2
#print('You have', ans, 'slices of pizza left')

#7

#name=input('Input your name: ')
#age=int(input('Input your age: '))
#age1=(age+1)
#print(name, 'your next birthday you will be', age1)

#8

#num1=int(input('What is the total bill: '))
#num2=int(input('How many diners are there: '))
#ans=num1/num2
#print('Every diner will have to pay', ans, 'dollars')

#9

#days=int(input('Input number of days: '))
#hrs=(days*24)
#mins=(hrs*60)
#secs=(mins*60)
#print(days, 'days has a total of', hrs, 'hours', mins, 'minutes', 'and', secs, 'seconds')

#10

#weight=int(input('Input your weight in kilograms: '))
#ans=(weight*2204)
#print('Your weight in pounds is', ans)

#11

#um2=int(input('Input a number under 10: '))
#ans=num1//num2
#print('num2 goes into num1', ans, 'times')

#If statements


#num1=int(input('input a number: '))
#if num1>10:
    #print('This is over 10')
#elif num1==10:
    #print('This is equal to 10')   
#else:
    #print('This is under 10')

#12

#num1=int(input('Input a number: '))
#num2=int(input('Input another number: '))
#if num1>num2: 
    #print(num1, num2)
#else:
    #print(num2, num1)

#13

#num=int(input('Enter a number that is under 20: '))
#if num>=20:
    #print('Too high')
#else:
    #print('Thank you')

#14

#num=int(input('Enter a number between 10 and 20: '))
#if num<10 or num>20:
    #print('Incorrect')
#else:
    #print('Thank you')

#15

#color=input('Enter your favorite color: ')
#if color=='red' or color=='Red' or color=='RED':
     #print('I like red too')
#else:
     #print('I dont like', color, ', I prefer Red')
#16

#19

#num1=1
#num2=2
#num3=3
#num=int(input('Enter a number between 1, 2 and 3:'))
#elif num==num1:
    #print('Thank you')
#elif num==num2:
    #print('Well done')
#elif num==num3:
    #print('correct')
#else:
    #print('Error message')

#STRINGS

#20

#name=input('Enter your first name: ')
#length=len(name)
#print(length)

#21

#name=input('Enter your first name: ')
#surname=input('Enter your surname: ')
#names=name + surname
#length=len(names)
#print(names)
#print(length)

#22

#name=input('Enter your first name in lowercase: ')
#surname=input('Enter your surname in lowercase: ')
#name1=name.title()
#name2=surname.title()
#print(name1+name2)

#23

#rhyme=input('Enter a nusery rhyme: ')
#length=len(rhyme)
#print(length)
#print(rhyme[0][0])


#24

#word=input('Type in any word: ')
#ans=word.upper()
#print(ans)

#25

#name=input('Enter your first name: ')
#length=len(name)
#if length<=5:
   #surname=input('Enter your surname: ')
    #names=name+surname
    #ans=names.upper()
    #print(ans)
#else:
    #name1=name.lower()
    #print(name1)

#27

#from math import*
#num=float(input('Enter any number with many decimal places: '))
#ans=num*2
#print(round(ans,2))

#29

#import math
#num=float(input('Enter a number that is over 500: '))
#ans=math.sqrt(num)
#print(round(ans,2))

#30

#print(round(math.pi,5))
#print(math.pi)

#31

#num=int(input('Enter the radius of a circle: '))
#ans=math.pi*(num**2)
#print('The circumference of the circle is: ', ans)

#32

#rad=int(input('Enter the radius of a cylinder: '))
#depth=int(input('Enter the depth of a cylinder: '))
#area=math.pi*(rad**2)
#vol=area*depth
#print(round(vol,3))

#33

#num1=int(input('Enter a number: '))
#num2=int(input('Enter another number: '))
#ans1=num1//num2
#ans2=num1%num2
#print(num1, 'divided by', num2, 'is', ans1, 'with', ans2, 'remaining')

#34

#print('1.Square\n2.Triangle\n')

#num=int(input('Enter a number: '))
#if num==1:
    #side=int(input('Enter the length of one of its sides: '))
    #ans1=side*side
    #print(ans1)
#elif num==2:
    #base=int(input('Enter the base of the triangle: '))
    #height=int(input('Enter the height of the triangle: '))
    #ans2=(base*height)/2
    #print(ans2)
#else:
    #print('Please select from available options')

#FOR LOOPS

#for i in range (1,10):
    #print(i)

#35

#name=input('Enter your name: ')
#num=int(input('Enter a number: '))
#for i in range (1,num):
    #print(name)

#36

#name=input('Enter your name: ')
#num=int(input('Enter a number: '))
#for x in range (1,num):
    #for i in name:
        #print(i)

#39

#num=int(input('Enter a number between 1 and 12: '))
#for i in range (1,13):
    #ans=i*num
    #print(ans)

#40

#num=int(input('Enter a number below 50: '))
#for i in range (50,num-1,-1):
    #print(i)

#41

#name=input('Enter your name: ')
#num=int(input('Enter a number: '))
#if num<=10:
    #for i in range (0,num):
        #print(name)
#else:
    #for i in range (0,3):
        #print('Too high')    

#42

#total=0
#for i in range (0,5):
    #num=int(input('Enter a number: '))
    #ans=input('Do you want this number included: (y/n) ')
    #if ans=='y':
        #total=total+num
        #print(total)

#43

#direction=input('Which direction do you want to count, up/down: ')
#if direction=='up':
    #num=int(input('Enter a number: '))
    #for i in range (1,num+1):
        #print(i)
#elif direction=='down':
    #num=int(input('Enter a number below 20: '))
    #for i in range (20,num-1,-1):
        #print(i)
#else:
    #print('I dont understand')

#44

#num=int(input('How many people do you want to invite to a party? '))
#if num<=10:
    #for i in range (0,num):
        #name=input('Enter a name: ')
        #print(name,' has been invited to the party')
        
#else:
    #print('Too many people')        

#WHILE LOOPS

#again='yes'
#while again=='yes':
    #print('Hello')
    #again=input('Do you want to loop again? ')

#total =0
#while total<100:
    #num=int(input('Enter a number: '))
    #total=total+num
    #print('The total is ', total)

#45

#total=0
#while total<50:
    #num=int(input('Enter a number: '))
    #total=total+num
    #print('Total is ', total)

#47

#num1=int(input('Enter a number: '))
#total=num1
#response='yes'
#while response=='yes':
    #num2=int(input('Enter another number: '))
    #total=total+num2
    #response=input('Do you want to enter another number? (yes/no)')
#print('The total is ', total)     

#48

#again='yes'
#count=0
#while again=='yes':
    #name=input('Who do you want to invite to a party? ')   
    #print(name, 'has now been invited to the party.')
    #count=count+1
    #again=input('Do you want to invite somebody else? yes or no: ') 
    #print('You have', count, 'people coming to your party.')

#Randoms
#52

#import random
#num=random.randint(0,100)
#print(num)

#53
'''
fruit=random.choice(['apple', 'banana', 'oranges', 'avocado', 'mango', 'pineapples'])
print(fruit)
'''
#54
'''
toss=random.choice(['Heads', 'Tails'])
user=input('Guess from the coin toss, heads or tails? ')
if user==toss:
    print('You win!')
else:
    print('Bad luck')
    print('The correct choice is ', toss)
'''
#55

'''
num=random.choice([1,2,3,4,5,6,7,8,9,10])
user=int(input('Enter a number between  1 and 10: '))
if user==num:
    print('Well done champ!')
else: 
    if user>num:
        print('Too high')
    elif user<num:
        print('Too low')
user2=int(input('Give it another try: '))
if user2==num:
    print('Well done you')
else:
    print('You lose')   
'''
#56

'''
import random
num=random.randint(1,10)
correct=False
while correct==False:
    guess=int(input('Enter a number between 1 and 10: '))
    if guess==num:
        correct=True
'''

#57

'''
import random
score=0
print('This is an addition test consisting of 5 questions.\nThe questions are as follows: ')
for i in range (0,5): 
    num1=random.randint(1,1000)
    num2=random.randint(1,1000)
    ans=num1+num2
    print('Number 1: Add ', num1, 'with ', num2)
    youranswer=int(input('Enter your answer: '))
    if youranswer==ans:
        score=score+1
print('Your total score is ', score, 'out of 5')
'''
    
#59

'''
import random
color=random.choice(['red', 'blue', 'yellow', 'green', 'black'])
choic=input('Pick a color between red, blue, yellow, green and black: ')
if choic==color:
    print('Well done artist!')
elif choic!=color and color=='red':
    print('Well guess whose tears will start turning red now')
elif choic!=color and color=='blue':
    print('Dont look so blue, you\'ll get it next time')
elif choic!=color and color=='yellow':
    print('Why are you so yellow when you can\'t even guess a color right')
elif choic!=color and color=='green':
    print('Look at you, you are greener than the grinch right now, i wish I could snap a picture of you')
elif choic!=color and color=='black':
    print('Your knuckles black, your brain blank...')
'''

#  TURTLE GRAPHICS

'''
import turtle
turtle.shape('turtle')
for i in range (0,5):
    turtle.forward(100)
    turtle.right(72)
turtle.exitonclick()
'''
'''
import turtle
for i in range (0,10):
    turtle.right(36)
    for i in range (0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.exitonclick()
'''
'''
import turtle
for i in range (0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()
'''
#61
'''
import turtle
for i in range (0,3):
    turtle.forward(100)
    turtle.right(120)
turtle.exitonclick()
'''

#62
'''
import turtle
for i in range (0,360):
    turtle.forward(1)
    turtle.right(1)
turtle.exitonclick()
'''
#63
'''
import turtle
turtle.color('blue', 'orange')
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(50)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(70)

turtle.pendown()
turtle.color('green', 'pink')
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.forward(70)
turtle.pendown()

turtle.color('red', 'black')
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
'''
#64
'''
import turtle
for i in range (0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()
'''

#65
'''
import turtle
import random
turtle.pensize(4)
for i in range (0,8):
    turtle.color(random.choice(['red', 'yellow', 'blue', 'black', 'orange','pink', 'green', 'violet']))

    turtle.forward(100)
    turtle.right(45)

turtle.exitonclick()
'''

#67
'''
import turtle
for i in range (0,10):
    turtle.right(36)
    for i in range (0,8):
        turtle.forward(50)
        turtle.right(45)
turtle.exitonclick()   
'''
#68
'''
import turtle
import random
lines=random.randint(5,10)
for i in range (0,lines):
    
    angle=random.randint(30,90)
    turtle.forward(100)
    turtle.right(angle)
turtle.exitonclick()      
'''    

#TUPLES, LISTS AND DICTIONARIES

#69
'''
countries_tuple=('Kenya', 'Australia', 'New Zealand', 'Iceland', 'South Africa')
print(countries_tuple)
user=input('Enter one of the countries in the tuple: ')
print(countries_tuple.index(user))
num=int(input('Enter a number: '))
num1=countries_tuple[num]
print('At position ', num, 'the coutry is ', num1)
'''    

#71
'''
sport_list=['Football', 'Basketball']
sport_list.append(input('What is your favorite sport? '))
print(sorted(sport_list))
'''
#72

subject_list=['Analogue electronics', 'Statistics', 'Calculus', 'Game theory', 'Geometry', 'Algebra']
ans=int(input('Which of the subjects in ', subject_list , 'do you not like? '))
del subject_list[ans]
