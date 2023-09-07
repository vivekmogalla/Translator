import re


#Function to check any exceptional names in file
def contains_exceptional_names(actual_filename, line):
    file_name_split = actual_filename.split()
    check = False
    for i in file_name_split:
        if i in line or 'ENG' in line or 'TIME' in line or 'Duration' in line or 'Time' in line:
            check = 'True'
            return check
    return check
#End of function


#Function to check any patterns are there
def conatins_time_range(line):
    pattern = r"\b\d+:\d+-\d+:\d+\b"
    return bool(re.search(pattern, line))
#End of function