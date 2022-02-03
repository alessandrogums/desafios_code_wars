def scale(string,k,v):
    string=string.split()
    stringg,string_final='',''
    for palavra in string:
        stringg=''
        for letra in range(len(palavra)):
            stringg+=palavra[letra]*k
        string_final+=(stringg + '\n')*v
    return string_final[:len(string_final)-1]
  
