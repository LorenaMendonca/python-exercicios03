import moeda 

p = float(input('digite uma preço: R$'))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'o aumento de 10% de {p} é {moeda.aumentar(p, 10)}')
print(f'reduzindo 13% de {p}, fica {moeda.diminuir(p, 13)}')