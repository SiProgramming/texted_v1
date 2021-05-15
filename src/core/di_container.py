''' Ce fichier ci, contient toute les dependances utile a l'application
    ex: instance de configuration
'''
from src.constants.actions_config import ActionConfig
from src.widgets.widgets_builders import WidgetBuilders
from src.utils.actions_methods import EditorActionsMethods

#Instance de configuration
app_config_di_instance=ActionConfig()

#Instance Widget builder 
widget_builder_di_instance=WidgetBuilders()

#Instance de action methods
action_methods=EditorActionsMethods()