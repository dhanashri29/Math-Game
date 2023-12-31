print ("*****MATH GAME*****")
print("")

score = 0

print("1. what is 2+2=?")
answer1= input("Enter your answer : ")

if answer1 == "4":
    score+=1
print("")

print("2. what is 2+10*5=?")
answer1= input("Enter your answer : ")

if answer1 == "60":
    score+=1
print("")

print("3. what is 36/2=?")
answer1= input("Enter your answer : ")

if answer1 == "18":
    score+=1
print("")

print("4. what is 50-10=?")
answer1= input("Enter your answer : ")

if answer1 == "40":
    score+=1
print("")

print("5. what is 6 * 12 =?")
answer1= input("Enter your answer : ")

if answer1 == "72":
    score+=1
print("")

print("correct answers are " + str(score) + " out of 5")
 