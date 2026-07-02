from sklearn.metrics import confusion_matrix, accuracy_score
from src.data_transformation import transformation as trans
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import pandas as pd


def train_test(previsores, classe): 

    x_train, x_test, y_train, y_test = train_test_split(previsores,
                                                        classe,
                                                        test_size=0.3,
                                                        random_state=0)
    
    return x_train, x_test, y_train, y_test 


#Matriz de Confusão 
def matriz_confusao(y_test, previsoes, floresta):

    ConfusionMatrixDisplay.from_predictions(
            y_test, 
            previsoes,
            display_labels=floresta.classes_,
            cmap='Blues',
            #normalize='True',
            xticks_rotation=45
    )

    plt.title('Matriz de Confusão Não Normalizada')
    plt.tight_layout()
    plt.savefig('matriz_confusao_nao_normalizada.png', dpi=300)
    plt.show()


def acuracia(y_test, previsoes): 

    taxa_acerto = accuracy_score(y_test, previsoes)
    taxa_erro = 1 - taxa_acerto

    return taxa_acerto 


def variavei_importantes(floresta, dados_usina, y_test, previsoes):

    importancias = pd.Series(floresta.feature_importances_, index=dados_usina.columns[:-1])
    print(importancias.sort_values(ascending=False))

    print(classification_report(y_test, previsoes))

