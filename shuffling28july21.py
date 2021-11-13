import random # random contain 'shuffle' used to shuffle our list
def word_spelling():
    print('HELLO, WELCOME TO THE WORD SPELLING GAME:')
    print('SPELL AS MUCH NUMBERS AS YOU CAN TO GET MARKS')
    print('-----------------------------------------------')
 
    correct_score = 0  # keep record of correct spellings
    wrong_score = 0    # keep record of wrong spellings exceeding number of trials
    max_trials = 3     # maximum number of trials
 
    # A dictionary of numbers as keys and spellings as values. This can be expanded to increase its level of difficulty.
 
    number_spell = [1,2,3,4,5,6,7,8,9,10]
 
    # get the list of keys from the dict and shuffle them so that random numbers are displayed on the screen.
    number_spell_keys = list(number_spell.keys())
    random.shuffle(number_spell_keys)
 
    # Our game starts here
    for number in number_spell_keys:
        # outer loop is a for loop which iterate through the keys
 
        trial_count = 0 # keeps track of number of trials
        while trial_count< max_trials:
            # inner loop is a while loop that checks if number of trials by the user exceeded the max
            # get user input
            spelling = input(random.format(number))
            if spelling.lower() == number_spell[number]:
                # if user got it right, increment it's score and break out of the outer loop
                correct_score += 1
                break
            else:
                # if not, increment number of trials and ask the user to try again
                trial_count += 1
                print('Incorrect spelling')
         
        else:
            # if while loop condition fails, increment wrong score and quit the inner loop
            print('Sorry! Number of trials Exceeded&quot;')
            wrong_score += 1
 
        print('-------------------')
        print('CORRECT SPELLING SCORE:', {})
        print('WRONG SPELLING SCORE:', {})
if __name__ == '__main__':
    word_spelling()