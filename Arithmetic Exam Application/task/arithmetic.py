# write your code here
import random
import time


def welcome():
    """
    prints astarting welcome and introduction to the text
    :return: boolean value for playing. if true the program loop will continue
    else the program will exit
    """
    global user_name
    for symbol in range(70):
        print("*", end="")
    print()
    if user_name == "":
        print("'Hello user.'")
        print(".......")
        print("(-)x(-)")
        print("  ___  ")
        print()
        print("'Welcome to the arithmetic test.'")
        print("'I am your invigilator...'")
        print("'and who might you be?'")
        user_name = input("enter your name...")
        return True
    else:
        print(f"'Welcome {user_name}. Good luck!'")
        print()
        print(".......")
        print("(-)x(-)")
        print(" -___- ")
        print()
        print("'Oh, and remember, if you want to leave you can type exit now!'")
        print("'Otherwise... lets get on with it!")
        escape = input("press enter to continue or type exit to leave")
        if escape == "exit":
            running = False
        else:
            running = True
        return running


def get_difficulty():
    """
    Prompt user to enter difficulty
    :return: difficulty level
    """
    print("Which level do you want? Enter a number:")
    global levels
    for L in levels:
        print(f"{L} - {levels[L]}")
    level_chosen = False
    while not level_chosen:
        choose_level = input()
        try:
            choose_level = int(choose_level)
            assert (1 <= choose_level <= len(levels))
            return choose_level
        except (AssertionError, ValueError):
            print("Incorrect format.")


def level_1():
    """
    create a simple math operation with numbers between 2 and 9
    print this operation as a string
    :return: the question value
    """
    global score
    int_1 = random.randint(2, 9)
    int_2 = random.randint(2, 9)
    operations = "+", "-", "*"
    operands = random.choice(operations)
    if operands == "+":
        question = int_1 + int_2
    elif operands == "-":
        question = int_1 - int_2
    else:
        question = int_1 * int_2
    print(f"{int_1} {operands} {int_2}")
    return question


def level_2():
    """
    create a math operation where integers between 11 and 29 are squared
    print this operation as a string
    :return: the question value
    """
    global score
    int_1 = random.randint(11, 29)
    question = int_1 ** 2
    print(f"{int_1}")
    return question


def level_3():
    """
    prints a number of lines describing an algebra problem
    and requesting the solution for x or y
    :return:the question value
    """
    global score
    global score
    alg_dict = {
        "x": random.randint(5, 24),
        "y": random.randint(5, 24),
        "z": random.randint(5, 24)
    }
    everydayimshuff = ["x", "y"]
    random.shuffle(everydayimshuff)
    guess = everydayimshuff[0]
    clue = everydayimshuff[1]
    int_1 = alg_dict["y"] + alg_dict["x"]
    int_2 = alg_dict["y"] * alg_dict["x"]
    int_3 = alg_dict["z"] - alg_dict[clue]
    int_4 = alg_dict["z"] - alg_dict[guess]
    print(f"x + y = {int_1}")
    print(f"y * x = {int_2}")
    print(f"z - {clue} = {int_3}")
    print(f"z - {guess} = {int_4}")
    print(f"{guess} = ")
    return alg_dict[guess]


def level_4():
    """
    prints a string that contains a problem where the cost of an item is
    reduced by a percentage
    :return: the question value
    """
    global score
    int_1 = random.choice([5, 10, 20, 25, 30, 40])
    int_2 = random.randint(101, 999)
    question = round(int_2 - (int_2 * int_1 / 100))
    print(f"£{int_2} is reduced by {int_1}%. what is the new price to the nearest whole number?")
    return question


def get_response(question):
    """
    asks the user for a response to the question allowing for typos to
    be corrected
    :param question: the computer generated question goes here
    :return: N/A
    """
    global score
    guessed = False
    while not guessed:
        try:
            answer = int(input())
            if answer == question:
                print("Right!")
                guessed = True
                score += 1
            else:
                print("Wrong!")
                guessed = True
        except ValueError:
            print("Incorrect format.")


def now_get_saved(difficulty, test_length, score, speed):
    """
    ask the user if they want to save their score.
    if so request their name for the records
    save the score to results.txt
    :param difficulty: the difficulty level selected by user
    :param test_length: the number of tasks set
    :param score: the users final score
    :param speed: time taken to complete
    :return:
    """
    global user_name
    print("Would you like to save your result to the file? Enter yes or no.")
    save = input()
    i_want_to_save = "YES", "Yes", "yes", "y"
    if save in i_want_to_save:
        name = user_name
        data = str(f"{name}: {score}/{test_length}. "
                   f"completed in {speed} in level {difficulty} ({levels[difficulty]})\n")
        file = open("results.txt", "a")
        file.write(data)
        file.close()
        print('The results are saved in "results.txt".')


def start_timer():
    """
    this function starts the timer
    :return: N/A global variables used
    """
    global time_started
    time_started = time.time()


def time_passed(time_started):
    """
    :return: time passed since test started
    """
    time_now = time.time()
    timer = int(time_now - time_started)
    return timer


def get_results(difficulty, test_length, score, speed):
    """
    print results for the user and analyse their score against existing saved scores
    :return:
    :param difficulty: the difficulty level selected by user
    :param test_length: the number of tasks set
    :param score: the users final score
    :param speed: time taken to complete
    """

    print()
    print(".......")
    print("(-)x(-)")
    print(" -___- ")
    print()
    print(f"'Your mark is {score}/{test_length}.'")
    accessing_past_scores = open("results.txt", "r")
    past_scores = accessing_past_scores.read().split("\n")
    scores = []
    for ps in past_scores:
        name = ps.split(":")
        slist = name[1].split("/")
        scores.append(int(slist[0]))
    if max(scores) <= score:
        print("'That's a great score!'")
    elif sum(scores) / len(scores) <= score:
        print("'that's better than average.'")
    else:
        print("'looks like that could be improved!'")
    print()
    print(f"'You completed the test in {speed} seconds")
    if speed < 180:
        print("'Wow that's fast!'")
    elif speed >= 300:
        print("'looks like you ran out of time!'")
    if score < test_length / 2:
        if difficulty > 1:
            print("'perhaps you could choose an easier difficulty?")
    elif score > test_length / 2:
        if difficulty < 5:
            print("'perhaps you could do with more of a challenge?")


# Variables ------------------------------------------------------
levels = {
    1: "simple operations with numbers 2-9",
    2: "integral squares of 11-29)",
    3: "algebra",
    4: "percentages",
    }

score = 0
test_length = 5
time_started = 0.0
user_name = ""

# Programme loop ---------------------------------------------------
playing = welcome()
while playing:
    playing = welcome()
    difficulty = get_difficulty()
    start_timer()
    for t in range(test_length):
        if difficulty == 1:
            task = level_1()
            get_response(task)
        elif difficulty == 2:
            task = level_2()
            get_response(task)
        elif difficulty == 3 :
            task = level_3()
            get_response(task)
        else:
            task = level_4()
            get_response(task)
    speed = time_passed(time_started)
    get_results(difficulty, test_length, score, speed)
    now_get_saved(difficulty, test_length, score, speed)

