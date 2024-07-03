print('1. Hamburguer - R$ 10,00')
print('2. batata frita - R$ 5,00')
print('3. refrigerante - R$ 4,00')
print('4. sorvete - R$ 2,00')
n1 = 10
n2 = 5
n3 = 4
n4 = 2
pedido = int(input('\nescreva o numero do seu pedido: '))
qunt = int(input('\ndigite  a quantidade: '))
nome = str(input('\nqual seu nome: '))
if pedido == 1:
    rst = n1 * qunt
    tempo = 5
if pedido == 2:
    rst = n2 * qunt
    tempo = 2
if pedido == 3:
    rst = n3 * qunt
    tempo = 1
if pedido == 4:
    rst = n4 * qunt
    tempo = 1
dem = qunt * tempo
if dem >= 60:
    dem = dem / 60 
    

print('\n',nome, 'seu pedido estará pronto em ', dem)
print('\ntotal do pedido: R$',rst)