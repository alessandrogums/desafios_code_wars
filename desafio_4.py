def valid_parentheses(string):
    parenteses = []
    for i in string:
        if i == ')' or i == '(':
            parenteses.append(i)

    cont = 0

    while not cont >= len(parenteses):
        # print(cont)
        if '(' == parenteses[len(parenteses) - 1] or ')'==parenteses[0]:
            break
        elif parenteses[cont] == '(' and parenteses[cont + 1] == ')':

            parenteses.pop(cont + 1) and parenteses.pop(cont)

            cont =0
        elif len(parenteses)==2:
            if parenteses[0]=='(' and parenteses[1]==')':
                parenteses.clear()


        # print(parenteses)
        cont += 1

    if len(parenteses)>=1:
        return False
    else:
        return True


      

print(valid_parentheses('(((0)))())('))
