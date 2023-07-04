from config import *
from dependencies import *
from utils import *
from filtering import *

def caller_fn(df, tolerance = 0.005, bandwidth = 0.0005):

    # Print a message to the user
    print("\n\n\t\t\t------- Data are available from 05.05.2003 to 18.10.2019 -------")
    print("\n\tWe will calculate the entry and exit points based on past 350 days record wrt the date you mention.")
    
    # Get the date from the user
    date = str(input("\t\tEnter the date you want to know the entry and exit points:"))

    # Initialize variables for start and end indices and dates
    start_index = 0
    end_index = 0
    start_date = ""
    end_date = ""

    # Iterate over the dataframe to find the specified date
    for i in range(len(df)):
        if df['Local time'][i] == date:
            start_index += i - 351;
            end_index += i - 1;
            start_date += df['Local time'][i - 351]
            end_date += df['Local time'][i - 1]

    # Extract support and resistance levels from the specified range of candles in the dataframe
    support, resistance = extract_support_resistance(df, start_index=start_index, end_index=end_index)

    # Filter the support and resistance levels based on the specified tolerance
    support, resistance = filter_tradeLines(support=support, resistance=resistance, tolerance=tolerance)

    # Calculate the current high and low values
    cur_high = df['high'][end_index]
    cur_low = df['low'][end_index]

    # Calculate the current price
    cur = (cur_low + cur_high)/2

    # Initialize variables for local support and resistance levels
    # global local_support 
    # global local_resistance 

    seed = 6575798687

    # Find the local support level closest to the current price
    for i in range(1, len(support)):
        if abs(abs(cur) - abs(support[i])) < seed:
            seed = abs(abs(cur) - abs(support[i]))
            local_support = support[i]

    seed = 6575798687

    # Find the local resistance level closest to the current price
    for i in range(1, len(resistance)):
        if abs(abs(cur) - abs(resistance[i])) < seed:
            seed = abs(abs(cur) - abs(resistance[i]))
            local_resistance = resistance[i]

    # Print a message to the user with the calculated entry and exit points
    print(f"\n\tWe studied the data from {start_date} to {end_date}\n")
    print(f"\tEntry Point: {round(local_support - bandwidth, 5)} to {round(local_support + bandwidth, 5)} ")
    print(f"\tExit Point: {round(local_resistance - bandwidth, 5)} to {round(local_resistance + bandwidth, 5)} ")