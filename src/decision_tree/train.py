from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.tree import export_graphviz
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def train_test(previsores, classe):
     
    x_train, x_test, y_train,  y_test = train_test_split(
        previsores,
        classe,
        test_size=0.3,
        random_state=0,
        stratify=classe
    ) 

    return x_train, x_test, y_train,  y_test    

def buscar_melhor_alpha(x_train, y_train):
    
    arvore_base = DecisionTreeClassifier(random_state=2, class_weight='balanced')
    path = arvore_base.cost_complexity_pruning_path(x_train, y_train)
    ccp_alphas = path.ccp_alphas

    return ccp_alphas


def alpha(ccp_alphas, x_train, y_train):

    scores = []

    for alpha in ccp_alphas:
        clf = DecisionTreeClassifier(random_state=2, ccp_alpha=alpha, class_weight='balanced')
        s = cross_val_score(clf, x_train, y_train, cv=5).mean()
        scores.append(s)
    
    return scores

def poda(melhor_alpha):

    arvore_podada = DecisionTreeClassifier(
                random_state=2, 
                ccp_alpha=melhor_alpha,
                max_depth=8, 
                min_samples_split=100,
                max_leaf_nodes=10,
                class_weight='balanced')
    
    return arvore_podada 

#Matriz de Confusão 
def matriz_confusao(y_test, previsoes, arvore):

    ConfusionMatrixDisplay.from_predictions(
            y_test, 
            previsoes,
            display_labels=arvore.classes_,
            cmap='Blues',
            normalize='true',
            xticks_rotation=45
    )

    plt.title('Matriz de Confusão Normalizada')
    plt.tight_layout()
    plt.savefig('matriz_confusao_normalizada_Arvore_de_Decisão.png', dpi=300)
    plt.show()



def acuracia(y_test, previsoes): 

    taxa_acerto = accuracy_score(y_test, previsoes)
    taxa_erro = 1 - taxa_acerto

    return taxa_acerto 


def variavei_importantes(arvore, dados_usina, y_test, previsoes):

    importancias = pd.Series(arvore.feature_importances_, index=dados_usina.columns[:-1])
    print(importancias.sort_values(ascending=False))

    print(classification_report(y_test, previsoes))


def gerar_arvore(arvore_podada):

    dot_data = export_graphviz(
        arvore_podada, 
        out_file=None, 
        feature_names=['NomFonteCombustivel', 'SigUFPrincipal', 'SigTipoGeracao', 'MdaGarantiaFisicaKw', 'DscFonteCombustivel', 'DscOrigemCombustivel'],  
        class_names=['Autorização', 'Concessão', 'Registro'], 
        filled=True,          
        rounded=True,         
        special_characters=True
    )

    graph = graphviz.Source(dot_data)
    graph.render("arvore_decisao_report", format="png", cleanup=True)

    print("Imagem 'REP Tree.png' gerada com sucesso!")
