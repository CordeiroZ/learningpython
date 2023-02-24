print('Descubra seu IMC:')

altura = int(input("Defina a altura: "))
peso = int(input("Defina seu peso: "))
altura = altura*altura
peso = peso*10000


imc = peso/altura
imc = round(imc, 2)
print(imc)

if(imc < 18.4):
    print("Abaixo do peso normal")
if(18.5 < imc < 24.9):
    print("Normal")
if(25 < imc < 29.9):
    print('Sobrepeso')
if(30 < imc < 39.9):
    print('Obesidade')
if(imc > 40):
    print('Obesidade Grave')
