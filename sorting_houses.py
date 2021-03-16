# This code is my variable for the four houses
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

def my_function(answers):
    print("+=", )


# listOfQuestions = [{"question":"this is question 1", "gryffindor" :{"score1": 1, "option": "pic him up"},"ravenclaw": 2, "options"[ "option1", "option2"], {"question":"this is question 2", "gryffindor" :1,"ravenclaw": 2}]

# make a list of two questions with options and scores for each house

# for loop for list

# display question and options (consider putting options in random order)

# add score to the variables up top based on user's anser (get from input)

#at end, display what house they are sorted in

# ask them if they want to go again


#dictionary = {"question:""what to do", "gryffindor" :1,"ravenclaw": 2}



def add(a, b):
    return a+b


q1_answer = input("Will you break the rules to help a friend? \na) yes \nb no \nc) maybe \nd) get lost")
if q1_answer == "a":
    gryffindor += 1
elif q1_answer == "b":
        ravenclaw += 1
elif q1_answer == "c":
    hufflepuff += 1
elif q1_answer == "d":
    slytherin += 1
else: print("Sorry, I don't understand that answer.")        


q2_answer = input("How do you describe yourself? \na) brave \nb) timid \nc)superstar \nd)best of the best")
if q2_answer == "a":
    gryffindor += 1
elif q2_answer == "b":
        ravenclaw += 1
elif q1_answer == "c":
    hufflepuff += 1
elif q2_answer == "d":
    slytherin += 1
else: print("Sorry, I don't understand that answer.")   

q3_answer = input("If you see a deatheater, what will you do? \na) fight \b) run \c) get help \d)run like crazy")