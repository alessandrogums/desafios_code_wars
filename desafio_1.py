def to_camel_case(palavra):
   palavra_modificada = ''
   contador = 0
   while contador < len(palavra):

        if palavra[contador] == '_' or palavra[contador] == '-':
            palavra_modificada += palavra[contador + 1].upper()
            contador+=1
        elif palavra[contador] != '_':
            palavra_modificada += palavra[contador]
        contador += 1
   return palavra_modificada

print(to_camel_case('The-Stealth-Warrior'))
