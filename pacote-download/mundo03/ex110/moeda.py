def aumentar(preço=0, taxa = 0, forma=False):
    res = preço + (preço * taxa/100) 
    return res if forma is False else moeda(res)

def diminuir(preço = 0, taxa = 0, forma=False):
    res = preço - (preço * taxa/100)
    return res if forma is False else moeda(res)

def dobro(preço = 0, forma=False):
    res = preço * 2
    return res if forma is False else moeda(res)

def metade(preço = 0, forma=False):
    res = preço / 2
    return res if forma is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0,taxa1=0,taxa2=0):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f'preço analisado: \t{moeda(preço)}')
    print(f'dobro do preço: \t{dobro(preço, True)}')
    print(f'metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preço, taxa2, True)}')
    print('-'*35)