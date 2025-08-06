import random
class fruitquiz:
    def __init__(self):
        self.fruits = {'apple':'red','banana':'yellow','orange':'orange','watermelon':'green'}
    def quiz(self):
        while (True):
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of{}".format(fruit))
            user_answer = input()
            if (user_answer.lower()==color):
                print("correct answer")
            else:
                print("Wrong answer")
            option = int(input("enter zero if u want to play again else 1"))
            if(option):
                break
print("Welcome to fruit quiz")
fq = fruitquiz()
fq.quiz()