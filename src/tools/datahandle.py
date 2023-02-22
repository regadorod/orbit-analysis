import re

def string_to_dict(string, keyLabels):
    data_dict = {}
    for i, ele in enumerate(re.split("[; / , :]", string)):
        data_dict[ keyLabels[ i ] ] = int(ele)

    return data_dict