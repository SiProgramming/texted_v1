from tkinter import *
from tkinter import font, filedialog, messagebox, colorchooser
from tkinter import ttk
import tkinter as nTk
import os
import sys


from utils.path_utils import PathUtils
# import win32api#win32print

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("TextEd")
    fenetre.iconbitmap(PathUtils.obtenir_logo_path())
    fenetre.geometry("1080x720")
    fenetre.minsize(width=600, height=400)

    #Theme
    theme_choice = StringVar()

    color_dict = {
        'Light': ("#000000", "#ffffff"),
        'Dark': ("#ffffff", "#000000"),
    }

    zone_de_texte = Text(fenetre, font=("Arial", 12))
    zone_de_texte.focus_set()
    scroll_barre_vertical = Scrollbar(fenetre, orient=VERTICAL)

    barre_outil = Label(fenetre)

    police_tuple = font.families()
    police_family = StringVar()
    police_box = ttk.Combobox(barre_outil, width=30,
                              textvariable=police_family, state='readonly')
    police_box['values'] = police_tuple
    police_box.current(police_tuple.index('Arial'))
    police_box.grid(row=0, column=0, padx=5, pady=5)

    taille_var = IntVar()
    police_taille = ttk.Combobox(
        barre_outil, width=14, textvariable=taille_var, state='readonly')
    police_taille['values'] = tuple(range(8, 80, 2))
    police_taille.current(2)
    police_taille.grid(row=1, column=0, padx=5, pady=5)

    actif_police_family = 'Arial'
    actif_police_taille = 12

    def change_police(event=None):
        global actif_police_family
        actif_police_family = police_family.get()
        zone_de_texte.config(font=(actif_police_family, actif_police_taille))

    def change_taille(event=None):
        global actif_police_taille
        actif_police_taille = police_taille.get()
        zone_de_texte.config(font=(actif_police_family, actif_police_taille))

    police_box.bind("<<ComboboxSelected>>", change_police)
    police_taille.bind("<<ComboboxSelected>>", change_taille)

    def mettre_gras():
        text = zone_de_texte
        bold_font = font.Font(text, text.cget("font"))
        bold_font.configure(weight="bold")
        text.tag_configure("bold", font=bold_font)

        try:

            current_tags = text.tag_names("sel.first")
            if "bold" in current_tags:
                text.tag_remove("bold", "sel.first", "sel.last")
            else:
                text.tag_add("bold", "sel.first", "sel.last")
        except:
            None

    def italique():
        italic_text = zone_de_texte
        italic_font = font.Font(italic_text, italic_text.cget("font"))
        italic_font.configure(slant="italic")
        italic_text.tag_configure("italic", font=italic_font)
        try:

            current_tags = italic_text.tag_names("sel.first")
            if "italic" in current_tags:
                italic_text.tag_remove("italic", "sel.first", "sel.last")
            else:
                italic_text.tag_add("italic", "sel.first", "sel.last")

        except:
            None

    def souligner():
        underline = zone_de_texte
        underline_font = font.Font(underline, underline.cget("font"))
        underline_font.configure(underline=True)
        underline.tag_configure("underline", font=underline_font)
        try:

            current_tags = underline.tag_names("sel.first")
            if "underline" in current_tags:  # gerer les cas ou on ne selectionne rien
                underline.tag_remove("underline", "sel.first", "sel.last")
            else:
                underline.tag_add("underline", "sel.first", "sel.last")
        except:
            None

    def barre():
        text_barre = zone_de_texte
        text_font = font.Font(text_barre, text_barre.cget("font"))
        text_font.configure(overstrike=True)
        text_barre.tag_configure("overstrike", font=text_font)

        try:
            current_tags = text_barre.tag_names("sel.first")
            if "overstrike" in current_tags:  # gerer les cas ou on ne selectionne rien
                text_barre.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                text_barre.tag_add("overstrike", "sel.first", "sel.last")
        except:
            None

    def creer_apropos():
        fnt = Tk()
        fnt.title("A Propos")
        fnt.geometry("300x300+600+400")
        fnt.maxsize(width=300, height=300)
        fnt.minsize(width=300, height=300)

        text = Label(fnt, text="TextEd, est un editeur simple \nconçu par le groupe SIProgramming\ncomposé d'étudiants de licence 3\n en Sciences Informatique d l'année 2020-2021.\nCeux-ci sont: AFRAITANE Ayal; KONAN Obed,\n KAMATE Issiaka,\n BHALE Silvere, KONDOMBO Ismael.", padx=12, pady=20, width=200)
        text.pack(expand=True, fill=BOTH)
        fnt.mainloop()

    def change_theme():
        chose_theme = theme_choice.get()
        print(chose_theme)
        color_tuple = color_dict.get(chose_theme)
        fg_color, bg_color = color_tuple[0], color_tuple[1]
        zone_de_texte.config(background=bg_color, fg=fg_color)

    def enregister_sous():

        #je cree une boite de dialogue dans
        fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetype=(
            ('Text File ', '*txt'), ('Doc File', '*docx'), ('pdf File', '*pdf')))

        if fichier != '':  # cette instruction me permet de gerer le cas ou on cliquerais par megarde sur la touche enregistrer_sous et qu'on
            #voudrait faire une autre action
            fic = open(fichier, "w", encoding='utf8')
            i = 1.0
            tmp = zone_de_texte.get(i, "end")
            while(tmp != ''):  # copie du contenue de la zone de texte dans
                # copie de chaque ligne y compris le caractere de fin de ligne dans tmp
                tmp = zone_de_texte.get(i, "end")
                # pour faire la copie effective dans le fichier_objet fic la variable i sert a modifie
                fic.write(tmp+'\n')
                i += 1  # lindice de la ligne dans la recupperation du contenu de Text
            fic.close()
        else:
            None

    global fichier_ouvert
    fichier_ouvert = ''

    def ouvrir():

        global fichier_ouvert
        fichier_ouvert = filedialog.askopenfilename(title="OUVRIR...")
        tmp = ''
        # je dois fermer la zone de texte pendant la saisie
        if fichier_ouvert == '':
            None
        else:
            try:
                zone_de_texte.delete("1.0", "end")
                fic = open(fichier_ouvert, 'r', encoding='utf8')
                tmp = fic.readline()
                j = 1.0
                #self.fenetre.quit
                while(tmp != ''):
                    zone_de_texte.insert(j, tmp)
                    tmp = fic.readline()
                    j = j+1
                fic.close()

            except:
                messagebox.showerror(
                    "ERREUR", "Mauvais format de document...!")

    def enregistrer():
        global fichier_ouvert

        if fichier_ouvert == '':
            enregister_sous()
        else:
            fic = open(fichier_ouvert, "w", encoding='utf8')
            i = 1.0
            tmp = zone_de_texte.get(i, "end")
            while(tmp != ''):  # copie du contenue de la zone de texte dans
                # copie de chaque ligne y compris le caractere de fin de ligne dans tmp
                tmp = zone_de_texte.get(i, "end")
                # pour faire la copie effective dans le fichier_objet fic la variable i sert a modifie
                fic.write(tmp+'\n')
                i += 1  # lindice de la ligne dans la recupperation du contenu de Text
            fic.close()

    def Nouveau():
        os.popen("python Autre.py")

    fichier_ouvert = ''

    def imprimer():

        nom_doc = fichier_ouvert
        try:
            win32api.ShellExecute(0, "print", nom_doc, None, None, 0)

        except:
            messagebox.showerror(
                "ERREUR", "enregistrer le fichier avant impression ...!")

    im_copier = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'copier.png'))
    copier = Button(barre_outil, image=im_copier,
                    command=lambda: zone_de_texte.event_generate("<Control c>"))
    copier.image = im_copier
    copier.grid(row=0, column=1, padx=5, pady=5)

    im_couper = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'couper.png'))
    couper = Button(barre_outil, image=im_couper,
                    command=lambda: zone_de_texte.event_generate("<Control x>"))
    couper.image = im_couper
    couper.grid(row=0, column=2, padx=5, pady=5)

    im_coller = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'coller.png'))
    coller = Button(barre_outil, image=im_coller,
                    command=lambda: zone_de_texte.event_generate("<Control v>"))
    coller.image = im_coller
    coller.grid(row=1, column=1, padx=5, pady=5)

    im_gras = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'gras.png'))
    gras = Button(barre_outil, image=im_gras, command=mettre_gras)
    gras.image = im_gras
    gras.grid(row=0, column=3, padx=5, pady=5)

    im_italique = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'italic.png'))
    italique = Button(barre_outil, image=im_italique, command=italique)
    italique.image = im_italique
    italique.grid(row=0, column=4, padx=5, pady=5)

    im_souligne = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'souligne.png'))
    souligne = Button(barre_outil, image=im_souligne, command=souligner)
    souligne.image = im_souligne
    souligne.grid(row=0, column=5, padx=5, pady=5)

    im_barre = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'barre.png'))
    barre = Button(barre_outil, image=im_barre, command=barre)
    barre.image = im_barre
    barre.grid(row=0, column=6, padx=5, pady=5)

    # im_indice = nTk.PhotoImage(file=os.path.join(os.getcwd(),'icons', 'indice.png'))
    # indice = Button(barre_outil, image=im_indice)
    # indice.image = im_indice
    # indice.grid(row=0, column=7, padx=5, pady=5)

    # im_exposant = nTk.PhotoImage(file=os.path.join(os.getcwd(),'icons', 'exposant.png'))
    # exposant = Button(barre_outil, image=im_exposant)
    # exposant.image = im_exposant
    # exposant.grid(row=0, column=8, padx=5, pady=5)

    im_parag_gauche = nTk.PhotoImage(
        file=os.path.join(os.getcwd(), 'icons', 'p_gauche.png'))
    parag_gauche = Button(barre_outil, image=im_parag_gauche)
    parag_gauche.image = im_parag_gauche
    parag_gauche.grid(row=1, column=2, padx=5, pady=5)

    im_parag_centre = nTk.PhotoImage(
        file=os.path.join(os.getcwd(), 'icons', 'p_centre.png'))
    parag_centre = Button(barre_outil, image=im_parag_centre)
    parag_centre.image = im_parag_centre
    parag_centre.grid(row=1, column=3, padx=5, pady=5),

    im_parag_droite = nTk.PhotoImage(
        file=os.path.join(os.getcwd(), 'icons', 'p_droite.png'))
    parag_droite = Button(barre_outil, image=im_parag_droite)
    parag_droite.image = im_parag_droite
    parag_droite.grid(row=1, column=4, padx=5, pady=5)

    barre_outil.pack(side=TOP, fill=BOTH)

    barre_statut = Label(fenetre, text="barre de statut")
    barre_statut.pack(side=BOTTOM)

    scroll_barre_vertical.pack(side=RIGHT, fill=Y)
    zone_de_texte.pack(expand=True, fill="both")
    scroll_barre_vertical.config(command=zone_de_texte.yview)
    zone_de_texte.config(yscrollcommand=scroll_barre_vertical.set)

    barre_menu = Menu(fenetre)

    def quit():
        fenetre.destroy()

    nouveau_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'nouveau.png'))
    ouvrir_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'ouvrir.png'))
    enregistrer_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'enregistrer.png'))
    enregistrer_sous_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'enregistrer_sous.png'))
    imprimer_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'imprimer.png'))
    quitter_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'quitter.png'))

    menuFichier = Menu(barre_menu, tearoff=False)
    barre_menu.add_cascade(label="Fichier", menu=menuFichier)
    menuFichier.add_command(
        label="Nouveau", image=nouveau_im, compound=LEFT, command=Nouveau)
    menuFichier.add_command(label="Ouvrir", image=ouvrir_im,
                            compound=LEFT, command=ouvrir)
    menuFichier.add_command(
        label="Enregistrer", image=enregistrer_im, compound=LEFT, command=enregistrer)
    menuFichier.add_command(label="Enregistrer Sous",
                            image=enregistrer_sous_im, compound=LEFT, command=enregister_sous)
    menuFichier.add_command(
        label="Imprimer", image=imprimer_im, compound=LEFT, command=imprimer)
    menuFichier.add_command(
        label="Quitter", image=quitter_im, compound=LEFT, command=quit)

    menuAffichage = Menu(barre_menu, tearoff=False)
    barre_menu.add_cascade(label="Affichage", menu=menuAffichage)

    show_statusbar = BooleanVar()
    show_statusbar.set(True)
    show_toolbar = BooleanVar()
    show_toolbar.set(True)

    def hide_toolbar():
        global show_toolbar
        if show_toolbar:
            barre_outil.pack_forget()
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            show_toolbar = False

        else:
            zone_de_texte.pack_forget()
            scroll_barre_vertical.pack_forget()
            barre_outil.pack(side=TOP, fill=X)
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            zone_de_texte.pack(fill=BOTH, expand=True)
            barre_statut.pack(side=BOTTOM)
            show_toolbar = True

    def hide_statusbar():
        global show_statusbar
        if show_statusbar:
            barre_statut.pack_forget()
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            show_statusbar = False
        else:
            zone_de_texte.pack_forget()
            scroll_barre_vertical.pack_forget()
            barre_statut.pack(side=BOTTOM)
            scroll_barre_vertical.pack(side=RIGHT, fill=Y)
            zone_de_texte.pack(fill=BOTH, expand=True)
            show_statusbar = True

    menuAffichage.add_checkbutton(label="Afficher la barre d'outil",
                                  onvalue=TRUE, offvalue=0, variable=show_toolbar, command=hide_toolbar)
    menuAffichage.add_checkbutton(label="Afficher la barre de staut", onvalue=TRUE,
                                  offvalue=0, variable=show_statusbar, command=hide_statusbar)

    menuTheme = Menu(barre_menu, tearoff=False)
    barre_menu.add_cascade(label="Thème", menu=menuTheme)

    light_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'light.png'))
    dark_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'dark.png'))
    personnaliser_im = nTk.PhotoImage(file=os.path.join(
        os.getcwd(), 'icons', 'personnaliser.png'))

    def change_font_color(color):
        zone_de_texte.configure(bg=color)

    global i
    i = 0

    def colorier():
        global i
        try:
            text_choisi = zone_de_texte
            color_var = colorchooser.askcolor()
            #current_tags=text_choisi.tag_names("sel.first")
            content = "format"+str(i)
            text_choisi.tag_add(content, "sel.first", "sel.last")
            text_choisi.tag_config(content, foreground=color_var[1])
            i = i+1
        except:
            None

    menuTheme.add_radiobutton(label="Light", image=light_im,
                              compound=LEFT, variable=theme_choice, command=change_theme)
    menuTheme.add_radiobutton(label="Dark", image=dark_im,
                              variable=theme_choice, compound=LEFT, command=change_theme)
    menuTheme.add_command(
        label="Personnaliser", image=personnaliser_im, compound=LEFT, command=colorier)

    menuApropos = Menu(barre_menu, tearoff=False)
    barre_menu.add_command(label="A propos", command=creer_apropos)
    fenetre.config(menu=barre_menu)

    fenetre.mainloop()
