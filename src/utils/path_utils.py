''' 
    Utilitaire pour faciler l'acces au ressource du projet, ex: image, logo, icon, etc ...
'''

import os

class PathUtils:

    @staticmethod
    def obtenir_root_path():
        return os.getcwd()

    @staticmethod
    def obtenir_path_from_root(sub_path:str):
        return os.path.join(os.getcwd(),sub_path)
    
    @staticmethod
    def obtenir_icon_path(icon_name:str):
        return os.path.join(os.getcwd(),"assets","icons",icon_name)
    
    @staticmethod
    def obtenir_logo_path():
        return os.path.join(os.getcwd(),"assets","images","logo.ico")
    