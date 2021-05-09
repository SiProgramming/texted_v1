''' 
    Ce fichier contient la definition et implementation de chaque fonction
    utiliser dans l'application ex: enregistrer, ouvrir, etc
'''
import os
import tkinter


class EditorActionsMethods:

    def __init__(self):
        super().__init__()

    def changer_police_taille(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet de changer la police d'un texte '''
        zone_texte.config(font=(font_family, texte_police.get()))

    def mettre_en_gras(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet de mettre un texte en gras '''
        bold_font = tkinter.Font(zone_texte, zone_texte.cget("font"))
        bold_font.configure(weight="bold")
        zone_texte.tag_configure("bold", font=bold_font)
        try:
            current_tags = zone_texte.tag_names("sel.first")
            if "bold" in current_tags:
                zone_texte.tag_remove("bold", "sel.first", "sel.last")
            else:
                zone_texte.tag_add("bold", "sel.first", "sel.last")
        except:
            None

    def italique(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet de mettre un texte en italic '''
        italic_font = tkinter.Font(zone_texte, zone_texte.cget("font"))
        italic_font.configure(slant="italic")
        zone_texte.tag_configure("italic", font=italic_font)
        try:
            current_tags = zone_texte.tag_names("sel.first")
            if "italic" in current_tags:
                zone_texte.tag_remove("italic", "sel.first", "sel.last")
            else:
                zone_texte.tag_add("italic", "sel.first", "sel.last")
        except:
            None

    def souligner(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet de souligner un texte '''
        underline_font = tkinter.Font(zone_texte, zone_texte.cget("font"))
        zone_texte.configure(underline=True)
        zone_texte.tag_configure("underline", font=underline_font)
        try:
            current_tags = zone_texte.tag_names("sel.first")
            if "underline" in current_tags:  # gerer les cas ou on ne selectionne rien
                zone_texte.tag_remove("underline", "sel.first", "sel.last")
            else:
                zone_texte.tag_add("underline", "sel.first", "sel.last")
        except:
            None

    def barrer_texte(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet de barrer un texte '''
        text_font = tkinter.Font(zone_texte, zone_texte.cget("font"))
        text_font.configure(overstrike=True)
        zone_texte.tag_configure("overstrike", font=text_font)

        try:
            current_tags = zone_texte.tag_names("sel.first")
            if "overstrike" in current_tags:  # gerer les cas ou on ne selectionne rien
                zone_texte.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                zone_texte.tag_add("overstrike", "sel.first", "sel.last")
        except:
            None

    def afficher_apropos(self):

        # TODO
        return None

    def enregister_sous(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police: tkinter.Combobox):
        ''' Cette methode permet d'enregistrer un document '''
        # je cree une boite de dialogue dans
        # TODO
        extension_supportes = [('Text File ', '*txt'), ]
        fichier = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt", filetype=(('Text File ', '*txt')))

        # cette instruction me permet de gerer le cas ou on cliquerais par megarde sur la touche enregistrer_sous et qu'on
        if fichier != '' or fichier != None:
            # voudrait faire une autre action
            fic = open(fichier, "w", encoding='utf8')
            i = 1.0
            tmp = zone_texte.get(i, "end")
            while(tmp != ''):  # copie du contenue de la zone de texte dans
                # copie de chaque ligne y compris le caractere de fin de ligne dans tmp
                tmp = zone_texte.get(i, "end")
                # pour faire la copie effective dans le fichier_objet fic la variable i sert a modifie
                fic.write(tmp+'\n')
                i += 1  # lindice de la ligne dans la recupperation du contenu de Text
            fic.close()
        else:
            None

    def imprimer(self, chemin_doc: str):
        ''' Permet d'imprimer un document '''
        try:
            win32api.ShellExecute(0, "print", chemin_doc, None, None, 0)
        except:
            # TODO
            tkinter.messagebox.showerror(
                "ERREUR", "enregistrer le fichier avant impression ...!")

    def nouveau_espace(self):
        ''' Pour ouvrir une autre instance de l'editeur '''
        os.popen("python Autre.py")
