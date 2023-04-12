nome=input("Nome do paciente")
idade=int(input("Qual a idade do paciênte?"))
doença=input("Paciente com suspeita de covid?")

if idade >= 65:
    print("o paciente necessita de atendimento prioritário")
elif idade < 30:
    print("paciente ", nome," pode esperar na fila normal")
else
    print("o paciente não precisa de atendimento prioritário")





