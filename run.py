
from tkinter import * 
from LogicCalculator import *

errMessage = "Error. "

MID = ' '

def string(L, mid=' '): # May not need this.
    """ (list[str], str) -> str
    
    Returns an output string that contains the elements of L in order of index, separated by the mid
    string.
    """
    
    i=0 
    toReturn = L[0]
    while i < len(L):
        toReturn += ' ' + L[i] 
        i += 1
    
    return toReturn

class calculator:
    
    def incIndex(self):
        """ (calculator) -> NoneType
        
        Increments the index of input, if possible.
        This is going one step previously into memory.
        """
        
        if self.index < len(self.record)-1:
            self.index += 1;
        
        # Update input and output
        self.In.set(self.record[self.index])
        self.Out.set('')
        
        # Update self.toCompute
        self.toCompute = self.record[self.index].split();
    
    def decIndex(self):
        """ (calculator) -> NoneType
        
        Decrements the index of input, if possible.
        This is going one step closer to main record.
        """
        
        if self.index >= 1:
            self.index -= 1;
        
        # Update input and output
        self.In.set(self.record[self.index])
        self.Out.set('')
        
        # Update self.toCompute
        self.toCompute = self.record[self.index].split()
    
    def updateRecord(self, text):
        """ (calculator, str) -> NoneType
        
        Updates the memory record when a symbol is added on the input string. 
        """
        
        self.record[0] = self.In.get()
    
    def newRecord(self):
        """ (calculator) -> NoneType
        
        Starts a new record item.
        """
        
        # Make sure there's at most 36 items in record. Delete a 36th one if there is one.
        if len(self.record) == 36:
            del self.record[35] # There are at most 35 objects in record.
        
        # Starts a new record.
        self.record[:] = [''] + self.record[:]
    
    def add(self, text):
        """ (calculator, str) -> NoneType
        
        Adds text to all string and list variables that are to be used for computing.
        """
        
        # If there is an output, clear first.
        if self.Out.get() != '':
            self.clear()
        
        if self.In.get() == '':
            self.record = [] + self.record
        
        # Once there is no output, update computation.
        self.toCompute.append(text) 
        self.In.set(self.In.get() + ' ' + text)
        self.updateRecord(text)
    
    def compute(self):
        """ (calculator) -> NoneType
        
        Computes the input and then outputs it.
        """
        
        # If not on most recent memory, delete future indices.
        if self.index != 0:
            del self.record[:self.index]
        
        # Consider using try-except for errors.
        try:
            self.Out.set(computeList(self.toCompute)[0])
        except:
            self.Out.set(errMessage)
    
    def clear(self):
        """ (calculator) -> NoneType
        
        Clears all input and output values.
        """
        
        self.In.set('') 
        self.Out.set('')
        
        # Make sure to update record and reset self.toCompute.
        self.toCompute = []
        self.newRecord()
    
    def delete(self):
        """ (calculator) -> NoneType
        
        Deletes the last added button into input.
        """
        
        # Clear output
        self.set('')
        
        # Updates self.toCompute
        s = self.toCompute[-1]
        del self.toCompute[-1]
        
        # Updates input
        r = len(s) + 1 # total index to be subtracted. The additional 1 is due to the space.
        self.In.set(self.In.get()[:-r])
    
    def __init__(self, window):
        """
        Constructor method.
        
        Need reset and delete buttons. May also add prev/next buttons for inputs.
        """
        
        # This is to assist with other methods, when introducing StringVar.
        self.window = window
        
        # Declaration of variables.
        self.toCompute = [] 
        self.In = StringVar(window) 
        self.Out = StringVar(window)
        
        self.In.set("") 
        self.Out.set("")
        self.record = [''] # Used for recording a series of input strings.
        self.index = 0 # For keeping record of input memory index. 0 = most recent.
        
        # Window title
        window.title("Logic Calculator")
        
        # The mainframe.
        main = Frame(window) 
        main.grid(row=0, column=0, padx=3, pady=3, sticky=N+S+W+E)
        
        # The set of frames.
        ioFrame = Frame(main, relief=GROOVE, borderwidth=3, padx=1, pady=1) 
        ioFrame.grid(row=0, sticky=N+E+S+W, columnspan=2) 
        ioFrame.columnconfigure(0, weight=1)
        
        nwFrame = Frame(main, padx=2, pady=2) 
        nwFrame.grid(row=1,column=0) 
        
        neFrame = Frame(main, padx=2, pady=2) 
        neFrame.grid(row=1,column=1) 
        
        swFrame = Frame(main, padx=2, pady=2) 
        swFrame.grid(row=2,column=0) 
        
        seFrame = Frame(main, padx=2, pady=2) 
        seFrame.grid(row=2,column=1) 
        
        SwFrame = Frame(main, padx=2, pady=2) 
        SwFrame.grid(row=3, column=0)
        
        SeFrame = Frame(main, padx=2, pady=3)
        SeFrame.grid(row=3, column=1)
        
        # Top 2 rows: the IO portion
        iFrame = Label(ioFrame, textvariable=self.In, relief=SUNKEN, anchor=W)
        iFrame.grid(row=0, sticky=N+W+E) 
        iFrame.grid_rowconfigure(0, weight=1)
        Label(ioFrame, textvariable=self.Out).grid(row=1, sticky=S+E,columnspan=2)
        
        # Top left 2x2 Frame: [ ( | ) ][ T | F ]
        Button(nwFrame, text=' ( ', height=2, width=10, command=lambda: self.add('(')).grid(row=0,column=0)
        Button(nwFrame, text=' ) ', height=2, width=10, command=lambda: self.add(')')).grid(row=0,column=1)
        Button(nwFrame, text=' T ', height=2, width=10, command=lambda: self.add('T')).grid(row=1,column=0)
        Button(nwFrame, text=' F ', height=2, width=10, command=lambda: self.add('F')).grid(row=1,column=1)
        
        # Top right 2x2 Frame: [ AND | OOR ][ NND | NOR ]
        Button(neFrame, text='and', height=2, width=10, command=lambda: self.add('and')).grid(row=0,column=0)
        Button(neFrame, text='oor', height=2, width=10, command=lambda: self.add('oor')).grid(row=0,column=1)
        Button(neFrame, text='nnd', height=2, width=10, command=lambda: self.add('nnd')).grid(row=1,column=0)
        Button(neFrame, text='nor', height=2, width=10, command=lambda: self.add('nor')).grid(row=1,column=1)
        
        # Bottom left 2x2 Frame: [ SSO | IIF ][ NSO | NIF ]
        Button(swFrame, text='sso', height=2, width=10, command=lambda: self.add('sso')).grid(row=0,column=0)
        Button(swFrame, text='iif', height=2, width=10, command=lambda: self.add('iif')).grid(row=0,column=1)
        Button(swFrame, text='nso', height=2, width=10, command=lambda: self.add('nso')).grid(row=1,column=0)
        Button(swFrame, text='nif', height=2, width=10, command=lambda: self.add('nif')).grid(row=1,column=1)
        
        # Bottom right 2x2 Frame: [ EEQ | NEG ][ NEQ | === ]
        Button(seFrame, text='eeq', height=2, width=10, command=lambda: self.add('eeq')).grid(row=0,column=0)
        Button(seFrame, text='neg', height=2, width=10, command=lambda: self.add('neg')).grid(row=0,column=1)
        Button(seFrame, text='neq', height=2, width=10, command=lambda: self.add('neq')).grid(row=1,column=0)
        Button(seFrame, text=' = ', height=2, width=10, command=lambda: self.compute() ).grid(row=1,column=1)
        
        # Bottom row: [ PRE | FOR || DEL | CLR ]
        Button(SwFrame, text='last',   height=2, width=10, command=lambda: self.incIndex()).grid(row=0,column=0)
        Button(SwFrame, text='next',   height=2, width=10, command=lambda: self.decIndex()).grid(row=0,column=1)
        Button(SeFrame, text='delete', height=2, width=10, command=lambda: self.delete()  ).grid(row=0,column=2)
        Button(SeFrame, text='clear',  height=2, width=10, command=lambda: self.clear()   ).grid(row=0,column=3)
        
        # May need to add a row with [ < | > | DEL | INS ] and replace above DEL with CLR ALL.



if __name__ == "__main__": # Only runs program if this specfic file is opened.
    
    window = Tk() # The window
    C = calculator(window)
    window.resizable(width=False, height=False)
    window.mainloop()
