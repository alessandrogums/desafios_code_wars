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
#outra solução mais extensa que fiz, porém com passos mais diretos, utilizando a lógica das posições finais para saber como ficará o final da string.

def solution(string,marcadores):
    string_final=''
    string=str(string)
    pos_mar,pos_esp=posicoes_finais(marcadores,string)
    
    i=0
    if len(string)==0:
        return ""
    elif len(string)==1:
        if string in marcadores:
            return ''
        else:
            return string
    else:
           if pos_esp>pos_mar or pos_mar==0:
                string+=string[(len(string)-1)]
                tamanho_string=len(string)-1
                while (len(string)-1)>= i:
                    if i>=len(string)-1:
                        break
                    if string[i] in marcadores:
                        for i in range(i,tamanho_string):
                            if string[i]=='\n':
                                break
                    elif string[i+1] in marcadores and string[i]==" ":
                        for i in range(i,tamanho_string):
                            if string[i]=='\n':
                                break
                    elif string[i+1] in marcadores and string[i]!=' ':
                        if string[i]=='\n':
                            pass
                        else:
                            string_final+=string[i]
                        for i in range(i,tamanho_string):
                            if string[i]=='\n':
                                break
                    string_final+=string[i]
                    i+=1
           else:
                while (len(string))>= i:
                   
                    if string[i] in marcadores:
                        for i in range(i,len(string)):
                            if string[i]=='\n':
                                break
                    elif string[i+1] in marcadores and string[i]==" ":
                        for i in range(i,len(string)):
                            if string[i]=='\n':
                                break
                    elif string[i+1] in marcadores and string[i]!=' ':
                        if string[i]=='\n':
                            pass
                        else:
                            string_final+=string[i]
                        for i in range(i,len(string)):
                            if string[i]=='\n':
                                break 
                    if i>len(string)-2:
                        break
                    string_final+=string[i]
                    i+=1
               
    return string_final

def posicoes_finais(marcadores,string):
    x,y=0,0
    for k in range(len(string)):
        if string[k] in marcadores:
            x=k
        elif string[k] =="\n":
            y=k
    return x,y
