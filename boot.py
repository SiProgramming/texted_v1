''' 
    Ici nous demarrons et initialisons tout, l'execution du logiciel
'''

import os
from src.application.application import Application
import src.core.di_container as DI


if __name__=="__main__":
    __main__windows=Application('TextEd',DI.app_config_di_instance,DI.widget_builder_di_instance,DI.action_methods)
    __main__windows.affiche_fenetre_principale()