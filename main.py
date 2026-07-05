from src.decision_tree import model as md_rp 
from src.random_forest import model as md_rf
import webbrowser
import os

def dashboard():
    caminho_arquivo = os.path.abspath("Sistema_Eletrico_Brasileiro/index.html")
    webbrowser.open(f"file://{caminho_arquivo}")

def main():
    #md_rp.criar_modelo_decision_tree()
    #md_rf.criar_modelo_random_forest()
    dashboard()

if __name__ == "__main__":
    main()