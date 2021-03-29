scrabble_dict = {
                  1:['a','e','i', 'l', 'n', 'o', 'r', 's', 't', 'u',],
                  2:['d', 'g'],
                  3:['b', 'c', 'm', 'p'],
                  4:['f', 'h', 'v', 'w', 'y'],
                  5:['k'],
                  8:['j', 'x'],
                  10:['q', 'z'],
                }

score = 0

def score_check(str, dict):
    """Takes in a string and a dictionary as arguments and computes the score. also set the score scope to global """
    global score
    for lt in str:
        for key, values in dict.items():
            if lt in values:
                score += key


while True:
    print("\nEnter 'end' to quit.")
    inp_1 = input("Enter a word and the program will tell you the score in scrabble\n").lower().strip()
    if inp_1.lower() == 'end':
        break
    score_check(inp_1, scrabble_dict)
    print(f"The total score for the word '{inp_1}' is {score}\n")
    score = 0
