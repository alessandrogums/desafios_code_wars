# Desafios Code Wars(TRADUZIDO para pt-br)
## Desafios do site https://www.codewars.com, utilizando a linguagem python para resolvê-los
### Desafio número 1:
### Conclua o método / função para que ele converta palavras delimitadas por traço / sublinhado em caixa de camelo. A primeira palavra na saída deve ser maiúscula apenas se a palavra original estiver em maiúscula (conhecido como Upper Camel Case, também frequentemente referido como Pascal case).

#### Exemplos
#### "the-stealth-warrior" é convertido em "the-stealthWarrior"
#### "The_Stealth_Warrior" é convertido em "TheStealthWarrior"

### Desafio número 2:
### Escreva uma função que aceite uma matriz de 10 inteiros (entre 0 e 9), que retorne uma string desses números na forma de um número de telefone.

#### Exemplos 
#### create_phone_number ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => retorna "(123) 456-7890"
#### O formato retornado deve estar correto para completar este desafio.
#### Não se esqueça do espaço após os parênteses de fechamento!

### Desafio número 3:
### O objetivo deste desafio é implementar uma função de diferença, que subtrai uma lista da outra e retorna o resultado.

### Deve remover todos os valores da lista a, que estão presentes na lista b mantendo sua ordem.

#### Exemplos:array_diff ([1,2], [1]) == [2]
 #### Se um valor estiver presente em b, todas as suas ocorrências devem ser removidas do outro:

 #### array_diff ([1,2,2,2,3], [2]) == [1,3]
### Desafio número 4:
### Escreva uma função que leve uma sequência de parênteses e determine se a ordem dos parênteses é válida. A função deve retornar se a sequência for válida e se for inválida true/false,respectivamente.

#### Exemplos
#### "()"              =>  true
#### ")(()))"          =>  false
#### "("               =>  false
#### "(())((()())())"  =>  true
#### Restrições
#### 0 <= input.length <= 100

#### Juntamente com a abertura () e o fechamento () parênteses, a entrada pode conter quaisquer caracteres ASCII válidos. Além disso, a sequência de entrada pode estar vazia #### e/ou não conter nenhum parêntese. Não trate outras formas de parênteses como parênteses (por exemplo, , .()[]{}<>
