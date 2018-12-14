####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Disappointments' # Only 10 chars displayed.
strategy_name = 'Low expectation'
strategy_description = 'Dont expect too much from us'
import random    
def move(my_history, their_history, my_score, their_score): 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1==dice2:
        return 'c'
    else:
        return 'b' 
        
move('','',0,0)
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
