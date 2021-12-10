# Pseudocode:

# Take a current state of the puzzle
# iterate through every entry(variables) to generate constraints
# if there are any with 0 possible values, return an error
# elif there are any with 1 possible value, set variable to value
# I guess technically at this point, the algorithm should break and re-evaluate constraints,
# but I would like to set all possible values before re-evaluating constraints, because
# I hypothesize that it doesn't really matter.
# if there is somehow a scenario with multiple possible values, do a search somehow, but let's
# only do puzzles with unique solutions and unique steps for now, which I think is a large
# set of sudoku problems

import numpy as np

"""I may choose to represent the initial state later as a .csv and convert it to a numpy array, but for now, I choose
it to be a 2x2 numpy array that I manually define in the code."""

initial_state = np.array([
    [3, 0, 5, 4, 0, 2, 0, 6, 0],
    [4, 9, 0, 7, 6, 0, 1, 0, 8],
    [6, 0, 0, 1, 0, 3, 2, 4, 5],
    [0, 0, 3, 9, 0, 0, 5, 8, 0],
    [9, 6, 0, 0, 5, 8, 7, 0, 3],
    [0, 8, 1, 3, 0, 4, 0, 9, 2],
    [0, 5, 0, 6, 0, 1, 4, 0, 0],
    [2, 0, 0, 5, 4, 9, 0, 7, 0],
    [1, 4, 9, 0, 0, 7, 3, 0, 6]
])


def update_constraints(state):
    current_state = np.copy(state)
    for row in range(len(current_state)):
        for column in range(len(current_state[:, ])):
            current_entry = current_state[row, column]
            if current_entry != 0:
                print(True)



def main():
    current_state = np.copy(initial_state)
    update_constraints(current_state)


if __name__ == "__main__":
    main()
