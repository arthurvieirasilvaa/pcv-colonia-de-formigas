"""
    Trabalho de Grafos: PCV utilizando colônia de formigas.
    
    Nome: Arthur Vieira Silva.    
"""

import networkx as nx
import matplotlib.pyplot as plt
import sys

Grafo = nx.Graph()

# Algumas constantes utilizadas:
NUMERO_ITERACOES = 20
ALFA = 1 # Influência do feromônio.
BETA = 5 # Influência do custo do caminho no cálculo da probabilidade.

Q = 100
P = 0.5 # 0 < p <= 1 é a taxa de evaporação de feromônio.
FEROMONIO_INICIAL = 10 ** -6 # Quantidade de feromônio inicial de cada aresta.

# Função utilizada para ler o arquivo de entrada fornecido:
def ler_arquivo(entrada):
    # Verificando se o arquivo de entrada existe:
    try:
        # Lendo os vértices do arquivo de entrada "entrada.txt" fornecido:
        with open(entrada, "r") as input:
            for linhas in input:
                linha = linhas.strip().split()
                
                if len(linha) == 3:
                    v1, v2, distancia = linha 
                    # Adicionando uma aresta entre os vértices de cada linha:
                    Grafo.add_edge(v1, v2, weight=float(distancia)) 
    # O arquivo de entrada não foi encontrado:
    except FileNotFoundError:
        print("ERRO! O arquivo {} não foi encontrado.".format(entrada))
        sys.exit(1)

# Função utilizada para desenhar e plotar o grafo lido:        
def desenhar_grafo(Grafo):
    options = {
        "font_size": 4,
        "font_weight": "bold",
        "font_color": "#FBFBFF",
        "node_size": 50,
        "node_color": "#351431",
        "edge_color": "#E4572E"
    }
    
    pos = nx.spring_layout(Grafo)
    
    # Desenhando o grafo lido no arquivo de entrada:
    nx.draw(Grafo, **options, with_labels=True, pos=pos) 

    edge_labels = dict([((u,v,),d['weight'])

    for u, v, d in Grafo.edges(data=True)])
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels, font_size=options["font_size"])

    plt.savefig("grafo.png")  # Salvando o grafo desenhado como uma imagem "grafo.png".
    plt.show()

# Função utilizada para calcular a probabibilidade da formiga escolher a próxima cidade:
def funcao_probabilidade(Grafo, feromonio, i, mapeamento, cidades_restantes):  
    soma = 0
    v1 = mapeamento[i]
    # Calculando o somatório do denominador da função de probabilidade:
    for j in cidades_restantes:
        distancia = Grafo[i][j]['weight']
        v2 = mapeamento[j]
        soma += ((feromonio[v1][v2] ** ALFA) * (1 / distancia) ** BETA)
    
    # Atualizando a matriz de probabilidade:
    for j in list(Grafo.nodes()):
        if i != j:
            v2 = mapeamento[j]
            distancia = Grafo[i][j]['weight']
            if soma != 0:
                probabilidade[v1][v2] = ((feromonio[v1][v2] ** ALFA) * (1 / distancia) ** BETA) / soma
        
    return probabilidade

# Função utilizada para calcular o custo de um dado caminho S:
def calcular_distancia(Grafo, S):
    l = 0
    for i in range(M-1):
        l += Grafo[S[i]][S[i+1]]['weight']
            
    return l

# Função utilizada para atualizar a matriz de feromônio:
def atualizar_feromonio(Grafo, mapeamento, feromonio, S):
    variacao_feromonio = feromonio # Matriz varição de feromônio que atualizará os feromônios.
    somatorio = 0
    
    for k in range(len(S)):
        # Calculando o custo total caminho S:
        ciclo = S[k]
        l = calcular_distancia(Grafo, ciclo)
        
        # Conjunto de arestas presentes no caminho S:
        arestas_s = []
        for i in range(M-1):
            arestas_s.append((ciclo[i], ciclo[i+1]))
        
        for i in list(Grafo.nodes()):
            v1 = mapeamento[i]
            for j in list(Grafo.nodes()):
                v2 = mapeamento[j]
                # Se a aresta (i, j) está presente nas arestas da solução S:
                if (i, j) in arestas_s:
                    variacao_feromonio[v1][v2] = Q / l 
                # Se a aresta (i, j) não está presente nas arestas da solução S:
                else:
                    variacao_feromonio[v1][v2] = 0
                
                somatorio += variacao_feromonio[v1][v2]
               
        # Atualiza a matriz de feromônio:
        for i in range(M):
            for j in range(M):
                feromonio[i][j] = ((1 - P) * feromonio[i][j]) + somatorio
    
    return feromonio

# Função utilizada para encontrar a solução para o problema:            
def criar_caminho(Grafo, S, feromonio):
    # Utilizando um dicionário para mapear os vértices de acordo com os seus índices:
    mapeamento = {vertice: indice for indice, vertice in enumerate(Grafo.nodes())}
    lmin = float('inf') # O custo mínimo inicial é infinito.
    smin = [] # O ciclo mínimo inicial está vazio.
    
    for _ in range(NUMERO_ITERACOES):
        for k in range(M):
            # Conjunto de cidades com uma determinada formiga ainda não visitou
            cidades_restantes = list(mapeamento.keys())
            
            # Vértice de partida será sempre o primeiro do conjunto de cidades:
            partida = cidades_restantes[0]
            proxima_cidade = partida
            # Enquanto a formiga k não construir a viagem S[k]:
            while cidades_restantes:
                # A próxima cidade será escolhida pela função de probabilidade:
                i = proxima_cidade 
                
                cidades_restantes.remove(i) # Removemos a cidade.
                S[k].append(i) # Adicionamos a cidade a viagem S[k].
                probabilidade = funcao_probabilidade(Grafo, feromonio, i, mapeamento, cidades_restantes)
                
                melhor_probabilidade = 0
                v1 = mapeamento[i]
                # Escolhemos a próxima cidade:
                for j in cidades_restantes:
                    v2 = mapeamento[j] 
                    if probabilidade[v1][v2] > melhor_probabilidade:
                        proxima_cidade = j
                        melhor_probabilidade = probabilidade[v1][v2]
            # Removemos a próxima cidade das cidades que ainda não foram visitadas:         
            if proxima_cidade in cidades_restantes:
                cidades_restantes.remove(proxima_cidade)
            
            # Adicionamos a próxima cidade a viagem S[k]:
            if proxima_cidade not in S[k]:
                S[k].append(proxima_cidade)

            # Calculamos a distância da viagem S[k]:
            l = calcular_distancia(Grafo, S[k])
            if l < lmin:
                smin = S[k]
                lmin = l
        
        # Depois que todas as formigas construíram suas viagens, atualizamos o feromônio:
        feromonio = atualizar_feromonio(Grafo, mapeamento, feromonio, S)
        S = [[] for _ in range(M)]
    
    smin.append(smin[0])
    return smin            
               
# Função utilizada para salvar a solução no arquivo de saída:
def arquivo_saida(Grafo, smin):
    output = open("saida.txt", "w") # Criando um arquivo de saída chamado "saida.txt" 
    
    # Escrevendo no arquivo de saída:
    output.write("PCV: {}\n".format(smin))
    l = calcular_distancia(Grafo, smin) 
    l += Grafo[smin[M-1]][smin[M]]['weight']
    output.write("Custo: {}\n".format(l))
    
    output.close() # Fechando o arquivo de saída escrito.
    
if len(sys.argv) != 2:
    print("Execute da seguinte maneira: python3 pcv.py nome_do_arquivo_de_entrada.txt")
    sys.exit(1)
entrada = sys.argv[1]    
ler_arquivo(entrada)

desenhar_grafo(Grafo)

M = nx.number_of_nodes(Grafo) # Número de formigas utilizadas.

# Lista para construir as viagens de cada formiga:
S = [[] for _ in range(M)]

# Inicializando a matriz de feromônio para cada aresta do grafo:
feromonio = [[FEROMONIO_INICIAL for _ in range(M)] for _ in range(M)]

# Inicializando a matriz de probabilidade para cada aresta do grafo:
probabilidade = [[0 for _ in range(M)] for _ in range(M)]

smin = criar_caminho(Grafo, S, feromonio)
arquivo_saida(Grafo, smin)