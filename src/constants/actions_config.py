''' 
    Ce fichier contient tout les actions que pourra realiser l'application
    et chaque action est associer a une fonction et une icon si necessaire
'''
import json
import os
from utils.path_utils import PathUtils


class AppActionsConfig:

    def __init__(self):
        ''' Initialiser toute les configurations de l'application 
            ex: les actions de l'application
        '''
        super().__init__()
        __json_config_file__=open(PathUtils.obtenir_path_from_root(os.path.join('src','constants','actions_names.json')),'r')
        self.__configs__=json.load(__json_config_file__)


    def obtenir_editor_style_actions(self):
        ''' Obtenir les configurations relatives a la stylisation '''
        return self.__configs__['editor_style_actions']


    def obtenir_menu_bar_action(self):
        ''' Obtenir les configurations relatives a la barre de menu '''
        return self.__configs__['menu_bar_action']
    
te=AppActionsConfig()
print(te.__configs__)