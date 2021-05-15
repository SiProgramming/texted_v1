import tkinter
import os

import src.utils as Utils
from src.constants.actions_config import ActionConfig
from src.widgets.widgets_builders import WidgetBuilders
from src.utils.actions_methods import EditorActionsMethods

class Application:

    def __init__(self, titre: str,action_config:ActionConfig,widget_builder:WidgetBuilders,action_methods:EditorActionsMethods):
        ''' titre represente le titre de l'application

            action_config est une depence pour le chargement des configurations
         '''
        super().__init__()
        #Instance de configuration
        self.__action_config__=action_config
        self.__widget_builder__=widget_builder
        self.__action_methods__=action_methods
        # Creation de l'ecran principale
        self._root = tkinter.Tk(titre.capitalize(), titre, titre)

        # Definition du logo
        self._root.iconbitmap(Utils.PathUtils.obtenir_logo_path())
        # Definition de la taille de la fenetre
        self._root_height = int(self._root.winfo_screenheight())
        self._root_width = int(self._root.winfo_screenwidth())
        self._root.geometry(f"{self._root_width}x{self._root_height}+0+0")

        self._barre_menu_=tkinter.Menu(self._root)
        self._barre_outil_=tkinter.Label(self._root)

        #Ajout barre d'outils
        self.__ajout_barre_outils__()
        self.__ajout_barre_menu__()
        self.__ajout_zone_texte__()

    def affiche_fenetre_principale(self):
        ''' Cette fonction est permet d'afficher la fenetre '''
        self._root.config(menu=self._barre_menu_)
        self._root.mainloop()

    def __ajout_barre_outils__(self):   
        ''' Elle permet de creer automatique tout les elements de la barre d'outils 
            Elle le fait se basant sur proprietes obtenu de la classe action_config
        '''
        _barre_outils_configs_=self.__action_config__.obtenir_menu_bar_action_config()
        for barre_outil_item in _barre_outils_configs_:
            self.__widget_builder__.creer_barre_des_taches_actions_widgets(self._barre_menu_,barre_outil_item,self.__action_methods__)

    def __ajout_barre_menu__(self):
        ''' Elle permet de creer automatique tout les elements de la barre d'outils 
            Elle le fait se basant sur proprietes obtenu de la classe action_config
        '''
        self._barre_menu_items=self.__action_config__.obtenir_editor_style_actions_config()
        self.__widget_builder__.creer_editor_style_action_widget(self._barre_outil_,self._barre_menu_items)

    def __ajout_zone_texte__(self):
        self.__widget_builder__.creer_font_family_et_paper(self._root)

    def fermer_app(self):
        # TODO
        self._about.destroy()
        self._root.destroy()

    def affiche_aprops(self):
        # Creation de la fenetre apropos
        self._about = tkinter.Tk('apropos')
        self._about_height = int(self.root.winfo_screenheight()/3)
        self._about_width = int(self.root.winfo_screenwidth()/4)
        self._about.withdraw()
        self._about.geometry(f"{self._root_width}x{self._root_height}+0+0")
        self._about.mainloop()
