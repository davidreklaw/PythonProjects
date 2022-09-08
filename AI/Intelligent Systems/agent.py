"""
Python Script for the learning agent

Insperation from:
alyticsvidhya.com/blog/2021/04/q-learning-algorithm-with-step-by-step-implementation-using-python/
"""

import numpy as np
import table_creator

ACTIONS = ['up', 'right', 'down', 'left']

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1

GOAL = 1500
DEATH = -50

ENVIRONMENT_ROWS = 5
ENVIRONMENT_COLUMNS = 10

CORNERS = [[0,0], [0,9], [4,0], [4,9]]



def is_terminal_state(current_row_index, current_column_index, rewards):
    """
    Determines if the given position is a reset point
    """
    return rewards[current_row_index, current_column_index] in [GOAL, DEATH]

def get_next_action(current_row_index, current_column_index, q_values, epsilon):
    """
    Determines the next action to take
    """
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_column_index])
    return np.random.randint(4)

def get_next_location(current_row_index, current_column_index, action_index):
    """
    Moves Wolfie to the next location
    """
    new_row_index = current_row_index
    new_column_index = current_column_index
    if ACTIONS[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif ACTIONS[action_index] == 'right' and current_column_index < ENVIRONMENT_COLUMNS - 1:
        new_column_index += 1
    elif ACTIONS[action_index] == 'down' and current_row_index < ENVIRONMENT_ROWS - 1:
        new_row_index += 1
    elif ACTIONS[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1
    return new_row_index, new_column_index

def get_shortest_path(start_row_index, start_column_index, rewards, q_values):
    """
    Gets the shortest path from the given starting position
    """
    if is_terminal_state(start_row_index, start_column_index, rewards):
        return []
    current_row, current_column = start_row_index, start_column_index
    shortest_path = []
    shortest_path.append([current_row, current_column])
    while not is_terminal_state(current_row, current_column, rewards):
        action = get_next_action(current_row, current_column, q_values, 1.)
        current_row, current_column = get_next_location(current_row, current_column, action)
        shortest_path.append([current_row, current_column])
        if len(shortest_path) == 20:
            return shortest_path
    return shortest_path

def train(q_values, rewards):
    """
    Trains the with the given number of episodes
    """
    episodes = int(input("How many episodes would you like?"))

    for _ in range(episodes):
        row_index, column_index = 3,0
        while not is_terminal_state(row_index, column_index, rewards):
            action_index = get_next_action(row_index, column_index, q_values, EPSILON)
            old_row_index, old_column_index = row_index, column_index
            row_index, column_index = get_next_location(row_index, column_index, action_index)
            reward = rewards[row_index, column_index]
            old_q_value = q_values[old_row_index, old_column_index, action_index]
            max_value = np.max(q_values[row_index, column_index])
            temporal_difference = reward + (GAMMA * max_value) - old_q_value
            new_q_value = old_q_value + (ALPHA * temporal_difference)
            q_values[old_row_index, old_column_index, action_index] = new_q_value
    print('Training complete!')

def run():
    """
    Runs  the algorithm for running training the agent and finding a path
    """
    q_values = table_creator.create_q_table()
    rewards = table_creator.create_rewards()

    np.random.seed(0)

    train(q_values, rewards)

    print(get_shortest_path(3,0, rewards, q_values))
