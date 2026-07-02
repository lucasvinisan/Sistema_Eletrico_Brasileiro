import pandas as pd 
from sklearn.preprocessing import LabelEncoder 


def tratamento_dados(): 
    
    dados_usina = pd.read_csv('Sistema_Eletrico_Brasileiro/dados/dados_futuros.csv', sep=';', encoding='latin-1')

    #Previsores e classe prevista (Classificação)
    previsores = dados_usina.iloc[:, 0:6].values
    classe = dados_usina.iloc[:,6].values

    #Transformar dados categoricos em númericos
    colunas_categoricas = [0, 1, 2, 3, 4]
    enconders = {}
    

    for i in colunas_categoricas: 
        enconders[i] = LabelEncoder() 
        previsores[:, i] = enconders[i].fit_transform(previsores[:,i])

    
    return previsores, classe, dados_usina