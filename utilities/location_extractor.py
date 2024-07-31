def extract_location(input_text: str, input_locations: list):
    for location in input_locations:
        if '-' in location:
            places = location.split("-")
            if 'between' in input_text:
                temp = input_text.split("between")
                temp = temp[1].strip().split(" ")
                temp = temp[0]+"-" + temp[2]
                return temp
        else:
            if 'between' not in input_text:
                return input_text.split(" ")[-1]
