# Trabalho Prático - Grafos

- **Disciplina**: Grafos
- **Curso**: Ciência da Computação
- **Instituição**: Universidade Federal de São João Del Rei
- **Docente**: Vinícius da Fonseca Vieira
- **Data**: 2° Semestre de 2023

## 📖 Objetivo:

Este trabalho consiste em implementar o algoritmo baseado em colônia de formigas para solucionar o Problema do Caixeiro Viajante (PCV).
Será definida a estrutura de dados que será utilizada para armazenar as formigas, suas soluções e seus respectivos valores de fitness,
além de armazenar ainda a quantidade de feromônio por aresta, de forma que seja viável a atualização desses valores.

## 🖥️ Tecnologias

- **Linguagem**: Python

## 🧠 Bibliotecas Utilizadas

- **Networkx**
- **Matplotlib**
- **Sys**

## 📝 Testes utilizados:
    - [teste1.txt](./teste1.txt): Possui um conjunto de 15 cidades.
    - [teste2.txt](./teste2.txt): Possui um conjunto de 5 cidades.
    - [teste3.txt](./teste3.txt): Possui um conjunto de 7 cidades.

## 🚀 Execução

```
python3 pcv.py nome_do_arquivo_de_entrada.txt
```

⚠️ ***Obs***: nome_do_arquivo_de_entrada.txt é o nome de um dos três arquivos de entrada fornecidos e, após a execução, será salvo uma imagem chamada "grafo.png" 
para uma melhor visualização do grafo. A rota do ciclo de hamilton (solução para o PCV) e custo desse ciclo serão salvos no arquivo de saída "saida.txt".
    
## 🖨️ Saída esperada para cada teste:

- teste1.txt:
```
PCV: ['A', 'M', 'B', 'O', 'I', 'E', 'G', 'C', 'L', 'N', 'J', 'H', 'F', 'D', 'K', 'A']
Custo: 291.0
```

- teste2.txt:
```
PCV: ['1', '4', '5', '2', '3', '1']
Custo: 19.0
```

- teste3.txt:
```
PCV: ['C1', 'C5', 'C3', 'C4', 'C2', 'C6', 'C7', 'C1']
Custo: 114.30000000000001
```
