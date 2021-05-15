def get_called_methods(class_objet:object,method_name:str):
    ''' Obtenir la fonction correspondante a une certaine appelation '''
    # AttributeError
    return class_objet.__getattribute__(method_name)

METHOD_WITH_UNEXCEPTED_PARAMS=[
'ouvrir_fichier',
'cacher_afficher_statusbar',
'cacher_afficher_toolbar',
'afficher_apropos',
'imprimer',
'nouveau_espace',
'fermer_fenetre'
]

def pass_right_args(params:dict):
    print(params)
    ''' Cette fonction permet de passer les bons parametres a la fonction correspondant au parametre command '''
    if(params['command'] not in METHOD_WITH_UNEXCEPTED_PARAMS):
        return params
