####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
from random import randint;
team_name = 'BiLasagnash' # Only 10 chars displayed.
strategy_name = 'All choices are bad choices.'
strategy_description = '10 minutes later...'
    
def move(my_history, their_history, my_score, their_score):
    bs, cs = 0
    if len(their_history) >= 1: # Make sure they have a history
        for i in their_history: # Root throught their history
            if i == 'b':
                bs = bs + 1;
            else:
                cs = cs + 1;
        tot = bs+cs;        # Total out betrays and colludes
        if cs/tot > bs/tot: # Figure out if they betray more, or collude more
            return 'c';
        else:
            return 'b';
    else:                     # If they don't have a history...
        coin =  randint(1,2); # Flip a 'coin'
        if coin == 1:
            return 'b';
        else:
            return 'c';
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             