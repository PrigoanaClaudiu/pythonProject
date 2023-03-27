from tkinter import *
from tkinter import ttk


class todo:
    # constructor
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')

        # width and height of the window
        self.root.geometry('600x400+300+200')

        # main label
        self.label = Label(self.root, text='To-do-list',
                           font='ariel, 25 bold', width=10,
                           bd=5, bg='blue', fg='black')
        # packing the main label
        self.label.pack(side='top', fill=BOTH)

        # add task label
        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10,
                            bd=5, bg='blue', fg='black')
        # placing the second label
        self.label2.place(x=30, y=60)

        # tasks label
        self.label3 = Label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10,
                            bd=5, bg='blue', fg='black')
        # placing the third label
        self.label3.place(x=340, y=60)

        # listbox -> where all the tasks will be displayed
        self.main_text = Listbox(self.root, height=8,
                                 bd=5, width=20,
                                 font='ariel, 20 italic bold')
        # placing the listbox
        self.main_text.place(x=280, y=100)

        # text -> the text that the user will write
        self.text = Text(self.root, bd=5, height=1, width=25,
                         font='ariel, 10 bold')

        self.text.place(x=20, y=120)

        #reading all the data
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        #add button
        self.button = Button(self.root, text='Add', font='sarif, 20 bold italic',
                             width=10, bd=5, bg='blue', fg='black', command=self.add)
        self.button.place(x=20, y=180)

        #delete button
        self.button = Button(self.root, text='Delete', font='sarif, 20 bold italic',
                             width=10, bd=5, bg='blue', fg='black', command=self.delete)
        self.button.place(x=20, y=300)

    # ADD TASK FUNCTION
    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
            file.seek(0)
            file.close()

        # delete from text, after we insert it
        self.text.delete(1.0, END)

    # DELETE TASK FUNCTION -> delete from .txt and listbox
    def delete(self):
        delete_ = self.main_text.curselection()
        look = self.main_text.get(delete_)
        #delete from .txt
        with open('data.txt', 'r+') as f:
            newf = f.readlines()
            f.seek(0)
            for line in newf:
                item = str(look)
                if item not in line:
                    f.write(line)
                f.truncate()
        #delete from listbox
        self.main_text.delete(delete_)




def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
