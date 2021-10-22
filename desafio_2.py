def create_phone_number(num):
    num.insert(0,'(')
    num.insert(4,')')
    num.insert(5,' ')
    num.insert(9,'-')

    num_novo=''
    for valor in num:

        num_novo+=str(valor)
    return num_novo
  
  
  #outro método, de forma mais resumida e direta
  def create_phone_number(numero):
    numero = list(map(str, numero))
    return f'({"".join(numero[:3])}) {"".join(numero[3:6])}-{"".join(numero[6:10])}'

print(create_phone_number([1,2,4,6,7,8,9,8,9,1]))
