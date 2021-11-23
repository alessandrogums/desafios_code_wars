def is_isogram(string):
    string=string.strip().lower()
    for c in string:
        if string.count(c) > 1:
            return False 
    return True
