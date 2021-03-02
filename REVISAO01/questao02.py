listanum = []
maior = 0
menor = 0
media = 0
for c in range(0,10):
    listanum.append(int(input(f'Digite um valor para a {c} posição: ')))
    if c== 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] >maior:
            maior = listanum[c]
        if listanum[c]<menor:
            menor = listanum[c]
print(f'Você digitou os valores{listanum}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print(f'A média é: {sum(listanum)/2}')

