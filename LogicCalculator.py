
from Logic import *;

## HELPER FUNCTIONS ________________________________________________________________________________
    
def checkBrackets(Code):
    """ Raises an exception if the number of left brackets != number of right brackets. """
    
    left = 0; right = 0;
    for item in Code:
        if "(" in item: left+= item.count("(");
        if ")" in item: right += item.count(")");
    if left != right: raise Exception("incorrect number of brackets.");

def orderOfComputation(Code, setPrec):
    """ (list[str], set[str]) -> tuple[int]
    
    Returns the order of computation to be applied to the code.
    """
    
    T = tuple(); resulT = tuple();
    for i in range(len(Code)):
        item = Code[i];
        if item in setPrec:
            T += (i,);
    return T;

def containsBrackets(Code):
    """ (list[str]) -> bool
    
    Returns True iff code contains brackets.
    """
    
    for item in Code:
        if '(' in item or ')' in item:
            return True;
    return False;

def total_sub(sub, index):
    """ (dict[int:int], int) -> int
    
    Determines the total amount to be taken away from index sub as a consequence of indices reduced
    during computation.
    """
    
    s = 0;
    for i in range(index):
        if i in sub:
            s += sub[i];
    return s;

def endBrackets(Code):
    """ (list[str]) -> (int, int)
    
    Returns indices of rightmost left end brackets and leftmost right end bracket.
    
    >>> endBrackets(['(', 'T', ')'])
    (0, -1)
    >>> endBrackets(['(', 'T', 'and', 'F', ')', 'oor', 'F'])
    (0, -3)
    >>> endBrackets(['(', '(', 'T', 'iif', 'F', ')', 'eeq', 'F', ')'])
    (1, -1)
    """
    
    left = 0; right = len(Code)-1;
    while right >= left:
        if Code[left] in brackets: left += 1;
        if Code[right] in brackets: right -= 1;
        if not (Code[left] in brackets or Code[right] in brackets): break;
    
    return (left-1, right+1);

def hasMidBrackets(Code):
    """ (list[str]) -> bool
    
    Returns True iff code contains any brackets in the middle.
    """
    
    l = len(Code);
    
    # Skip past the end brackets.
    left, right = endBrackets(Code)[0], endBrackets(Code)[1];
    left += 1; right -= 1;
    
    # Then keep going until either references a bracket or right < left.
    while right >= left: 
        if Code[left] in brackets: return True;
        if Code[right] in brackets: return True;
        left += 1; right -= 1;
    
    # Return False if right < left.
    return False;


## MAIN FUNCTIONS __________________________________________________________________________________

def computeList(Code):
    """ (list[str]) -> str
    
    Computes code provided by given list of string, which is a splitted string.
    
    >>> s1 = "T"
    >>> computeList(s1.split())
    'T'
    >>> s2 = "((F))"
    >>> computeList(s2.split())
    'F'
    >>> s3 = "T and F"
    >>> computeList(s3.split())
    'F'
    >>> s4 = "neg T oor F"
    >>> computeList(s4.split())
    'F'
    >>> s5 = "neg F iif T neq T"
    >>> computeList(s5.split())
    'F'
    >>> s6 = "neg (neg T) sso (T nnd F)"
    >>> computeList(s6.split())
    'T'
    """
    
    l = len(Code);
    # Make sure number of left brackets still == no of right brackets
    checkBrackets(Code);
    
    
    # Base case: Code = ['T'] or ['F'] or has brackets.
    if l == 1:
        
        C = Code[0].strip('( )');
        
        if C in constants: return C;
        
        else: return Exception("output is neither true nor false.");
    
    
    # Secondary case: No brackets remaining.
    elif not containsBrackets(Code):
        
        sub = {}; # records reduced indices in list, as a result of computation
        
        order = tuple();
        for prec in precedence:
            order += orderOfComputation(Code, prec); # Order of looking at the computation
        
        for i in order:
            
            s = total_sub(sub, i); # Computes the total to be subtracted from index.
            j = i-s; item = Code[j];
            
            # Negation case.
            if inputs[item] == 1:
                f = interpret[item]; inp = interpret[Code[j+1]];
                result = f(inp); string = inverse[result];
                Code = Code[:j] + [string] + Code[j+2:];
                
                # Update sub
                if not i in sub:
                    sub[i] = 1;
                
                else:
                    sub[i] += 1;
            
            # Binary Relation case.
            elif inputs[item] == 2:
                f = interpret[item]; 
                inp = (interpret[Code[j-1]], interpret[Code[j+1]]);
                result = f(*inp); string = inverse[result];
                Code = Code[:j-1] + [string] + Code[j+2:];
                
                # Update sub
                if not i in sub:
                    sub[i] = 2;
                
                else:
                    sub[i] += 2;
            
            else:
                raise Exception('incomplete inputs set.')
    
    
    # Tertiary case: brackets left inside to compute.
    else: # Here, deal with brackets to make sure no brackets are contained in between.
        
        # Remove the same total number of brackets from each end.
        if not hasMidBrackets(Code):
            endB = endBrackets(Code); first = endB[0]; last = endB[1];
            Code = Code[first+1: last]; 
            
            return computeList(Code);
 
        # Keep going until right bracket
        j = 0;
        while not ")" in Code[j]: j += 1;
        
        # Go back for left bracket.
        i = j-1;
        while not "(" in Code[i] or i < 0: i -= 1;
        
        if i < 0: raise Exception("improper use of brackets.");
        
        Code = Code[:i] + [ computeList(Code[i+1:j]) ] + Code[j+1:];
    
    return computeList(Code);


def compute(s):
    computeList(s.strip());