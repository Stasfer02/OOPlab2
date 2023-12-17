"""
This is the test file for lab 2 of Object Oriented Programming.
Group 48: Stan Ferguson (S4674367), Jelle Molenaar (S4807243)

Structure of the input:
there are 6 possible colors: White (w), Black (k), Yellow (y), Green (g), Red (r), Blue (b)
--- duplicates are allowed ---

Codemaker (e.g. the computer), creates a code that needs to be broken. TEST
"""

import unittest
from typing import List

class Tests(unittest.TestCase):
    # test class
    def test_target_length(self, x: List[str]):
        # testing if the code is 4 inputs
        self.assertIs(len(x), 4, "The target code is not of length 4.")

    def test_target_inputs(self, x: List[str]):
        valid = ['w', 'k', 'y', 'g', 'r', 'b']
        for i in x:
            self.assertIn(i, valid, "The target code does not contain valid inputs.")

    def test_proposal_length(self, x: List[str]):
        self.assertIs(len(x), 4, "the proposal code is not of length 4.")

    def test_proposal_inputs(self, x: List[str]):
        valid = ['w', 'k', 'y', 'g', 'r', 'b']
        for i in x:
            self.assertIn(i, valid, "the proposal code does not contain valid inputs.")

    def test_exceeded_limit(self, iterations: int, limit: int):
        self.assertLess(iterations, limit, "The limit of iterations was exceeded.")

    def test_correct_positions(self, correctPosition: int, target: List[str], proposal: List[str]):
        amount = 0

        for i in range(len(target)):
            if target[i] == proposal[i]:
                amount += 1
        self.assertEqual(amount, correctPosition, "The calculated amount of correct positions is not correct.")

    def test_wrong_positions(self, wrongPosition: int, target: List[str], proposal: List[str]):
        # we need to remove the correct positions first, otherwise we get false returns. for example:
        # if the target is ['w','r','b','b'] and the proposal is ['r','w','r','r'] it should not return 3 wrong positions for
        # all 'r' in the proposal, but only one. So we first remove the correct positions,
        # then we remove target values if they have been predicted.
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
        self.assertEqual(amountWrong, wrongPosition, "The calculated amount of wrong positions is not correct.")

    def test_found_solution(self, target: List[str], proposal: List[str]):
        correct = 0
        for i in range(len(target)):
            if target[i] == proposal[i]:
                correct += 1
        self.assertEqual(correct, 4, "the found solution is not the correct solution.")

    def test_limit_input_type(self, limit):
        self.assertIsInstance(limit, int, "input variable is not an integer.")

    def test_limit_input(self, limit: int):
        # the maximum attempts is variable, but has to stay below 100
        self.assertLess(limit, 100, "the limit boundary exceeds the maximum value of 100.")
