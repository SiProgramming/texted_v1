''' Cette classe defini la facon dont chaque ellement du design se cree '''
import os
import tkinter

from utils.get_called_method import get_called_methods 
from utils.path_utils import PathUtils

class WidgetBuilders:

    @staticmethod
    def creer_editor_style_action_widget(master,configs:dict,event_listener):
        ''' Permet la creation de button icon pour la stylisation '''

        # Pour le cas d'un button
        if configs['type']=='icon_btn':
            __icon__btn__image__ = tkinter.PhotoImage(file=os.path.join(os.getcwd(),'Icones', 'copier.png'))
            #TODO
            __icon__btn__= tkinter.Button(master, image=__icon__btn__image__,command=lambda:event_listener.event_generate("<Control c>"))
            __icon__btn__.grid(row=0, column=1, padx=5, pady=5)


    @staticmethod
    def creer_barre_des_taches_actions_widgets(master:tkinter.Menu,configs,base_class_obj:object):
        ''' creer les elements de la barres des taches '''

        #Pour le cas d'une checkbox
        __master_menu__=tkinter.Menu(master,tearoff=False)
        master.add_cascade(label=configs['name'],tearoff=False)
        for cascade_item in configs['sub_actions']:
            #Obtenir la fonction
            __icon__img__=''
            #Obtenir le lien vers le chemin vers la ressource
            if(str(cascade_item['icon'])!=''):
               __icon__img__=PathUtils.obtenir_icon_path(cascade_item['icon'])

            __func__=get_called_methods(base_class_obj,configs['command'])
            __master_menu__.add_command(label=str(configs['name']).capitalize(), image=__icon__img__, compound=tkinter.LEFT, command=__func__(**configs))
        # if configs['type']=='icon-checkbook':
