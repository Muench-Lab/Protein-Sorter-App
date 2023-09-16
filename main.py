import pandas as pd
from threading import Thread
from tkinter import *
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from functions import *

class MyWindow():
    def __init__(self, parent):

        self.frame = Frame(parent, width=840, height=480)
        self.font = Font(family="Times New Roman", size=16)
        self.request_timeout = 30
        global root
        root=parent
        Label(self.frame, text="Select Localization and Protein file!", fg='#ffe7b6', bg='#b97455', font=self.font).place(x=220, y=15)

        self.fontRadio = Font(family="Times New Roman", size=13)
        self.var = StringVar()


        try:
            self.database = pd.read_excel('./files/database.xlsx')
        except Exception as e:
            print(e)
            self.Message('Error, "database.xlsx" not found!', 'Please put "database.xlsx" into "files" folder.')
            root.destroy()

        ####### Browse label and button ######
        self.browseLabel = Label(self.frame, font=Font(family="Times New Roman", size=14), text="Please, choose a file:")
        self.browseLabel.place(x = 80, y = 80)
        self.browseButton = Button(self.frame, text="Browse", justify=LEFT, font=Font(family="Times New Roman", size=12, weight='bold'), command=self.browse)
        self.browseButton.place(x = 250, y = 75)


        ######## Sorting Buttongs #######
        self.varDecision = StringVar()
        self.all = Radiobutton(root, font=self.fontRadio,  text="Mitochondria Human", value="Mitochondria_Human", variable=self.varDecision)
        self.all.select()
        self.all.place(x=380, y=60)

        self.mito = Radiobutton(root, font=self.fontRadio,  text="Mitochondria Mouse", value="Mitochondria_Mouse", variable=self.varDecision)
        self.mito.place(x=380, y=80)

        self.mim = Radiobutton(root, font=self.fontRadio, text="MIM", value="MIM", variable=self.varDecision)
        self.mim.place(x=380, y=100)

        self.mom = Radiobutton(root, font=self.fontRadio, text="MOM", value="MOM", variable=self.varDecision)
        self.mom.place(x=380, y=120)

        self.ims = Radiobutton(root, font=self.fontRadio, text="IMS", value="IMS", variable=self.varDecision)
        self.ims.place(x=380, y=140)

        self.matrix = Radiobutton(root, font=self.fontRadio, text="Matrix", value="Matrix", variable=self.varDecision)
        self.matrix.place(x=380, y=160)

        self.compartment = Radiobutton(root, font=self.fontRadio, text="All compartment", value="All compartment", variable=self.varDecision)
        self.compartment.place(x=600, y=60)

        self.complex = Radiobutton(root, font=self.fontRadio, text="All complex", value="All complex", variable=self.varDecision)
        self.complex.place(x=600, y=80)

        self.CompartComplex = Radiobutton(root, font=self.fontRadio, text="All compartment + complex", value="All compartment + complex", variable=self.varDecision)
        self.CompartComplex.place(x=600, y=100)

        self.mia40 = Radiobutton(root, font=self.fontRadio, text="Mia40 Substrates", value="Mia40 Substrates", variable=self.varDecision)
        self.mia40.place(x=600, y=120)

        self.interest = Radiobutton(root, font=self.fontRadio, text="Protein of Interest",
                                          value="Protein of Interest", variable=self.varDecision)
        self.interest.place(x=600, y=140)

        self.statusbar = ScrolledText(self.frame, state='disabled')
        self.statusbar.place(x=100, y=200, width=650, height=180)

        # self.runbutton = Button(self.frame, text='RUN', fg='black', bg='#b4e67e',
        #                         font=Font(family="Times New Roman", size=18, weight='bold'), command=self.runbutton_click)
        # self.runbutton.place(x=320, y=410, width=150, height=50)

        self.runbutton = Button(self.frame, text='RUN', fg='black', bg='#b4e67e',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.runbutton_click)
        self.runbutton.place(x=250, y=410, width=150, height=50)

        self.openbutton = Button(self.frame, text='Open', fg='black', bg='#FF5733',
                                font=Font(family="Times New Roman", size=18, weight='bold'), command=self.open_click)
        self.openbutton.place(x=450, y=410, width=150, height=50)


        self.frame.pack()

        self.update_status_box('\n\t >> :: Protein Sorting Bot Started! :: <<\n')
        self.update_status_box('\n------------------------------------------------------------------------------\n')


    def Message(self, title, message):
        messagebox.showinfo(title=title, message=message)

    def update_status_box(self, text):
        self.statusbar.configure(state='normal')
        self.statusbar.insert(END, text)
        self.statusbar.see(END)
        self.statusbar.configure(state='disabled')

    def clear_status_box(self):
        self.statusbar.configure(state='normal')
        self.statusbar.delete(1.0, END)
        self.statusbar.see(END)
        self.statusbar.configure(state='disabled')

    def check_main_thread(self):
        root.update()
        if self.myThread.is_alive():
            root.after(1000, self.check_main_thread)
        else:
            self.x = True

    def open_click(self):
        import os
        os.startfile(f'{self.outputLocation}')

    def browse(self):

        self.filename = filedialog.askopenfile(parent=self.frame, mode='rb', title='Choose a file')
        self.filenamePretify = str(self.filename).split('/')[-1].split("'>")[0]
        if self.filenamePretify == "None":
            self.Message('Error!', 'Please choose a file!')
            return 0
        self.update_status_box(f'\n "{self.filenamePretify}" file is chosen! \n')

        finalFileOutputLocation = str(self.filename).split("'")[1].split(".xlsx")[0]
        if '_MC3' in str(finalFileOutputLocation):
            finalFileOutputLocation= finalFileOutputLocation.replace('_MC3','')
        self.outputLocation =  finalFileOutputLocation+'_MC3.xlsx'
        self.outputLocationPretify = str(self.outputLocation).split('/')[-1].split("'>")[0]

    def runbutton_click(self):

        self.update_status_box(f'\n "{self.varDecision.get()}" is selected! \n')
        self.myThread = Thread(target=self.engine)
        self.myThread.daemon = True
        self.myThread.start()
        root.after(1000, self.check_main_thread)

    def engine(self):
        try:
            self.update_status_box(f'\n The file is reading..! \n')
            self.fileRead = pd.read_excel(self.filename)
        except Exception as e:
            self.update_status_box(f'\n Error is "{e}"! \n')
            self.Message('Error!', 'An Error Occured, please choose a file before run!')
            return 0
        self.update_status_box(f'\n The file is read! \n')

        try:
            self.accessionNum = list(self.fileRead['Accession'])
        except:
            self.accessionNum = list(self.fileRead['Master Protein Accessions'])

        if self.varDecision.get() == 'Mitochondria_Mouse':
            self.update_status_box(f'\n Running..! \n')
            self.data = mito_mouse(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'Mitochondria_Human':
            self.update_status_box(f'\n Running..! \n')
            self.data = mito_human(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'MIM':
            self.update_status_box(f'\n Running..! \n')
            self.data = MIM(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'MOM':
            self.update_status_box(f'\n Running..! \n')
            self.data = MOM(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'IMS':
            self.update_status_box(f'\n Running..! \n')
            self.data = IMS(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'Matrix':
            self.update_status_box(f'\n Running..! \n')
            self.data = Matrix(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'All compartment':
            self.update_status_box(f'\n Running..! \n')
            self.data = mitochondrialLocationsAll(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'All complex':
            self.update_status_box(f'\n Running..! \n')
            self.data = complexSortingAll(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'All compartment + complex':
            self.update_status_box(f'\n Running..! \n')
            self.data = AllCompartComplex(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'Protein of Interest':
            self.update_status_box(f'\n Running..! \n')
            self.data = proteinOfInterest(self.fileRead, self.accessionNum, self.database)
        elif self.varDecision.get() == 'Mia40 Substrates':
            self.update_status_box(f'\n Running..! \n')
            self.data = mia40_subs(self.fileRead, self.accessionNum, self.database)

        self.update_status_box(f'\n Completed..! \n')
        self.update_status_box(f'\n Data is saving..! \n')
        try:
            self.data.to_excel(self.outputLocation, index=False)
            self.update_status_box(f'\n Saved as {self.outputLocationPretify}! \n')
            self.Message('Finished!', 'Application Completed!')
        except Exception as e:
            self.update_status_box(f'\n Error is "{e}"! \n')
            self.Message('Error!', 'An Error Occured, please fix it and rerun!')

if __name__ == '__main__':

    root = Tk()
    # root.iconbitmap('files//icon.ico')
    # updated 01.07.2022
    root.title("Protein Sorter v2.5 by S. Bozkurt")
    root.geometry("840x480")
    root.resizable(0, 0)

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (840 / 2)
    y = (hs / 2) - (480 / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (840, 480, x, y))

    # root.iconphoto(False, tkinter.PhotoImage(file='icon.ico'))
    MyWindow(root)
    root.wm_iconbitmap('files//icon.ico')
    root.mainloop()