preço = float(input('Qual é  preço do produto? R$'))
desconto = preço*0.05
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${preço-desconto:.2f}.')