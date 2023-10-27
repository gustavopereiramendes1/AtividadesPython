largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
m2 = largura * altura
qnt_tinta = m2/2
print(f'Sua parede tem a dimensão de {largura}x{altura} e a sua área é de {m2}m².')
print(f'Para pintar essa parede, você precisará de {qnt_tinta}L de tinta.')