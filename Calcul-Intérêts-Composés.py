from tkinter import *
from tkinter import ttk
from time import strftime  #Pour récupérer la date courante
from tkinter import messagebox as Msg 

def calcul():
    fen = Toplevel()  #Création de la fenêtre de résultat
    fen.title("Simulation")
    #Mise au centre de la fenêtre
    fen.geometry("%dx%d+%d+%d" % (500,900, (fen.winfo_screenwidth()-500)/2,
                                (fen.winfo_screenheight()-900)/2 ) )
    scrollbar = Scrollbar(fen)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte = Text(fen, width= 40,fg = "blue",yscrollcommand=scrollbar.set)
    #-----------------------------------------------------------------
    #Gestion des calculs
    cap=s3.get()
    i=s.get()/100
    annee = int(strftime("%Y"))
    texte.insert(END,"%d :\t%.2f \n"%(annee,cap))
    texte.insert(END,"-"*40+"\n")
    for n in range(1,(spinval2.get()+1)):
        somme=cap*(1+i)**n
        texte.insert(END,"%d :\t%.2f \n" %(annee+1,somme))
        texte.insert(END,"-"*40+"\n")
        annee+=1
    #------------------------------------------------------------------
    texte.pack(expand = YES,fill=BOTH)
    scrollbar.config(command=texte.yview)
    gain = somme-cap
    pourcent=(gain/cap)*100
    Msg.showinfo(title="mic",message="Gains : %.2f \n soit %.2f "%(gain,pourcent)+
                 " % de la mise de départ")
    ferme = ttk.Button(fen,text = "Quitter", command = fen.destroy)
    ferme.pack(side="top")
    

root =Tk()
root.geometry("400x120")
root.title("Calcul d'intérêts composés")
#--------------------------------------------------------------
frame=Frame(root)
frame.grid(column =0,row=0)
lab = Label(frame,text="Taux de placement")
lab.grid(column=1,row=0)
s = DoubleVar()
ent = Entry(frame, textvariable = s, width = 5)
ent.grid(column =2,row=0)
Label(frame,text="%").grid(column = 3 , row = 0)
frame.grid()
#--------------------------------------------------------------
lab2 = Label(frame,text="Durée du placement en années")
lab2.grid(column=1,row=1)
spinval2 = IntVar()
spin2 = Spinbox(frame, from_=1.0, to=100.0, textvariable=spinval2, width = 4)
spin2.grid(column =2,row=1)
Label(frame,text=" ans").grid(column = 3 , row = 1)
#-----------------------------------------------------------------
lab3 = Label(frame,text="Montant du placement en dollars canadiens")
lab3.grid(column=1,row=2)
s3=IntVar()
ent3=ttk.Entry(frame, width = 10,textvariable = s3, justify = "right")
ent3.grid(column =2,row=2)
Label(frame,text=" $").grid(column = 3 , row = 2)
#-------------------------------------------------------------------
frame4=Frame(root)
frame4.grid(column = 0, row = 5)
calc = ttk.Button(frame4,text ="Calculer", width = 20, command = calcul)
calc.grid(column = 0, row = 3, columnspan = 2)
quitter = ttk.Button(frame4, text ="Quitter", width = 20,command = root.destroy)
quitter.grid(column = 3, row = 3)
frame4.grid()
#------------------------------------------------------------------------
root.mainloop()
