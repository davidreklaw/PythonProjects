"""
Python Script for creating the necessary tables
"""

import numpy as np

def create_q_table():
    """
    Creates the initial q-table
    """
    q_values = np.zeros((5,10,4))
    return q_values

def create_rewards():
    """
    Creates a matrix for all the rewards for the map
    """
    rewards = np.full((5,10), 0.)

    rewards[0,5] = -10
    rewards[0,6] = -10
    rewards[0,9] = 1500
    rewards[1,2] = 25
    rewards[1,3] = -10
    rewards[2,3] = -50
    rewards[2,4] = -10
    rewards[2,5] = -10
    rewards[2,7] = -10
    rewards[3,3] = -50
    rewards[3,7] = -50
    rewards[4,1] = -10
    rewards[4,3] = -10
    rewards[4,7] = -10

    for row in rewards:
        print(row)

    return rewards
