from random import randint
outer_count = 0
while outer_count < 5:
    num1 =3 #TODO generate a rando number from 1 to 10
    num2 = 8#TODO generate another rando number from 1 to 10
    product = num1 * num2
    print(f"Question {outer_count + 1}: What is {num1} x {num2}?")
    inner_count = 0
    while inner_count < 5:
        guess =5 #TODO: get from user input and int
        print(f"You answer: {guess}")
        if guess == product:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            inner_count += 1
    outer_count += 1