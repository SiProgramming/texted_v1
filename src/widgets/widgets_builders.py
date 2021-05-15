''' Cette classe defini la facon dont chaque ellement du design se cree '''
import os
import tkinter

from src.utils.get_called_method import get_called_methods 
from src.utils.path_utils import PathUtils
from src.utils.get_called_method import pass_right_args
from tkinter import StringVar
from tkinter.font import Font,families
from tkinter import ttk


class WidgetBuilders:
    @staticmethod
    def creer_font_family_et_paper(master):
        # font families
        _police_tuple =families()
        _police_family = StringVar()
        _police_box=ttk.Combobox(master, width=30 ,textvariable=_police_family,state='readonly' )
        _police_box['values']=_police_tuple
        _police_box.current(_police_tuple.index('Arial'))
        # _police_box.grid(row=0,column=0,padx=5, pady=5)        
        
        __zone_text__=tkinter.Text(master, font=("Arial", 12))
        __zone_text__.pack(expand = True, fill = "both")

    @staticmethod
    def creer_editor_style_action_widget(master:tkinter.Label,menu_items_configs:dict):
        ''' Permet la creation de button icon pour la stylisation '''
        for item in menu_items_configs:
            # Pour le cas d'un button
            if item['type']=='icon_btn':
                __icon__btn__image__ = tkinter.PhotoImage(file=PathUtils.obtenir_icon_path(item['icon'])).subsample(20,20)
                #TODO
                print(__icon__btn__image__.width())
                # command=lambda:event_listener.event_generate("<Control c>")
                __icon__btn__= tkinter.Button(master, image=__icon__btn__image__)
                __icon__btn__.grid(row=item['coord']['row'], column=item['coord']['column'], padx=5, pady=5)
        master.pack(side=tkinter.TOP, fill=tkinter.BOTH)

    @staticmethod
    def creer_barre_des_taches_actions_widgets(master:tkinter.Menu,configs,base_class_obj:object):
        ''' creer les elements de la barres des taches '''

        #Pour le cas d'une checkbox
        __sub_menu__=tkinter.Menu(master,tearoff=False)
        master.add_cascade(label=configs['name'].capitalize(),menu=__sub_menu__)
        # print(configs)
        for cascade_item in configs['sub_actions']:
            #Obtenir la fonction
            __icon__img__=''
            if(str(cascade_item['type'])=='checkbox'):
                __sub_menu__.add_checkbutton(label=cascade_item['name'].capitalize(),onvalue=True,offvalue=1,variable=True)
            #Obtenir le lien vers le chemin vers la ressource
            elif(str(cascade_item['icon'])!=''):
                __icon__img__=tkinter.PhotoImage(file=PathUtils.obtenir_icon_path(cascade_item['icon']))
                # __func__=get_called_methods(base_class_obj,cascade_item['command'])
                # __func__(pass_right_args(cascade_item))
                __sub_menu__.add_command(label=str(cascade_item['name']).capitalize(), image=__icon__img__,compound=tkinter.LEFT)

            else :
                # __func__=get_called_methods(base_class_obj,cascade_item['command'])
                # command=__func__(pass_right_args(cascade_item))
                __sub_menu__.add_command(label=str(cascade_item['name']).capitalize(), compound=tkinter.LEFT)
