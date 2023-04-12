equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamentos:"))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento:"))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca=input("\nDigite o nome do equipamente que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor...:", valores[indice])
        print("Serial...:", seriais[indice])
