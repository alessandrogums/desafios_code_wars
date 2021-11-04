def to_weird_case(string):
    string = string.strip()
    if len(string)==1:
        return string.upper()
    else:
        palavra_vazia = ''
        str_variavel = ''
        #Fazer o refinamento do código para retirar mais de um espaço entre as palavras, quando houver
        c = 0
        while len(string) >= c + 1:
            if string[c] != ' ':
                str_variavel += string[c]


            else:
                str_variavel += string[c]
                while string[c] == ' ':
                    c += 1
                str_variavel += string[c]
            c += 1
        ini=0
        fin=0
        qte_espaco= str_variavel.count(' ')
        for i in range(len(str_variavel)):
            var_mutavel = ''
            if i==0:
                ini=0
            elif str_variavel[i] == ' ' and qte_espaco>0:
                qte_espaco-=1
                fin=i+1

                var_mutavel=str_variavel[ini:fin]
                for k in range(len(var_mutavel)):
                    if k % 2 == 0:
                         palavra_vazia += var_mutavel[k].upper()
                    else:
                         palavra_vazia += var_mutavel[k]
                palavra_vazia+=''
                ini=fin
            elif qte_espaco==0:
                var_mutavel=str_variavel[fin:]
                for k in range(len(var_mutavel)):
                    if k % 2 == 0:
                         palavra_vazia += var_mutavel[k].upper()
                    else:
                         palavra_vazia += var_mutavel[k]
                break
        return palavra_vazia
