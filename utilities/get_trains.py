import pandas as pd


def get_trains(data: pd.core.frame.DataFrame):
    """
    Returns unique list of trains

    parameters:
        data: pandas dataframe data
    return:
        dict: unique trains dict with there frequency
    """
    unique_trains = {}
    for _, entry in data.iterrows():
        temp = str(entry["Occurrence Location"])
        if 'train' in temp:
            train_number = temp.split("train")[1].strip()
            train_number = train_number.split(" ")[2].split(
                "(")[0]   # Extract train number
            # print(train_number.split("(")[0])
            if train_number not in unique_trains:
                unique_trains[train_number] = 0
            unique_trains[train_number] += 1
    return unique_trains
