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

#### Juntamente com a abertura () e o fechamento () parênteses, a entrada pode conter quaisquer caracteres ASCII válidos. Além disso, a sequência de entrada pode estar vazia #### e/ou não conter nenhum parêntese. Não trate outras formas de parênteses como parênteses (por exemplo, , .()[]{}<>)

### Desafio número 5:
### Escreva uma função para "caso estranho"  que aceita uma string e retorna a mesma string com todos os caracteres pares indexados em cada palavra maiúscula 
### e todos os caracteres ímpares indexados em cada palavra minúscula. A indexação que acabamos de explicar é baseada em zero, portanto, o índice zero-ésimo é par, portanto, esse caractere deve ser maiúsculo e você precisa começar de novo para cada palavra.
### A string passada consistirá apenas em caracteres alfabéticos e espaços (''). Os espaços só estarão presentes se houver várias palavras. As palavras serão separadas por um ### único espaço ('').


#### Exemplos:
#### to_weird_case ('String');  => retorna 'StRiNg'
#### to_weird_case ('Weird string case')  => retorna 'WeIrD StRiNg CaSe'

### Desafio número 6:
### Jaden Smith, filho de Will Smith, é a estrela de filmes como The Karate Kid (2010) e After Earth (2013). Jaden também é conhecido por algumas de suas filosofias que ele 
### entrega via Twitter. Ao escrever no Twitter, ele é conhecido por quase sempre capitalizar cada palavra. Para simplificar, você terá que capitalizar cada palavra, confira 
### como as contrações devem ser no exemplo abaixo.

### Sua tarefa é converter cordas em como elas seriam escritas por Jaden Smith. As cordas são citações reais de Jaden Smith, mas não são capitalizadas da mesma forma que ele 
### originalmente as digitou.

#### Exemplos: 
#### Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#### Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

### Desafio número 7:
### Raiz digital é a soma recursiva de todos os dígitos em um número.
### Dado o valor, pegue a soma dos dígitos. Se esse valor tiver mais de um dígito, continue reduzindo desta forma até que um número de um dígito seja produzido. A entrada será um inteiro não negativo.

#### Exemplos:
#### 16  -->  1 + 6 = 7
#### 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#### 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#### 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

### Desafio número 8:
### Escreva um algoritmo que pegue uma matriz e mova todos os zeros até o fim, preservando a ordem dos outros elementos.

#### Exemplos:
#### move_zeros([1, 0, 1, 2, 0, 1, 3]) #### returns [1, 1, 2, 1, 3, 0, 0]
