num = int(input('Informe um número: '))
print(f'Analisando o número {num}')
u = num %10
print(f'Unidade: {u}')
u = num //10 %10
print(f'Dezena: {u}')
u = num // 100 %10
print(f'Centena: {u}')
u = num // 1000 %10
print(f'Milhar: {u}')

