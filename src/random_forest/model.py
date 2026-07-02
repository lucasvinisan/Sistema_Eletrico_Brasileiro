from src.data_transformation.transformation import tratamento_dados as trans
from src.random_forest import train as t 

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def criar_modelo_random_forest(): 

    previsores, classe, dados_usina = trans()

    x_train, x_test, y_train, y_test  = t.train_test_split(previsores, classe)

    floresta = RandomForestClassifier(n_estimators=100)

    floresta.fit(x_train, y_train)

    floresta.estimator_

    previsoes = floresta.predict(x_test)

    #t.matriz_confusao(y_test, previsoes, floresta)

    t.acuracia(y_test, previsoes)

    t.variavei_importantes(floresta, dados_usina, y_test, previsoes)


