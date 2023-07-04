from config import *
from dependencies import * 
from dataloader import *
from preprocessing import *
from utils import *
from filtering import *
from caller import *

def __run__():
    # Load the dataset
    df = load_dataset()

    # Modify the date format of the dataframe
    df = date_modifier(df)

    # Drop the NA Vol columns from the dataframe
    df = drop_NAVol(df)

    # Call the caller_fn function with the specified tolerance and bandwidth values
    caller_fn(df, tolerance = tolerance, bandwidth=bandwidth)

if __name__ == "__main__":
    __run__()
