#!C:\Users\Adeboye Emmanuel\AppData\Local\Programs\Python\Python36-32\python.exe
from todo import Todo
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
        self.root.title('To-do List')
        self.root.config(pady=2, padx=2, )
        
        # frame to hold the canvas
        self.canvas_frame = tk.Frame(self.root, width = 540, height = 250)
        # canvas to hold the page elements. i use canvas so as to 
        # make use of the scroll functionality of the canvas 
        self.app_canvas = tk.Canvas(self.canvas_frame, 
            width = 540, height = 250, scrollregion=
                (0,0,540,800))
        
        # scrollbar
        self.scroll = tk.Scrollbar(self.canvas_frame, orient = 'vertical')
        self.scroll.config(command= self.app_canvas.yview)
        # add the scrollbar to the main window
        self.scroll.pack(side='right', fill='y')
        # app_canvas config
        self.app_canvas.config(yscrollcommand=self.scroll.set)
        
        # set the window dimension
        self.root.geometry('{}x{}'.format(540, 250))
        # make the main window unresizeable
        self.root.resizable(width=False, height=False)
        # scrolled window


        # variable to hold the value of the radio buttons
        self.sel_rad = tk.StringVar()
        # container for the upper section of the app
        self.input_container = tk.Frame(self.root,)

        # create a label
        self.label = tk.Label(self.input_container, text = 'Enter Task here', font=("courier", 10))
        # arrange in a grid
        self.label.grid(row=0, column=0)

        # create text box
        self.user_input = tk.Entry(self.input_container, width=45)
        # arrange textbox in a grid
        self.user_input.grid(row=0, column=1)

        # ---------------------------------------------------
        # create the Add button
        tk.Button(self.input_container, text = 'Add', font=("courier", 10),
            command = self.get_input_value).grid(row=0, column=2)

        # button to remove completed task
        self.mark_done = tk.Button(self.input_container, text="Completed", 
            font=("courier", 10), command=self.done)
        # add to input_container grid
        self.mark_done.grid(row=0, column=3)

        # add input_container to the main window
        self.input_container.pack()

        # Task list header
        tl_header = tk.Label(self.root, text='List of activities', 
            font=("courier", 20))
        tl_header.pack()

        # add canvas frame to the main window
        self.canvas_frame.pack(anchor='w', fill='x')
        # update the list
        self.update_list()

        
    
    
    #get item from the db
    # get input and insert into the db
    def get_input_value(self):
        foo = tk.Entry.get(self.user_input)
        self.t_list.insert_item(foo)
        # destroy previous frame
        t_frame.destroy()
        # create an updated new frame
        self.update_list()
        self.label.setvar('')
        print(foo)

    def update_list(self):
        # frame to hold the list of tasks
        global t_frame
        t_frame = tk.Frame(self.app_canvas, ) #yscrollcommand= scroll.set)

        for item in self.t_list.view_all():
            tk.Radiobutton(t_frame, text = item[1], font=("courier", 10),
            value = item[0], variable = self.sel_rad).pack(anchor='w' )
        # pack the frame to the app_canvas
        t_frame.pack(anchor='w', fill='x')
        # pack the canvas in the main window
        self.app_canvas.pack(anchor='w')

    # remove completed task from list and db
    def done(self):
        print(self.sel_rad.get())
        self.t_list.remove_item(self.sel_rad.get())
        # destroy previous frame
        t_frame.destroy()
        # create an updated new frame
        self.update_list()


if __name__ == "__main__":
    t_app = TodoApp()
    # update the list
    #t_app.update_list()
    t_app.root.mainloop()