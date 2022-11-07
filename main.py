alturas = []

print("Digite a altura dos 10 alunos da sala e pressione enter entre os valores.")
for i in range(10):
    alturas.append(float(input("Altura do aluno " + str(i+1) + ":\n")))
print(alturas)
media = sum(alturas)/len(alturas)
print(media)

quantidade_alunos = 0
for i in range(10):
    if alturas[i] < media:
        quantidade_alunos = quantidade_alunos + 1

print (str(quantidade_alunos) + " alunos possuem altura inferior ou igual a média de altura dos alunos")
