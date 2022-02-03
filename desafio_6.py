def to_jaden_case(string):
    string=string.split()
    for k in range(len(string)):
        aux=string[k].capitalize()
        string[k]=aux
    return ' '.join(string)

