import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("JUMIA")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_730=tk.Button(root)
        GButton_730["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_730["font"] = ft
        GButton_730["fg"] = "#000000"
        GButton_730["justify"] = "center"
        GButton_730["text"] = "SUBMIT"
        GButton_730.place(x=80,y=420,width=265,height=30)
        GButton_730["command"] = self.GButton_730_command

        GLabel_460=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_460["font"] = ft
        GLabel_460["fg"] = "#333333"
        GLabel_460["justify"] = "center"
        GLabel_460["text"] = "SEARCH_TERM"
        GLabel_460.place(x=30,y=60,width=94,height=30)

        GLabel_714=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_714["font"] = ft
        GLabel_714["fg"] = "#333333"
        GLabel_714["justify"] = "center"
        GLabel_714["text"] = "PRICE_RANGE"
        GLabel_714.place(x=30,y=110,width=94,height=31)

        GLabel_856=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_856["font"] = ft
        GLabel_856["fg"] = "#333333"
        GLabel_856["justify"] = "center"
        GLabel_856["text"] = "EMAIL"
        GLabel_856.place(x=20,y=170,width=70,height=25)

        GCheckBox_347=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_347["font"] = ft
        GCheckBox_347["fg"] = "#333333"
        GCheckBox_347["justify"] = "center"
        GCheckBox_347["text"] = "Receive email update "
        GCheckBox_347.place(x=20,y=210,width=166,height=47)
        GCheckBox_347["offvalue"] = "0"
        GCheckBox_347["onvalue"] = "1"
        GCheckBox_347["command"] = self.GCheckBox_347_command

        GMessage_293=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_293["font"] = ft
        GMessage_293["fg"] = "#333333"
        GMessage_293["justify"] = "center"
        GMessage_293["text"] = "Results"
        GMessage_293.place(x=50,y=270,width=527,height=139)

        GLineEdit_247=tk.Entry(root)
        GLineEdit_247["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_247["font"] = ft
        GLineEdit_247["fg"] = "#333333"
        GLineEdit_247["justify"] = "center"
        GLineEdit_247["text"] = "Enter Search Term"
        GLineEdit_247.place(x=140,y=60,width=246,height=30)

        GLineEdit_472=tk.Entry(root)
        GLineEdit_472["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_472["font"] = ft
        GLineEdit_472["fg"] = "#333333"
        GLineEdit_472["justify"] = "center"
        GLineEdit_472["text"] = ""
        GLineEdit_472.place(x=140,y=120,width=248,height=30)

        GLineEdit_442=tk.Entry(root)
        GLineEdit_442["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_442["font"] = ft
        GLineEdit_442["fg"] = "#333333"
        GLineEdit_442["justify"] = "center"
        GLineEdit_442["text"] = ""
        GLineEdit_442.place(x=140,y=180,width=249,height=30)

        GLabel_547=tk.Label(root)
        GLabel_547["activebackground"] = "#cb9696"
        GLabel_547["activeforeground"] = "#a34646"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_547["font"] = ft
        GLabel_547["fg"] = "#333333"
        GLabel_547["justify"] = "center"
        GLabel_547["text"] = "WELCOME TO JUMIA PRICE TRACKER "
        GLabel_547.place(x=110,y=10,width=280,height=30)

    def GButton_730_command(self):
        print("command")


    def GCheckBox_347_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
