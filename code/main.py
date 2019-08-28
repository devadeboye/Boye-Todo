#!C:\Users\Adeboye Emmanuel\AppData\Local\Programs\Python\Python36-32\python.exe
from todo2 import Todo
import tkinter as tk

class TodoApp:
    def __init__(self):
        """
        constructor for the app
        """
        self.t_list = Todo()
        # main window
        self.root = tk.Tk()

        # title
        self.root.title('3TM')
        self.root.config(pady=2, padx=2, )
        
        # scrollbar
        self.scroll = tk.Scrollbar(self.root, orient = 'vertical')
        # add the scrollbar to the main window
        self.scroll.pack(side='right', fill='y')
        
        # list box to contain the list
        self.my_list = tk.Listbox(self.root, selectmode = 'extended',\
            yscrollcommand = self.scroll.set, width=540, font=('courier', 11))#, 'bold'))
        
        # set the window dimension
        self.root.geometry('{}x{}'.format(540, 250))
        # make the main window unresizeable
        self.root.resizable(width=False, height=False)

        #////////////////////////////////////////////////
        #/////  UPPER SECTION OF THE APP STARTS HERE ////
        #////////////////////////////////////////////////

        # container for the upper section of the app
        self.input_container = tk.Frame(self.root,)

        # create a label
        self.label = tk.Label(self.input_container, text = 'Enter Task:', font=("courier", 10))
        # arrange in a grid
        self.label.grid(row=0, column=0)

        # create text box
        self.user_input = tk.Entry(self.input_container, width=34)
        # arrange textbox in a grid
        self.user_input.grid(row=0, column=1)
        
        # ---------------------------------------------------
        # create the Add button
        tk.Button(self.input_container, text = 'Add', font=("courier", 10),
            command = self.__get_input_value).grid(row=0, column=2)

        # button to remove completed task
        self.mark_done = tk.Button(self.input_container, text="Completed", 
            font=("courier", 10), command=self.__done)
        # add to input_container grid
        self.mark_done.grid(row=0, column=3)

        # add input_container to the main window
        self.input_container.pack()
        #////////////////////////////////////////////////
        #/////  UPPER SECTION OF THE APP ENDS HERE //////
        #////////////////////////////////////////////////

        # Task list header
        tl_header = tk.Label(self.root, text='List of activities', 
            font=("courier", 16))
        tl_header.pack()

        # update the list
        self.__update_list()

        
    
    
    #get item from the db
    def __get_input_value(self):
        """
        get input from users and insert into the db
        """
        # get user value of user entry
        foo = tk.Entry.get(self.user_input)
        # insert item into db
        self.t_list.insert_item(foo)
        # clear the content of the entry box
        self.user_input.delete(0, 'end')
        # default text value
        #self.user_input.insert(0, 'Enter task here')

        # remove all item in the listbox
        self.my_list.delete(0, 'end')
        # update the content of the listbox
        self.__update_list()
        self.label.setvar('')

    def __update_list(self):
        """
        updates the content of the listbox
        """
        for item in self.t_list.view_all():
            # insert item into the listbox
            self.my_list.insert('end',' - '+item[1])
        # pack the listbox in the main window])
        self.my_list.pack( side = 'left', fill = 'both')
        # set the config of the scrollbar
        self.scroll.config(command= self.my_list.yview)


    def __done(self):
        """
        remove completed task from list and db
        """
        # get the string of the current selection using its
        # listbox index
        x =self.my_list.get(self.my_list.curselection())
        # dictionary of db contents
        db = self.t_list.dict_db_content()
        # deletes the current selected item from the listbox
        self.my_list.delete('anchor')
        # remove the item from db using its id in the db
        #print(db[(x[3:])])
        self.t_list.remove_item(db[(x[3:])])

    def start(self):
        """
        starts the app
        """
        self.root.mainloop()


#if __name__ == "__main__":
# start the app
TodoApp().start()