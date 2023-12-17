"""
the mastermind model for lab 2 of Object Oriented Programming
Group 48: Stan Ferguson (S4674367), Jelle Molenaar (S4807243)
"""

import numpy as np

import sys
sys.path.append("tests")
from tests import testFile
from typing import List

tests = testFile.Tests()

# starting the program, we provide the user with the rules and let them input the amount of turns that is allowed.
print("""
Welcome to this coded version of mastermind. The rules are as follows:
\n the computer will generate a 4-color code that you need to break. Every turn, you can propose a combination of 4 colors and the computer will respond with:
\n \t1. The amount of colors that are correct and in the right place (if any).
\n \t2. The amount of colors that are correct but in the wrong place (if any).
\n It will NOT tell you which of the colors you proposed are correct. Note that colors can be used multiple times.
\n 4. The possible colors (with corresponding inputs) are: White 'w', Black 'k', Yellow 'y', Green 'g', Red 'r' and Blue 'b'.
\n An example input could be: "wygb"
\n\n Now, please enter the amount of turns that you would like as the limit (you could start with 20 if you don't know):
""")

#taking the limit and testing it's type and value
limit = int(input())
tests.test_limit_input_type(limit)
tests.test_limit_input(limit)
print("The limit has been set to: ", limit)

# all valid inputs for the codes
valid = ['w', 'k', 'y', 'g', 'r', 'b']

def create_target(valid: List[str]):
    target = ['', '', '', '']
    for i in range(len(target)):
        target[i] = valid[np.random.randint(0, 6)]
    return target

# creating our target code and testing it
target = create_target(valid)
tests.test_target_length(target)
tests.test_target_inputs(target)

print("The code has been generated, good luck with cracking it. Enter your first proposal:")

def found_solution(proposal, target):
    for i in range(len(proposal)):
        if proposal[i] != target[i]:
            return False
    return True

def evaluate_proposal(proposal,target):
    amountCorrect = 0
    newTarget = ['', '', '', '']
    newProposal = ['', '', '', '']
    for i in range(len(target)):
        newTarget[i] = target[i]
        newProposal[i] = proposal[i]

    for i in range(len(target)):
        if proposal[i] == target[i]:
            del newTarget[i - amountCorrect]
            del newProposal[i - amountCorrect]
            amountCorrect += 1
  
    amountWrong = 0
    idx = 0
    while idx < len(newProposal):
        for k in range(len(newTarget)):

            if newProposal[idx] == newTarget[k]:
                del newTarget[k]
                amountWrong += 1
                break
        idx += 1
    
    tests.test_correct_positions(amountCorrect, target,proposal)
    tests.test_wrong_positions(amountWrong, target,proposal)
    # printing the outcome:
    print("The outcome of your first guess is as follows: \n Amount of colors in the right place: \t", amountCorrect, "\n Amount of colors in the wrong place: \t", amountWrong)

proposal = list(input())
tests.test_proposal_inputs(proposal)
tests.test_proposal_length(proposal)

iterations = 1
while not found_solution(proposal, target) and iterations < limit:
    # making sure we did not exceed the limit
    tests.test_exceeded_limit(iterations, limit)

    # doing the evaluation and returning the values for right and wrong colors
    evaluate_proposal(proposal, target)

    # taking in a new proposal
    proposal = list(input())
    tests.test_proposal_inputs(proposal)
    tests.test_proposal_length(proposal)

    iterations += 1

if found_solution(proposal, target):
    tests.test_found_solution(target, proposal)
    print("----------WON----------\n Congratulations, you have found the winning solution within the turn limit!")
    print("The final solution was indeed: ", target[0], target[1], target[2], target[3])
else:
    print("\n \n----------LOST---------- \n Unfortunately, the turn limit has been reached and you have not found the solution. \n Consider trying again with a higher turn limit.")
    print("the final solution was: ", target[0], target[1], target[2], target[3])
print("\n")