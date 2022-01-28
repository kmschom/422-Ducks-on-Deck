"""
visual.py

Creation Date: Jan. 20, 2022
Last Updated: Jan. 28, 2022

Authors: Kalyn Koyanagi (kek), Liza Richards
TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22
"""

# Import Statements
from tkinter import *
from buildQueue import *
from fileWriter import *


class GraphicalUserInterface:

    def __init__(self):
        # Windows
        self.on_deck = None
        self.menu = None

        # Student name labels
        self.student_1 = None
        self.student_2 = None
        self.student_3 = None
        self.student_4 = None

        # Student names
        self.first = None
        self.second = None
        self.third = None
        self.forth = None

        self.highlight_ind = 0

        self.currentQueue = Queue()
        self.currentQueue.randomize()

    def RightKeystroke(self, event):
        if self.highlight_ind == 3:
            self.highlight_ind = 0
            self.toggleHighlight(self.highlight_ind)

        else:
            self.highlight_ind += 1
            self.toggleHighlight(self.highlight_ind)

    def LeftKeystroke(self, event):
        if self.highlight_ind == 0:
            self.highlight_ind = 3
            self.toggleHighlight(self.highlight_ind)
        else:
            self.highlight_ind -= 1
            self.toggleHighlight(self.highlight_ind)

    def UpperKeystroke(self, event):
        pass

    def LowerKeystroke(self, event):
        pass

    def toggleHighlight(self, highlight_index):
        current_positions = {0: self.student_1, 1: self.student_2, 2: self.student_3, 3: self.student_4}
        old = current_positions.get(self.highlight_ind)
        old.configure(bg='black')
        self.highlight_ind = highlight_index
        new = current_positions.get(self.highlight_ind)
        new.configure(bg='yellow')
        self.on_deck.update()

        return

    def presView(self):
        self.on_deck = Toplevel(height=105, width=750, bg='black')
        deck = self.on_deck
        deck.deiconify()
        deck.title("Ducks on Deck")
        deck.resizable(False, False)
        # Make the display window the topmost window at all times
        deck.attributes('-topmost', 'true')
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.forth = StringVar()

        names = self.ondeck()
        self.first.set(names[0][0].split()[1] + " " + names[0][0].split()[0].replace(',', ''))
        self.second.set(names[1][0].split()[1] + " " + names[1][0].split()[0].replace(',', ''))
        self.third.set(names[2][0].split()[1] + " " + names[2][0].split()[0].replace(',', ''))
        self.forth.set(names[3][0].split()[1] + " " + names[3][0].split()[0].replace(',', ''))

        self.highlight_ind = 0
        self.student_1 = Label(deck, textvariable=self.first)
        self.student_1.pack(padx=12, side=LEFT)
        self.student_1.configure(width=15, wraplength=100, relief='raised', bg='white')

        self.student_2 = Label(deck, textvariable=self.second)
        self.student_2.pack(padx=12, side=LEFT)
        self.student_2.configure(width=15, wraplength=100, relief='raised', bg='white')

        self.student_3 = Label(deck, textvariable=self.third)
        self.student_3.pack(padx=12, side=LEFT)
        self.student_3.configure(width=15, wraplength=100, relief='raised', bg='white')

        self.student_4 = Label(deck, textvariable=self.forth)
        self.student_4.pack(padx=12, side=LEFT)
        self.student_4.configure(width=15, wraplength=100, relief='raised', bg='white')

        deck.bind('<Left>', self.LeftKeystroke)
        deck.bind('<Right>', self.RightKeystroke)
        deck.bind('<Up>', self.UpperKeystroke)
        deck.bind('<Down>', self.LowerKeystroke)

        deck.update()

    def ondeck(self):
        names = []
        for stu in self.currentQueue:
            names.append(stu)
        return names[0:4]

    def UserExportDaily(self):
        # exportDailyLog()
        pass

    def UserExportTerm(self):
        exportSumPerf(self.currentQueue)

    def MenuDisplay(self):
        self.menu = Tk()  # Toplevel()  # " Ducks on Deck: Menu ")
        menu = self.menu
        menu.title(" Ducks on Deck: Menu ")
        # Sets window size
        menu.geometry("250x300")
        # Prevent the menu window from being resized
        menu.resizable(False, False)

        # Set background color
        menu.configure(bg='black')

        # Create menu buttons here
        export_daily_button = Button(menu, text="Export Daily Data", font=("MS Sans Serif", 20),
                                     command=self.UserExportDaily, bg="white", width=15)
        export_daily_button.place(x=28, y=20)
        export_total_button = Button(menu, text="Export Performance\n Summary", font=("MS Sans Serif", 20),
                                     command=self.UserExportTerm, bg="white", width=15)
        export_total_button.place(x=28, y=65)
        # Import class data
        import_button = Button(menu, text="Import Roster", font=("MS Sans Serif", 20),
                               bg="white",
                               width=15)  # command=UserImport,
        import_button.place(x=28, y=135)
        # Button to exit session
        exit_button = Button(menu, text="            Exit           ", font=("MS Sans Serif", 20), command=self.exit_,
                             bg="white", width=15)
        exit_button.place(x=28, y=190)
        # Button to create a new session
        session_button = Button(menu, text="    New Session   ", font=("MS Sans Serif", 20), command=self.presView,
                                bg="white", width=15)
        session_button.place(x=28, y=235)
        menu.mainloop()

    def exit_(self):
        sys.exit()

    def UpdateDeck(self, current_ducks):
        self.first.set(current_ducks[0])
        self.second.set(current_ducks[1])
        self.third.set(current_ducks[2])
        self.forth.set(current_ducks[3])
        self.on_deck.update()

        return


if __name__ == "__main__":
    screen = GraphicalUserInterface()
    screen.MenuDisplay()
