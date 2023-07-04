from dependencies import *
from config import *

def load_dataset():

    '''

    # -------- Below is the dataset Descriptor ---------- # 

    Local time: The date and time wrt to the data 
    Open: The first traded price
    Close: The final traded price
    High: The highest traded price
    Low: The lowest traded price
    Volume: The total volume traded by all trades

    ''' 

    df = pd.read_csv(data_path)
    return df



