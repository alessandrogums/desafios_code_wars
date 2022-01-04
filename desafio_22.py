def solution(string, marcadores):
    string_filt=''
    i=0
    while i < len(string):
        if string[i] not  in marcadores:
          string_filt+=string[i]
        else:
            if string[i-1]=="\n":
                pass
            else:
                string_filt=string_filt.rstrip()
            for k in string[i:]:
                if k =="\n":
                    string_filt+="\n"
                    break
                i+=1
        i+=1        
        
    return string_filt
