=> Nome: Arthur Vieira Silva

=> Execução:
    O arquivo deve ser executado da seguinte maneira:
        python3 pcv.py nome_do_arquivo_de_entrada.txt
    
    Obs: Após a execução, será salvo uma imagem chamada "grafo.png" para uma melhor visualização do grafo. A rota do ciclo de hamilton (solução para o PCV) e custo desse ciclo serão salvos no arquivo de saída "saida.txt".

=> Testes utilizados:
    teste1.txt : Possui um conjunto de 15 cidades.
    teste2.txt : Possui um conjunto de 5 cidades.
    teste3.txt : Possui um conjunto de 7 cidades.

=> Saída esperada para cada teste:
    1.  PCV: ['A', 'M', 'B', 'O', 'I', 'E', 'G', 'C', 'L', 'N', 'J', 'H', 'F', 'D', 'K', 'A']
        Custo: 291.0
    
    2.  PCV: ['1', '4', '5', '2', '3', '1']
        Custo: 19.0
    
    3.  PCV: ['C1', 'C5', 'C3', 'C4', 'C2', 'C6', 'C7', 'C1']
        Custo: 114.30000000000001