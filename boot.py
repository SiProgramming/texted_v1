''' 
    Ici nous demarrons et initialisons tout, l'execution du logiciel
'''

import os
from src.application.application import Application

if __name__=="__main__":
    print("dde"+os.getcwd())
    __main__windows=Application('TextEd')
    __main__windows.affiche_fenetre_principale()