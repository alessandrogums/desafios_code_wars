def pig_it(texto):
    texto_final=''
    vet_ini=texto.split()
    for palavra in vet_ini:
        palavra=str(palavra)
        primeira_letra=''
        if palavra.isalpha() == False:
            texto_final+=palavra
        else:
            for letra in range(len(palavra)):
                if letra==0:
                    primeira_letra=palavra[letra]
                else:
                    texto_final+=palavra[letra]
            texto_final+=primeira_letra+'ay'+' '
                
            
    return texto_final.strip()
