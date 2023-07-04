from dependencies import *
from config import *


def isSupport(dataframe, l, left_slip, right_slip): #left_slip right_slip before and after candle l
    
    # Check if the lows of the candles before the current candle are higher than the current candle's low
    for i in range(l-left_slip+1, l+1):
        if (
            dataframe.low[i]>dataframe.low[i-1]
        ):
            return 0
    
    # Check if the lows of the candles after the current candle are lower than the current candle's low
    for i in range(l+1,l+right_slip+1):
        if (
            dataframe.low[i]<dataframe.low[i-1]
        ):
            return 0
    
    # If both conditions are met, return 1 (True)
    return 1


def isResistance(dataframe, l, left_slip, right_slip): #left_slip right_slip before and after candle l
    
    # Check if the highs of the candles before the current candle are lower than the current candle's high
    for i in range(l-left_slip+1, l+1):
        if (
            dataframe.high[i]<dataframe.high[i-1]
        ):
            return 0
    
    # Check if the highs of the candles after the current candle are higher than the current candle's high
    for i in range(l+1,l+right_slip+1):
        if (
            dataframe.high[i]>dataframe.high[i-1]
        ):
            return 0
    
    # If both conditions are met, return 1 (True)
    return 1


def extract_support_resistance(df, start_index, end_index):
    # Initialize empty lists for support and resistance levels
    support = list()
    resistance = list()

    # Iterate over the specified range of candles in the dataframe
    for i in range(start_index, end_index):
        # Check if the current candle is a support level
        if isSupport(
                        dataframe = df, 
                        l = i, 
                        left_slip = left_slip, 
                        right_slip=right_slip
                ) == True:
            
            # Add the current candle's low value to the support list
            support.append(df['low'][i])

        # Check if the current candle is a resistance level
        if isResistance(
                        dataframe = df, 
                        l = i, 
                        left_slip = left_slip, 
                        right_slip=right_slip
                ) == True:
            
            # Add the current candle's high value to the resistance list
            resistance.append(df['high'][i])

    # Return the support and resistance lists
    return support, resistance



