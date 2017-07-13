
black = "black"; red = "red";

from tkinter import *; from LogicCalculator import *;

errMessage = "afasdf";

def string(L, mid=' '):
    """ (list[str], str) -> str
    
    Returns an output string that contains the elements of L in order of index, separated by the mid
    string.
    """
    
    i=0; toReturn = L[0];
    while i < len(L):
        toReturn += ' ' + L[i]; i += 1;
    
    return toReturn;

class calculator:
    
    def add(self, text):
        """ (calculator, str) -> NoneType
        
        Adds text to all string and list variables that are to be used for computing.
        """
        
        # If there is an output, clear it.
        if self.Out != StringVar().set(""):
            self.Out.set("");
        
        # Once there is no output, update computation.
        self.toCompute.append(text); self.In.set(self.In + text); 
    
    def compute(self, L):
        """ (calculator, list) -> NoneType
        
        Computes the input and then outputs it.
        """
        
        # Consider using try-except for errors.
        self.Out.set(computeList(L)[0]);
    
    def clear(self):
        """ (calculator) -> NoneType
        
        Clears all input and output values.
        """
        
        self.In.set(''); self.Out.set('');
        # Make sure to update record.
        pass
    
    def delete(self):
        """ (calculator) -> NoneType
        
        Deletes the last added button into input.
        """
        
        s = self.toCompute[-1];
        del self.toCompute[-1]; self.In.set(self.In - s);
    
    def __init__(self, window):
        """
        Constructor method.
        
        Need reset and delete buttons. May also add prev/next buttons for inputs.
        """
        
        # This is to assist with other methods, when introducing StringVar.
        self.window = window;
        
        # Declaration of variables.
        self.toCompute = []; self.In = StringVar(window); self.Out = StringVar(window);
        
        self.In.set(""); self.Out.set("");
        self.In.set("Hello"); self.Out.set("Hi there!"); # Dummy text. 
        self.record = []; # Used for recording a series of input strings.
        
        # Window title
        window.title("Logic Calculator");
        
        # The mainframe.
        main = Frame(window); main.grid(row=0, column=0, padx=3, pady=3, sticky=N+S+W+E);
        
        # The set of 6 frames.
        ioFrame = Frame(main, relief=GROOVE, borderwidth=3, padx=1, pady=1); 
        ioFrame.grid(row=0, sticky=N+E+S+W, columnspan=2); ioFrame.columnconfigure(0, weight=1)
        nwFrame = Frame(main, padx=2, pady=2); nwFrame.grid(row=1,column=0); 
        neFrame = Frame(main, padx=2, pady=2); neFrame.grid(row=1,column=1); 
        swFrame = Frame(main, padx=2, pady=2); swFrame.grid(row=2,column=0); 
        seFrame = Frame(main, padx=2, pady=2); seFrame.grid(row=2,column=1); 
        ssFrame = Frame(main, padx=2, pady=2); ssFrame.grid(row=3, columnspan=2);
        
        # Top 2 rows: the IO portion
        iFrame = Label(ioFrame, textvariable=self.In, relief=SUNKEN, anchor=W)
        iFrame.grid(row=0, sticky=N+W+E); iFrame.grid_rowconfigure(0, weight=1);
        Label(ioFrame, textvariable=self.Out).grid(row=1, sticky=S+E,columnspan=2);
        
        # Top left 2x2 Frame: [ ( | ) ][ T | F ]
        Button(nwFrame, text='(', height=2, width=10).grid(row=0,column=0);
        Button(nwFrame, text=')', height=2, width=10).grid(row=0,column=1);
        Button(nwFrame, text='T', height=2, width=10).grid(row=1,column=0);
        Button(nwFrame, text='F', height=2, width=10).grid(row=1,column=1);
        
        # Top right 2x2 Frame: [ AND | OOR ][ NND | NOR ]
        Button(neFrame, text='and', height=2, width=10).grid(row=0,column=0);
        Button(neFrame, text='oor', height=2, width=10).grid(row=0,column=1);
        Button(neFrame, text='nnd', height=2, width=10).grid(row=1,column=0);
        Button(neFrame, text='nor', height=2, width=10).grid(row=1,column=1);
        
        # Bottom left 2x2 Frame: [ SSO | IIF ][ NSO | NIF ]
        Button(swFrame, text='sso', height=2, width=10).grid(row=0,column=0);
        Button(swFrame, text='iif', height=2, width=10).grid(row=0,column=1);
        Button(swFrame, text='nso', height=2, width=10).grid(row=1,column=0);
        Button(swFrame, text='nif', height=2, width=10).grid(row=1,column=1);
        
        # Bottom right 2x2 Frame: [ EEQ | NEG ][ NEQ | === ]
        Button(seFrame, text='eeq', height=2, width=10).grid(row=0,column=0);
        Button(seFrame, text='neg', height=2, width=10).grid(row=0,column=1);
        Button(seFrame, text='neq', height=2, width=10).grid(row=1,column=0);
        Button(seFrame, text='=', height=2, width=10).grid(row=1,column=1);
        
        # Bottom row: [ PRE | FOR | DEL | CLR ]
        Button(ssFrame, text='last', height=2, width=10).grid(row=0,column=0);
        Button(ssFrame, text='next', height=2, width=10).grid(row=0,column=1);
        Button(ssFrame, text='delete', height=2, width=10).grid(row=0,column=2);
        Button(ssFrame, text='clear', height=2, width=10).grid(row=0,column=3);
        
        # May need to add a row with [ < | > | DEL | INS ] and replace above DEL with CLR ALL.



if __name__ == "__main__": # Only runs program if this specfic file is opened.
    
    window = Tk(); # The window
    calculator(window);
    window.resizable(width=False, height=False)
    window.mainloop();