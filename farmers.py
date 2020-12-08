'''
The explanation denotes that D# means 'starts in D# days'.

So, if today is day 0, and D# is 3:
day 0: no rate (starts in three days)
day 1: no rate (starts in two days)
day 2: no rate (starts in one day)
day 3: rate    (starts today)


However the explanation of the example problem says
the first two days have no rate, and that the third
does. This made me think that the 'starts in D# days'
part of the question actually meant, 'starts on day D#'

But the problem set to test for includes 0 as value for
D. This seems somewhat contradictory, so for reference,
I am assuming that Loans begin today if D == 0. If not,
this changes the output of that problem by 1.
'''


def get_days_of_power(R1,D1,R2,D2,R3,D3,k):
    
    # Not necessary, but for readability
    loans = [
            {'day': D1, 'rate': R1},
            {'day': D2, 'rate': R2},
            {'day': D3, 'rate': R3}
    ]

    rate = 0
    today = 0 
    days_on = 0
    while k >= rate:

        # removes loans if their rates have been added to prevent unnecessary checks
        for loan in loans[:]:
            if today == loan['day']:
                rate += loan['rate']
                loans.remove(loan)
        
        # k must afford the rate, and the rate must be greater than 0
        if k >= rate and rate > 0:
            k -= rate
            days_on += 1
        
        # increment day
        today += 1

    return days_on

# Test for the example problem
print('Example Problem')
a = get_days_of_power(1000,3,500,10,1500,7,21000)
print(a)

# I presumed problems being given as a list of lists.
# Could be used with other functions and sets

# The unit testing I am used to for APIs generally entails having a desired outcome
# and asserting that it is equal to the outcome of the function. I am assuming that
# you just wanted me to automate the problems, let me know if you want me to do this
# differently.

def test_function(problem_set, func):
    return([func(*problem) for problem in problem_set])

problems = [
        [3000,3,500,10,1500,7,700000],
        [500,3,500,10,500,7,21000],
        [1300,0,500,0,1500,7,10000],
        [10000,3,500,10,1500,7,11000]
        ]

print('Problem set')
print(test_function(problems, get_days_of_power))


