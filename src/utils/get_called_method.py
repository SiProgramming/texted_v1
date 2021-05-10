def get_called_methods(class_objet:object,method_name:str):
    ''' Obtenir la fonction correspondante a une certaine appelation '''
    return class_objet.__getattribute__(method_name)
