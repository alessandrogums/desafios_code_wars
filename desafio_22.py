def solution(string,marcadores):
    string_final = ""
    i = 0
    while len(string)>i>=0:
        if string[i] not in marcadores:
            string_final += string[i]
            i += 1
        else:
            if string[i-1]==" ":
                string_final = string_final.strip(" ")
            if "\n" in string[i:]:
                for k,v in enumerate(string[i:]):
                    if v=="\n":
                        i += k
                        break
            else:
                return string_final
    return string_final
