import moeda 

p = float(input('digite uma preço: R$'))
print(f'a metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'o aumento de 10% de {p} é {moeda.aumentar(p, 10, True)}')
print(f'reduzindo 13% de {p}, fica {moeda.diminuir(p, 13)}')