import pandas as pd


def extract_location_code(data: pd.core.frame.DataFrame):
    """
    This function would return all the unique locations with there frequency
    """
    locations: list = []
    for _, entry in data.iterrows():
        temp = str(entry["Occurrence Location"])
        if 'between' in temp:
            temp = temp.split("between")
            temp = temp[1].strip().split(" ")
            temp = temp[0]+"-" + temp[2]
            if temp not in locations:
                locations.append(temp)
        else:
            temp = temp.split(" ")
            for i in temp:
                if (len(i) == 3 or len(i) == 4) and i.isupper() and i.isalpha():
                    if i not in locations:
                        locations.append(i)
    return locations
