# Dado o grafo anterior, faça um programa que leia um vértice e retorne os vértices adjacentes a ele. A lista que vai receber as arestas
arestas = []
vertices = []
matrix = []


class Grafo:
    def __init__(self, no, noAux, prioridade):
        self.no = no
        self.noAux = noAux
        self.prioridade = prioridade


grafo = open('lArestas.txt', 'r')
for i in grafo:
    linha = i.split()
    arestas.append(Grafo(int(linha[0]), int(linha[1]), int(linha[2])))
grafo.close()


def Inserir(vector):
    inserido = False
    for i in range(len(vertices)):
        if (vector == vertices[i]):
            inserido = True
            break
    return inserido


for i in range(len(arestas)):
    if(not Inserir(arestas[i].no)):
        vertices.append(arestas[i].no)
    if(not Inserir(arestas[i].noAux)):
        vertices.append(arestas[i].noAux)
vertices = sorted(vertices)

# Preencher matrix com zeros
for i in range(len(vertices)):
    linha = []
    for j in range(len(vertices)):
        linha.append(0)
    matrix.append(linha)

# Criando matrix adjacente
for i in range(len(arestas)):
    matrix[arestas[i].no][arestas[i].noAux] = arestas[i].prioridade
    matrix[arestas[i]
           .noAux][arestas[i].no] = arestas[i].prioridade

    # Ler o vértice
try:
    v = int(input("Informe o vertice desejado: "))
except ValueError as vet:
    print("Erro: {}".format(vet))
    exit()

#Verificar se o vértice existe
exist = False
for i in range( len(vertices)):
    if v == vertices[i]:
        exist = True
        break
if exist == False:
    print("O vertice solicitado não existe")
    exit()

#Retornar os adjacentes
adj = []
for i in range(len (matrix[v]) ):
    if matrix[v][i] != 0:
        adj.append(i)
print("Os valores correspondentes aos vertices adjacentes são: ")
print(adj)