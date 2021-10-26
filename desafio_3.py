#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.

#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:

#array_diff([1,2,2,2,3],[2]) == [1,3]


def array_dif(a,b):
    vetor_intersec = []
    for valor in a:
        for i in b:
            if i == valor:
                 vetor_intersec.append(i)
    for c in range(len(vetor_intersec)):
        while vetor_intersec[c] in a:
            variavel=vetor_intersec[c]
            a.remove(variavel)
    return a



print(array_dif([1,3,4,5],[1,3]))
