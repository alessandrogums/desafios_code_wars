def interpreta_palavra(palavra):
    numbers = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8, 'nine':9,'ten':10,'eleven':11,'twelve':12}
    tem_hifen='-' in palavra
    adicional=0
    if tem_hifen:
        ini,fin=palavra.index('-')+1,len(palavra)
        adicional=numbers[palavra[ini:fin]]
    for k in range(len(palavra)):
            
            if (palavra[k-1] + palavra[k] ) == 'ty':
                s=0
                st=''
                while k != 0 :
                    k-=1
                st=palavra[k]+ palavra[k+1]
                for keys,values in numbers.items():
                    if st ==(keys[0]+keys[1]):
                        s=(values*10)+adicional
                        return s 
                        break
            elif (palavra[k:k+4]) =='teen':
                y=0
                rf=''
                while k !=0:
                    k-=1
                rf=palavra[k] + palavra[k+1]
                for keys,values in numbers.items():
                    if rf ==(keys[0]+keys[1]):
                        y= values +10 
                        return y
            elif palavra in numbers:
                return numbers[palavra]
def parse_int(string):
    um_milhao='one million' in string
    if um_milhao:
        return 1000000
    string=string.strip().split()
    string_filtrada=list(filter(lambda x: x!='and',string))
    valores=[]
    existem_ambos='hundred' in string_filtrada and 'thousand' in string_filtrada 
    if existem_ambos:
            if string_filtrada.index('hundred') < string_filtrada.index('thousand'):
                valor=interpreta_palavra(string_filtrada[0])
                valores.append(valor*100000)
                string_filtrada.pop(0) and string_filtrada.pop(0)
                if string_filtrada.index('thousand') ==0:
                    string_filtrada.pop(0)
    for chave,palavra in enumerate(string_filtrada):
        if palavra =='hundred':
            
            valores[len(valores)-1]*=100  
        elif palavra=='thousand':
            
            valores[len(valores)-1]*=1000
        
        else:
            numero=interpreta_palavra(palavra)
            valores.append(numero)
        print(valores) 
    return sum(valores)
