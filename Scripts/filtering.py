from config import *
from dependencies import *


def filter_tradeLines(support, resistance, tolerance):
    # Sort the support and resistance lists
    support.sort()
    resistance.sort()

    # Create new lists for the filtered support and resistance values
    new_support = list()
    new_resistance = list()

    # Iterate over the support list and add values to the new_support list if they meet the tolerance criteria
    for i in range(1, len(support)):
        if (support[i] - support[i-1] >= tolerance):
            new_support.append(support[i])

    # Iterate over the resistance list and add values to the new_resistance list if they meet the tolerance criteria
    for i in range(1, len(resistance)):
        if (resistance[i] - resistance[i-1] >= tolerance):
            new_resistance.append(resistance[i])

    # Return the filtered support and resistance lists
    return new_support, new_resistance



        