import tkinter


class Application:

    def __init__(self, titre: str):
        ''' titre represente le titre de l'application '''
        super().__init__()

        # Creation de l'ecran principale
        self.root = tkinter.Tk(titre, titre, titre)
        # Definition de la taille de la fenetre
        self._root_height = int(self.root.winfo_screenheight())
        self._root_width = int(self.root.winfo_screenwidth())
        self.root.geometry(f"{self._root_width}x{self._root_height}+0+0")

        # Creation de la fenetre apropos
        self.about = tkinter.Tk('apropos')
        self._about_height = int(self.root.winfo_screenheight()/3)
        self._about_width = int(self.root.winfo_screenwidth()/4)
        self.about.geometry(f"{self._root_width}x{self._root_height}+0+0")

    def affiche_fenetre_principale(self):
        ''' Cette fonction est permet d'afficher la fenetre '''
        self.root.mainloop()

    def fermer_app(self):
        # TODO
        return None

    def affiche_aprops(self):
        self.about.mainloop()
