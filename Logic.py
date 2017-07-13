


def NEG(value: bool):
    return not value;

def EEQ(v1: bool, v2: bool):
    return v1 == v2;

def NEQ(v1: bool, v2: bool):
    return v1 != v2;


def AND(v1: bool, v2: bool):
    return v1 & v2;

def OOR(v1: bool, v2: bool):
    return v1 | v2;

def NND(v1: bool, v2: bool):
    return not (v1 & v2);

def NOR(v1: bool, v2: bool):
    return not (v1 | v2);


def SSO(v1: bool, v2: bool):
    return v1 <= v2;

def IIF(v1: bool, v2: bool):
    return v1 >= v2;

def NSO(v1: bool, v2: bool):
    return v1 > v2;

def NIF(v1: bool, v2: bool):
    return v1 < v2;


brackets = {'(', ')'};

interpret = {}
interpret["T"] = True; interpret["F"] = False; constants = {"T", "F"};
interpret["neg"] = NEG; interpret["eeq"] = EEQ; interpret["neq"] = NEQ;
interpret["and"] = AND; interpret["oor"] = OOR; interpret["nnd"] = NND; interpret["nor"] = NOR;
interpret["sso"] = SSO; interpret["iif"] = IIF; interpret["nso"] = NSO; interpret["nif"] = NIF;

def invert(d: dict):
    """
    """
    D = dict();
    for item in d:
        key = d[item]; value = item; D[key] = item;
    return D;

inverse = invert(interpret);

relations = set(interpret) - constants;

inputs = {};
inputs["neg"] = 1;
for item in relations - {"neg"}:
    inputs[item] = 2;

brackets = {"(", ")"};

precedence = (
    {"neg"}, 
    {"and", "nnd"}, 
    {"oor", "nor"}, 
    {"sso", "iif", "nso", "nif"}, 
    {"eeq", "neq"}
);