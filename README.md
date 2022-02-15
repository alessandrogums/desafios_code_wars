# Desafios Code Wars(TRADUZIDO para pt-br)
## Desafios do site https://www.codewars.com, utilizando a linguagem python para resolvê-los.É valido ressaltar que os desafios não estão organizados pela dificuldade, ou seja, não necessariamente os últimos são os com dificuldade maior do que os anteriores. 
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

### Desafio número 21:
### suponha que você tenha 4 números: e 3 strings compostas com eles:'0', '9', '6', '4'

### s1 = "6900690040"
### s2 = "4690606946"
### s3 = "9990494604"
### Compare e veja quantas posições elas têm em comum: no índice 3, no índice 4, no índice 8 ou seja, 3 posições comuns de dez.s1s2064

### Compare e veja quantas posições elas têm em comum: no índice 1, no índice 3, no índice 5 ou seja, 3 posições comuns de dez.s1s3909

### Compare e . Encontramos 2 posições comuns em dez.s2s3

### Então, para as 3 cordas temos 8 posições comuns de 30 ou seja, 0,2666... ou 26.666...%

### Dado substrings (n >= 2) em uma string nossa função calculará a porcentagem média de posições que são as mesmas entre os conjuntos de substrings tomados entre os substrings dado. Pode acontecer que alguns substrings são duplicados, mas como suas fileiras não são as mesmas em serem consideradas substrings diferentes.nspos_average(n * (n-1)) / 2ns

### A função retorna a porcentagem formatada como um flutuador com 10 decimais, mas o resultado é testado em 1e.-9 (ver função assertFuzzy nos testes).

#### Exemplo:
#### Dado string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490" compondo um conjunto de n = 10 substrings (daí 45 combinações), retorna .pos_average29.2592592593

#### Em um conjunto, os substrings terão o mesmo comprimento (> 0 ).n

### Desafio número 22:
### Complete a solução para que ela tire todo o texto que segue qualquer um conjunto de marcadores de comentários passados. Qualquer espaço branco no final da linha também deve ser retirado.

#### Exemplo:

#### Dada uma sequência de entrada de:

#### apples, pears # and bananas
grapes
bananas !apples
A saída esperada seria:

#### apples, pears
grapes
bananas

#### O código seria chamado assim:

##### result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
##### result should == "apples, pears\ngrapes\nbananas"


### Desafio número 23:
### Certo, detetive, um de nossos colegas observou com sucesso nosso alvo, Robby, o ladrão. Nós o seguimos até um armazém secreto, onde assumimos encontrar todas as coisas roubadas. A porta deste armazém está presa por uma fechadura eletrônica. Infelizmente nosso espião não tem certeza sobre o PIN que ele viu, quando Robby entrou nele.

### O teclado tem o seguinte layout:

![image](https://user-images.githubusercontent.com/90655009/146844915-b5e6e986-485b-43e2-b83e-5d81246ebc4e.png)

    

### Ele observou o PIN, mas também disse, é possível que cada um dos dígitos que viu possa realmente ser outro dígito adjacente (horizontal ou verticalmente, mas não na diagonal).

### Ele também mencionou, ele sabe este tipo de fechaduras. Você pode inserir uma quantidade ilimitada de PINs errados, eles nunca finalmente bloqueiam o sistema ou soam o alarme. É por isso que podemos experimentar todas as variações possíveis (*).

#### * possível no sentido de: o PIN observado em si e todas as variações considerando os dígitos adjacentes

### Pode nos ajudar a encontrar todas essas variações? Seria bom ter uma função, que retorna uma matriz  de todas as variações para um PIN observado com um comprimento de 1 a 8 dígitos. Poderíamos nomear a função. Mas, por favor, note que todos os PINs, o observado e também os resultados, devem ser strings, por causa do  '0's. Já preparamos alguns casos de teste para você.

### Detetive, estamos contando com você!


### Desafio número 24:
### Escreva uma função, que leva um inteiro não negativo (segundos) como entrada e retorna o tempo em um formato legível pelo homem (HH:MM:SS)

### HH = horas, acolchoado a 2 dígitos, intervalo: 00 a 99
### MM = minutos, acolchoado a 2 dígitos, intervalo: 00 a 59
### SS = segundos, acolchoado a 2 dígitos, intervalo: 00 a 59
#### O tempo máximo nunca excede 359999 (99:59:59)

### Desafio número 25:
#### Mova a primeira letra de cada palavra para o final dela, em seguida, adicione "ay" ao final da palavra. Deixe marcas de pontuação intocadas.

#### Exemplos
##### pig_it('Pig latin is cool') # igPay atinlay siay oolcay
##### pig_it('Hello world !')     # elloHay orldway !

### Desafio número 26:
### Escreva uma função que, dada uma sequência de texto (possivelmente com pontuação e quebras de linha), retorna uma matriz das palavras mais ocorrerias no top-3, na ordem descendente do número de ocorrências.

### Suposições:
### Uma palavra é uma sequência de letras (A a Z) contendo opcionalmente um ou mais apóstrofes () em ASCII.'
### Apóstrotrofes podem aparecer no início, meio ou fim de uma palavra (, , são todos válidos)'abcabc''abc'ab'c
### Quaisquer outros caracteres (por exemplo, , , ... ) não fazem parte de uma palavra e devem ser tratados como espaço branco.#\/.
### As partidas devem ser insensíveis, e as palavras no resultado devem ser minúsculas.
### Os laços podem ser quebrados arbitrariamente.
### Se um texto contiver menos de três palavras únicas, as palavras top-2 ou top-1 devem ser devolvidas ou uma matriz vazia se um texto não contiver palavras.
#### Exemplos:
  #### top_3_words("In a village of La Mancha, the name of which I have no desire to call to
  #### mind, there lived not long since one of those gentlemen that keep a lance
  #### in the lance-rack, an old buckler, a lean hack, and a greyhound for
  #### coursing. An olla of rather more beef than mutton, a salad on most
  #### nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
  #### on Sundays, made away with three-quarters of his income.")
  #### => ["a", "of", "on"]

#### top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
#### => ["e", "ddd", "aa"]

#### top_3_words("  //wont won't won't")
####  => ["won't", "wont"]
### Pontos bônus (não realmente, mas apenas por diversão):
### Evite criar uma matriz cuja pegada de memória é aproximadamente tão grande quanto o texto de entrada.
### Evite classificar toda a matriz de palavras únicas.

### Desafio número 27:
### complete a função/método (dependendo da linguagem) para retornar / quando seu argumento é uma matriz que tem as mesmas estruturas de aninhamento e o mesmo comprimento correspondente de matrizes aninhadas que a primeira matriz.true/ True

#### Por exemplo:

#### should return True
#### same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
#### same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

#### should return False 
#### same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
#### same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

#### should return True
#### same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

#### should return False
#### same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

### Desafio número 28:
### A função rgb está incompleta. Complete-o para que a passagem em valores decimais RGB resulte em uma representação hexadecimal sendo devolvida. Os valores decimais válidos para RGB são de 0 a 255. Os valores que saem dessa faixa devem ser arredondados para o valor válido mais próximo.

### Nota: Sua resposta deve ser sempre de 6 caracteres, a taquigrafia com 3 não funcionará aqui.

#### A seguir, exemplos de valores de saída esperados:

#### rgb(255, 255, 255) # returns FFFFFF
#### rgb(255, 255, 300) # returns FFFFFF
#### rgb(0,0,0) # returns 000000
#### rgb(148, 0, 211) # returns 9400D3

### Desafio número 29:
### Era uma vez, em um caminho através do velho oeste montanhoso selvagem,...
### ... um homem foi dado instruções para ir de um ponto para outro. As direções foram "NORTE", "SUL", "OESTE", "LESTE". Claramente "NORTE" e "SUL" são opostos, "OESTE" e "LESTE" também.

### Ir para uma direção e voltar na direção oposta imediatamente é um esforço desnecessário. Uma vez que este é o oeste selvagem, com tempo terrível e pouca água, é importante economizar um pouco de energia, caso contrário você pode morrer de sede!

#### Como atravessei um deserto montanhoso da maneira inteligente.
#### As instruções dadas ao homem são, por exemplo, as seguintes (dependendo da linguagem):

#### ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
#### { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
#### [North, South, South, East, West, North, West]

#### Outros exemplos:
#### Em , a direção está indo para o norte e voltando imediatamente. ["NORTH", "SOUTH", "EAST", "WEST"]"NORTH" + "SOUTH"

#### O caminho se torna , agora e aniquilar uns aos outros, portanto, o resultado final é (zero em Clojure).["EAST", "WEST"]"EAST""WEST"[]

#### Em ["NORTE", "LESTE", "OESTE", "SUL", "OESTE", "OESTE"], "NORTE" e "SUL" não são diretamente opostos, mas se tornam diretamente opostos após a redução de "LESTE" e "OESTE" para que todo o caminho seja redutível para ["OESTE", "OESTE"].

### Tarefa
### Escreva uma função que levará uma matriz de strings e retorna uma matriz de strings com as direções desnecessárias removidas (W<->E ou S<->N lado a lado).dirReduc

### Desafio número 30:
### Dadas as duas cordas s1 e s2, queremos visualizar o quão diferentes são as duas cordas. Só levaremos em conta as letras minúsculas (a a z). Primeiro vamos contar a frequência de cada letras minúsculas em s1 e s2.
### s1 = "A aaaa bb c"

### s2 = "& aaa bbb c d"

### s1 has 4 'a', 2 'b', 1 'c'

### s2 has 3 'a', 3 'b', 1 'c', 1 'd'

### Assim, o máximo para 'a' em s1 e s2 é 4 de s1; o máximo para 'b' é 3 de s2. A seguir, não consideraremos cartas quando o máximo de suas ocorrências for menor ou igual a 1.

### Podemos retomar as diferenças entre s1 e s2 na seguinte sequência: onde em posição para string s1 e porque o máximo para é 4. Da mesma forma significa string s2 e porque o máximo para é 3."1:aaaa/2:bbb"11:aaaaaaaaa2:bbbbbbb

### A tarefa é produzir uma sequência na qual cada letras minúsculas de s1 ou s2 apareça tantas vezes quanto o seu máximo se este máximo for estritamente maior que 1; essas letras serão prefixadas pelo número da sequência onde aparecem com seu valor máximo e . Se o máximo estiver no S1, bem como no s2, o prefixo é .:=:

### No resultado, substrings (um substring é, por exemplo, 2:nnnnn ou 1:hhh; contém o prefixo) estarão em ordem decrescente de seu comprimento e quando tiverem o mesmo comprimento classificado em ordem lexicográfica ascendente (letras e dígitos - mais precisamente classificados por ponto de código); os diferentes grupos serão separados por '/'. Veja exemplos e "Testes de Exemplo".

![image](https://user-images.githubusercontent.com/90655009/152017670-fa664f0c-fdd3-497a-a792-f88fde8e39c4.png)


### Desafio número 31:
### Você recebe uma série de linhas, cada substring sendo personagens longos. Por exemplo:nn

#### s = "abcd\nefgh\nijkl\nmnop"

### Estudaremos o dimensionamento "horizontal" e o dimensionamento "vertical" deste quadrado de cordas.

### Um dimensionamento k-horizontal de uma sequência consiste em replicar vezes cada caractere da string (exceto '\n').k

#### Exemplo: dimensionamento 2-horizontal de s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
Um dimensionamento v-vertical de uma sequência consiste em replicar vezes cada parte da corda quadrada.v

#### Exemplo: dimensionamento vertical de 2: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop\nmnop"

### A função executará um dimensionamento k-horizontal e um dimensionamento v-vertical.scale(strng, k, v)
#### Example: a = "abcd\nefgh\nijkl\nmnop" scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
#### Impresso:

![image](https://user-images.githubusercontent.com/90655009/152409179-6bcc43a8-7a8a-4375-a4e4-41da513f9839.png)

### Tarefa: Escrever função k e v serão inteiros positivos. Se retornar.scale(strng, k, v)strng == """"

### Desafio número 32:
### Dado o triângulo de números ímpares consecutivos:

![image](https://user-images.githubusercontent.com/90655009/152435299-677cc1c7-1776-4261-9dca-dd7b57197f6e.png)


### Calcule a soma dos números no nésimo linha deste triângulo (começando no índice 1) por exemplo: (Entrada --> Saída)

#### 1 -->  1
#### 2 --> 3 + 5 = 8

## Desafio número 33:
### O problema da Torre de Hanói envolve 3 torres. Uma série de anéis que diminuem de tamanho são colocados em uma torre. Todos os anéis devem então ser movidos para outra torre, mas em nenhum momento um anel maior pode ser colocado em um anel menor.

### Sua tarefa: Dado um número de anéis, retorne o número MÍNIMO de movimentos necessários para mover todos os anéis de uma torre para outra.

## Desafio número 34:

### Sua tarefa é calcular o número mínimo de movimentos para ganhar o jogo "Towers of Hanoi", com um determinado número de discos.

### O que é "Torres de Hanói"?
### Towers of Hanoi, é um jogo simples que consiste em três varas, e uma série de discos de diferentes tamanhos que podem deslizar para qualquer vara. O quebra-cabeça começa com os discos em uma pilha limpa em ordem ascendente de tamanho em uma haste, a menor no topo, fazendo assim uma forma cônica.

### O objetivo do quebra-cabeça é mover toda a pilha para outra vara, obedecendo às seguintes regras simples:

### Apenas um disco pode ser movido de cada vez.
### Cada movimento consiste em pegar o disco superior de uma das pilhas e colocá-lo em cima de outra pilha, ou seja, um disco só pode ser movido se for o disco mais alto de uma pilha.
### Nenhum disco pode ser colocado em cima de um disco menor.

## Desafio número 35:
### Uma forteza de um número par é o número de vezes que podemos dividir sucessivamente por 2 até chegarmos a um número ímpar começando com um número par n.

### Por exemplo, se n = 12, então

#### 12 / 2 = 6
#### 6 / 2 = 3
#### Então dividimos sucessivamente 2 vezes e chegamos a 3, então a força de 12 é.2

#### Se n = 16, então

#### 16 / 2 = 8
#### 8 / 2 = 4
#### 4 / 2 = 2
#### 2 / 2 = 1
### dividimos sucessivamente 4 vezes e chegamos a 1, então a força de 16 é 4

### Tarefa
### Dado um intervalo fechado, retorne o número igual que é o mais forte no intervalo. Se existirem várias soluções, retorne o menor número de pontos.[n, m]

### Observe que os programas devem ser executados dentro do tempo de servidor alocado; uma solução ingênua provavelmente vai estourar o tempo! 
