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
#### move_zeros([1, 0, 1, 2, 0, 1, 3]) 
#### returns [1, 1, 2, 1, 3, 0, 0]


### Desafio número 9:
### Escreva uma função nomeada que pegue uma entrada de string e retorne o primeiro caractere que não é repetido em nenhum lugar da string.first_non_repeating_letter

### Por exemplo, se dada a entrada, a função deve retornar, uma vez que a letra não ocorre apenas uma vez na sequência, e ocorre primeiro na sequência.'stress''t'

### Como um desafio adicional, letras maiúsculas e minúsculas são consideradas o mesmo caractere,mas a função deve retornar o caso correto para a letra inicial. Por exemplo, a entrada deve retornar .'sTreSS''T'

### Se uma sequência contiver todos os caracteres repetitivos,ela deve retornar uma sequência vazia () ou -- ver testes de amostra.""None

### Desafio número 10:
### Alguns números têm propriedades engraçadas. Por exemplo:

#### 89 --> 8¹ + 9² = 89 * 1

#### 695 --> 6² + 9³ + 50= 1390 = 695 * 2

#### 46288 --> 4³ + 60+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

### Dado um inteiro positivo n escrito como abcd ... (a, b, c, d... sendo dígitos) e um inteiro positivo p

### queremos encontrar um inteiro positivo k, se ele existe, como a soma dos dígitos de n levados aos sucessivos poderes de p é igual a k * n.
### Em outras palavras:

### Existe um inteiro k tais como : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

### Se for o caso, retornaremos k, se não voltarmos -1.

##### Nota: n e p sempre serão dados como inteiros estritamente positivos.


### Desafio número 11:
### Escreva uma função que leve uma matriz de números (inteiros para os testes) e um número de destino. Ele deve encontrar dois itens diferentes na matriz que, quando ### adicionados juntos, dão o valor de destino. Os índices desses itens devem então ser devolvidos em uma tupla como assim: .(index1, index2)

### Para efeitos deste kata, alguns testes podem ter múltiplas respostas; quaisquer soluções válidas serão aceitas.

### A entrada será sempre válida (os números serão um conjunto de comprimento 2 ou superior, e todos os itens serão números; o alvo sempre será a soma de dois itens diferentes dessa matriz).

#### Exemplos:
#### twoSum [1, 2, 3] 4 === (0, 2)



### Desafio número 12:
### Um número narcisista é um número positivo que é a soma de seus próprios dígitos, cada um elevado ao poder do número de dígitos em uma determinada base. Neste Kata, vamos nos restringir ao decimal (base 10).

### Por exemplo, pegue 153 (3 dígitos), que é narcises:

 ####  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#### e 1652 (4 dígitos), o que não é:

#### 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
### O Desafio:

### Seu código deve retornar verdadeiro ou falso (não 'verdadeiro' e 'falso') dependendo se o número dado é um número narcisista na base 10. 

### Não é necessário verificar erros para sequências de texto ou outras entradas inválidas, apenas os inteiros positivos não-zero válidos serão passados para a função.

### Desafio número 13:
### Um isograma é uma palavra que não tem letras repetidas, consecutivas ou não consecutivas. Implemente uma função que determine se uma sequência que contém apenas letras é um ### isograma. Suponha que a corda vazia seja um isograma. Ignore o caso da carta.
#### Exemplos:
#### "Dermatoglyphics" --> true
#### "aba" --> false
#### "moOse" --> false (ignore letter casing)

### Desafio número 14:
### Um pangrama é uma frase que contém cada letra do alfabeto pelo menos uma vez. Por exemplo, a frase "The quick brown fox jumps over the lazy dog" é um pangrama, porque ### usa as letras A-Z pelo menos uma vez (caso é irrelevante).

### Dado uma corda, detecte se é ou não um pangrama. Devolva True se for, falso se não. Ignore números e pontuação.


### Desafio número 15:
### Uma Progressão Aritmética é definida como aquela em que há uma diferença constante entre os termos consecutivos de uma determinada série de números. Você é fornecido com elementos consecutivos de uma Progressão Aritmética. No entanto, há um problema: exatamente um termo da série original está faltando do conjunto de números que foram dados você. O resto da série dada é o mesmo que o AP original.

### Você tem que escrever uma função que recebe uma lista, o tamanho da lista sempre será de pelo menos 3 números. O termo perdido nunca será o primeiro ou o último.

### Exemplo
### find_missing([1, 3, 5, 9, 11]) == 7
### PS: Esta é uma questão amostra do desafio do engenheiro do Facebook na rua de entrevistas. Achei muito divertido resolver no papel usando matemática, derivar o algo dessa forma. Divertir-se!

### Desafio número 16:
### O desenho mostra 6 quadrados dos quais têm um comprimento de 1, 1, 2, 3, 5, 8. É fácil ver que a soma dos perímetros desses quadrados é: 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

### Você poderia dar a soma dos perímetros de todos os quadrados em um retângulo quando há n + 1 quadrados descartados da mesma forma que no desenho:
![image](https://user-images.githubusercontent.com/90655009/143148092-45fd474c-26e1-4b42-b6d3-96af00d14f75.png)

### O perímetro de função tem para parâmetro n onde n + 1 é o número de quadrados (eles são numerados de 0 a n) e retorna o perímetro total de todas as praças.
#### Exemplos:
#### perimeter(5)  should return 80
#### perimeter(7)  should return 216

### Desafio número 17:
### Para este exercício você estará fortalecendo seu domínio page-fu. Você completará a classe PaginationHelper, que é uma classe de utilidade útil para consultar informações de paginação relacionadas a um array.

### A classe foi projetada para receber uma variedade de valores e um inteiro indicando quantos itens serão permitidos por cada página. Os tipos de valores contidos no conjunto de coleta/matriz não são relevantes.

### A seguir, alguns exemplos de como esta classe é usada:

#### helper = PaginationHelper(['a','b','c','d','e','f'], 4)
#### helper.page_count() # should == 2
#### helper.item_count() # should == 6
#### helper.page_item_count(0)  # should == 4
#### helper.page_item_count(1) # last page - should == 2
#### helper.page_item_count(2) # should == -1 since the page is invalid

#### page_index takes an item index and returns the page that it belongs on
#### helper.page_index(5) # should == 1 (zero based index)
#### helper.page_index(2) # should == 0
#### helper.page_index(20) # should == -1
#### helper.page_index(-10) # should == -1 because negative indexes are invalid


### Desafio número 18:
### Sudoku é um jogo jogado em um grid 9x9. O objetivo do jogo é encher todas as células da grade com dígitos de 1 a 9, de modo que cada coluna, cada linha, e cada uma das nove sub-grades 3x3 (também conhecidas como blocos) contenham todos os dígitos de 1 a 9.
### (Mais informações em: http://en.wikipedia.org/wiki/Sudoku)

### Validador de soluções Sudoku
### Escreva uma função // que aceite uma matriz 2D representando uma placa Sudoku e retorne verdadeira se for uma solução válida ou falsa de outra forma. As células da placa sudoku também podem conter 0's, o que representará células vazias. Placas contendo um ou mais zeros são consideradas soluções inválidas.validSolutionValidateSolutionvalid_solution()

### A placa é sempre 9 células por 9 células, e cada célula contém apenas inteiros de 0 a 9.

#### Exemplos
#### validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
#### validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false

### Desafio número 19:
### Neste kata queremos converter uma string em um inteiro. As strings simplesmente representam os números em palavras.

#### Exemplos:
#### OBS: CONVERSÂO FEITA EM NÚMEROS EM INGLES PARA VALIDAR O DESAFIO PELO SITE
#### "um" => 1
#### "vinte" => 20
#### "duzentos e quarenta e seis" => 246
#### "setecentos e oitenta e três mil novecentos e dezenove" => 783919
#### Notas adicionais:

#### O número mínimo é "zero" (inclusive)
#### O número máximo, que deve ser suportado é de 1 milhão (inclusive)
#### O "e" em por exemplo, "cento e vinte e quatro" é opcional, em alguns casos está presente e em outros não é
#### Todos os números testados são válidos, você não precisa validá-los


### Desafio número 20:
### Você tem que dar o número de diferentes triângulos inteiros com um ângulo de 120 graus que os perímetros estão abaixo ou igual a um determinado valor. Cada lado de um triângulo inteiro é um valor inteiro.

### give_triang(max. perimeter) --------> number of integer triangles,
### com os lados a, b e c inteiros de tal forma que:

### a + b + c <= perímetro máximo.

#### Veja alguns dos seguintes casos

#### give_triang(5) -----> 0 # No Integer triangles with perimeter under or equal five
#### give_triang(15) ----> 1 # One integer triangle of (120 degrees). It's (3, 5, 7)
#### give_triang(30) ----> 3 # Three triangles: (3, 5, 7), (6, 10, 14) and (7, 8, 13)
#### give_triang(50) ----> 5 # (3, 5, 7), (5, 16, 19), (6, 10, 14), (7, 8, 13) and (9, 15, 21) are the triangles with perim under or equal 50.
