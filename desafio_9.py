def first_non_repeating_letter(string):
    if len(string)==0:
        return ''
    else:
        string_tratada=string.strip().lower()
        letra=string_tratada[0]
        c=0
        pos=0
        for c in range(len(string_tratada)):
            
            if  c+1==len(string_tratada) and string_tratada[c]  in string_tratada[:c]:
                return ''
            
            elif letra in string_tratada[c+1:] or letra in string_tratada[:c]:
                pos=c+1
                letra=string_tratada[pos]
            else:
                break
        pos=string_tratada.index(letra)
        return string[pos]
print(first_non_repeating_letter('PkFYDvsX EN3LnNAVvEZjV6J;Sk6U4'))
