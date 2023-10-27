dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
totalPagar = (dias * 60.0) + (0.15 * km)
print(f'O total a pagar é de R${totalPagar:.2f}.')