# to generate random numbers
import random
# a value defined as random numbers between 10 and 99
value=random.randint(10,99)
# a variable defined as random numbers between 10 and 99
a=random.randint(10,99)
#to generate the sum of a and value
sum=value+a
# counts the number of times user gets the correct answer
check=1
# to help execute the codes below
while check<=3:
# help the program generate random integers between 10 and 99
    value=random.randint(10,99)
# help the program generate random integers between 10 and 99
    a=random.randint(10,99)
# help the program add value and a
    sum=value+a
# you are asking the user the summation of value and a
    print("what is", value, "+", a,"?")
# you are asking the user to enter his/her answer
    user_input=int(input("Answer: "))
# if the user input equals the summation
    if user_input==sum:
# the program should user answer is correct 3 times in a row
        print("user answer is correct",check,"times in a row")
# indexing variable
        check+=1
    else:
        check=1
        print("user answer is wrong, the expected answer is ",sum)





