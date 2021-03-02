# Dado o grafo representado na imagem a seguir. Faça um programa que leia um arquivo contendo
#informações do grafo, gere uma matriz de adjacência e calcule o grau de cada vértice.
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
    for i in range( len(vertices) ):
        if (vector == vertices[i]):
            inserido = True
            break
    return inserido

#Iterar para preencher a lista 'vertices'
for i in range( len(arestas) ):
    if(not Inserir(arestas[i].no)):
        vertices.append(arestas[i].no)
    if(not Inserir(arestas[i].noAux)):
        vertices.append(arestas[i].noAux)
vertices = sorted(vertices)

#Preencher matriz com zeros
for i in range( len(vertices) ):
    linha = []
    for j in range( len(vertices) ):
        linha.append(0)
    matrix.append(linha)

#Criando matriz adjacente
for i in range( len(arestas) ):
    matrix[arestas[i].no][arestas[i].noAux] = arestas[i].prioridade
    matrix[arestas[i].noAux][arestas[i].no] = arestas[i].prioridade

#Imprimir matriz
print()
print("Matriz Adjacencia: ")
for i in range( len(matrix) ):
    print(matrix[i])
print()

#Calculando e imprimindo o grau de cada vértice:
print("O grau de cada vértice é: ")
for i in range( len(matrix) ):
    g = 0
    for j in range( len(matrix[i]) ):
        if(matrix[i][j] != 0):
            g += 1
    print('Grau de {}: {}'.format(i,g) )