''' 
    Ce fichier contient la definition et implementation de chaque fonction
    utiliser dans l'application ex: enregistrer, ouvrir, etc
'''
import os
import tkinter
from tkinter import * 


class EditorActionsMethods:

    def __init__(self):
        ''' Cette classe defini toute les fonctions utiliser dans l'application, ex: gras, quitter, nouveau '''
        super().__init__()
        self._text_indice=0 # Indice de formatage 
    #doit etre un combox
    def changer_police_taille(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
        ''' Cette methode permet de changer la police d'un texte '''
        zone_texte.config(font=(font_family, texte_police.get()))

    def mettre_en_gras(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
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

    def italique(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
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

    def souligner(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
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

    def colorier_texte(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
        ''' Permet de colorier un texte '''
        try:
            color_var =tkinter.colorchooser.askcolor()
            content="format"+str(self._text_indice)
            zone_texte.tag_add(content,"sel.first","sel.last")
            zone_texte.tag_config(content,foreground=color_var[1])
            self._text_indice+=1
        except:
            None


    def ouvrir_fichier(self,zone_texte:tkinter.Text):
        fichier_ouvert=tkinter.filedialog.askopenfilename(title="OUVRIR...")
        tmp=''
        # je dois fermer la zone de texte pendant la saisie
        if fichier_ouvert=='' or fichier_ouvert==None:
            None
        else:
            try :
                zone_texte.delete("1.0","end")
                fic=open(fichier_ouvert,'r',encoding='utf8')
                tmp=fic.readline()
                j=1.0
                #self.fenetre.quit
                while(tmp!=''):
                    zone_texte.insert(j,tmp)
                    tmp=fic.readline()
                    j=j+1
                fic.close()
            except :
                tkinter.messagebox.showerror("ERREUR","Mauvais format de document...!")


    def cacher_afficher_statusbar(self,zone_texte:tkinter.Text,barre_status:tkinter.Text,scroll_barre_vertical:tkinter.Scrollbar):
        ''' Permet de cacher et afficher la barre des status '''
        #TODO
        if barre_status: # doit etre un boolean
            barre_status.pack_forget()
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            show_statusbar =False
        else:
            barre_status.pack_forget()
            scroll_barre_vertical.pack_forget()
            barre_status.pack(side=BOTTOM)
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            barre_status.pack(fill=BOTH,expand =True)
            show_statusbar=True       


    def cacher_afficher_toolbar(self,zone_texte:tkinter.Text,barre_status:tkinter.Text,scroll_barre_vertical:tkinter.Scrollbar):
        ''' Permet de cacher et afficher la barre des status '''
        #TODO
        if barre_status:
            barre_status.pack_forget()
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            show_toolbar =False

        else:
            barre_status.pack_forget()
            scroll_barre_vertical.pack_forget()
            barre_status.pack(side=TOP,fill=X)
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            barre_status.pack(fill=BOTH,expand =True)
            barre_status.pack(side=BOTTOM)
            show_toolbar = True 


    def barrer_texte(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
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

    def enregister_sous(self, zone_texte: tkinter.Text, font_family: tkinter.StringVar, texte_police):
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

    def fermer_fenetre(self,window:tkinter.Tk):
        ''' Pour fermer la fenetre '''
        window.destroy()
