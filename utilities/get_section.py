import pandas as pd


def get_section(data: pd.core.frame.DataFrame):
    '''
    This function returns a list of unique sections that is contained in the data

    Parameter:
    data: Main data in pandas format

    Return:
    dict: list of unique sections with there numbers occured
    '''
    unique_sections = {}
    for _, row in data.iterrows():
        # access row data using row['column_name']
        temp = str(row['Sections'])
        temp = temp.split(",")
        for i in temp:
            if i.strip() not in unique_sections:
                unique_sections[i.strip()] = 0
            unique_sections[i.strip()] += 1
    return unique_sections
