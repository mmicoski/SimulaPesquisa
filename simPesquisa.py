# -*- coding: cp1252 -*-
''' Simulação de coleta de amostras para definir 
'''


import random


# simula dados: 10000 veiculos com 10% de ocorrência de uma característica
qt_veiculos = 10000
p_caract = 0.1

veiculos = [1*(random.random() < p_caract) for i in range(qt_veiculos)]


# mostra no gráfico
if 1:
    from matplotlib import pyplot as plt
    import math

    cores = ['orange', 'green']
    
    ind = range(qt_veiculos)
    
    base = int(math.sqrt(qt_veiculos))
    if base*base < qt_veiculos:
        base += 1
        
    x = [i/base for i in ind]
    y = [i%base for i in ind]
    cor = [cores[i] for i in veiculos]

    plt.scatter(x, y ,c=cor, s=3)
    plt.show()


# simula várias pesquisas
qt_coletas = 100
resultados = []


for i in range(qt_coletas):
    # executa a pesquisa
    qt_veiculos_pesquisados = 964

    pesquisados = {}
    while len(pesquisados) < qt_veiculos_pesquisados:
        ind = int(qt_veiculos*random.random())
        pesquisados[ind] = veiculos[ind]

    pesquisados = pesquisados.values()
    resultados.append(float(sum(pesquisados))/qt_veiculos_pesquisados)


# mostra resultados    
if 1:
    from matplotlib import pyplot as plt
    ind_coleta = list(range(qt_coletas))

    proporcao_real = float(sum(veiculos))/len(veiculos)
    valor_real = [proporcao_real for i in ind_coleta]

        
    plt.plot(ind_coleta, valor_real, color = 'red', label="valor real")
    plt.scatter(ind_coleta, resultados, color='blue', label="valor medido")

    # barras de intervalo
    margem = 0.03  # definida com o tamanho da amostra
    ip = 0
    p = resultados[ip]
    plt.plot([ip, ip],[p-margem,p+margem], color = 'gray', label='margem de erro')

    for ip in range(1,len(resultados)):
        p = resultados[ip]
        plt.plot([ip, ip],[p-margem,p+margem], color = 'gray')
        
    plt.xlabel('#coleta')
    plt.ylabel(u'proporção de ônibus')
    plt.title(u'pesquisa em fração da população')
    plt.ylim((0.06, 0.16))
    plt.legend()
    plt.show()
              


