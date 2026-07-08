from src.decision_tree import train as t
from src.data_transformation import transformation as trans

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd 


def criar_modelo_decision_tree():

    previsores, classe, dados_usina = trans.tratamento_dados()

    x_train, x_test, y_train,  y_test  = t.train_test(previsores, classe)

    ccp_alphas = t.buscar_melhor_alpha(x_train, y_train)

    scores = t.alpha(ccp_alphas, x_train, y_train)

    melhor_indice = np.argmax(scores)
    melhor_alpha = ccp_alphas[melhor_indice]

    #Ávore para metricas do Relatório 
    arvore_podada = t.poda(melhor_alpha)

    arvore_podada.fit(x_train, y_train)

    previsoes = arvore_podada.predict(x_test)

    taxa_acerto = t.acuracia(y_test, previsoes)
    importancias = t.variaveis_importantes(arvore_podada, dados_usina, y_test, previsoes)
    
    #t.matriz_confusao(y_test, previsoes, arvore_podada)

    print(taxa_acerto)
    print(classification_report(y_test, previsoes))

    #Visulização da Árvore para Relatório

    #arvore_relatorio = t.poda_visualizacao_relatorio() 

    #arvore_relatorio.fit(x_train, y_train)

    #t.gerar_arvore(arvore_relatorio)

    