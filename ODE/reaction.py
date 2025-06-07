sp = {"H2": 0, "H2O": 1, "O2": 2, "CO": 3, "CH4": 4, "CO2": 5, "CH2": 6}

R1 = {"ls1": "H2", "ls1_m": 1,
      "ls2": "O2", "ls2_m": 0.5, 
      "rs1": "H2O", "rs1_m": 1, 
      "rs2": None, "rs2_m": None, 
      "A": 9.1e8, 
      "E": 23000,
      "a": 0.54,
      "b": 0.5}

R2 = {"ls1": "CO", "ls1_m": 1,
      "ls2": "O2", "ls2_m": 0.5, 
      "rs1": "CO2", "rs1_m": 1, 
      "rs2": None, "rs2_m": None, 
      "A": 1.42e8, 
      "E": 42600,
      "a": 0.95,
      "b": 0.5}

R3 = {"ls1": "CO", "ls1_m": 1,
      "ls2": "H2O", "ls2_m": 1, 
      "rs1": "CO2", "rs1_m": 1, 
      "rs2": "H2", "rs2_m": 1, 
      "A": 2.26e13, 
      "E": 20000,
      "a": 1,
      "b": 1}

M1R = {"ls1": "CH4", "ls1_m": 1,
      "ls2": "O2", "ls2_m": 0.5, 
      "rs1": "CO", "rs1_m": 1, 
      "rs2": "H2", "rs2_m": 2, 
      "A": 1.84e6, 
      "E": 32500,
      "a": 0.2,
      "b": 0.5}

M2= {"ls1": "CH4", "ls1_m": 1,
      "ls2": "H2", "ls2_m": 1, 
      "rs1": "CH2", "rs1_m": 1, 
      "rs2": "H2", "rs2_m": 2, 
      "A": 3.0e14, 
      "E": 20000,
      "a": 1,
      "b": 1}

M3= {"ls1": "CH2", "ls1_m": 1,
      "ls2": "H2O", "ls2_m": 1, 
      "rs1": "CO", "rs1_m": 1, 
      "rs2": "H2", "rs2_m": 2, 
      "A": 2.0e11, 
      "E": 20000,
      "a": 1,
      "b": 1}

rections = [R1, R2, R3, M1R, M2, M3]
T   = 1500
R = 1.987
Eq  = dict()
J   = dict()

for s in sp:
    Eq[s] = f"dydx[{sp[s]}] = "

    for reac in rections:
        if reac["rs1"] == s:
            Eq[s] += f" + {reac["rs1_m"]} * {reac["A"]} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
        elif reac["rs2"] == s:
            Eq[s] += f" + {reac["rs2_m"]} * {reac["A"]} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
        
        if reac["ls1"] == s:
            Eq[s] += f" - {reac["ls1_m"]} * {reac["A"]} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
        elif reac["ls2"] == s:
            Eq[s] += f" - {reac["ls2_m"]} * {reac["A"]} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
    Eq[s] += ";"

file = open("react.txt", "w")

for s in Eq:
    file.write(Eq[s] + '\n')
    
for s1 in sp:
    for s2 in sp:
        J[(s1, s2)] = f"dfdy({sp[s1]}, {sp[s2]}) = 0"
     
        for reac in rections:
            if reac["rs1"] == s1:
                if reac["ls1"] == s2:
                    J[(s1, s2)] += f" + {reac["rs1_m"]} * {reac["A"]} * {reac['a']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']} - 1) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
                elif reac["ls2"] == s2:
                    J[(s1, s2)] += f" + {reac["rs1_m"]} * {reac["A"]} * {reac['b']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']} - 1) * Foam::exp(-{reac["E"] / (R * T)})"
            elif reac["rs2"] == s1:
                if reac["ls1"] == s2:
                    J[(s1, s2)] += f" + {reac["rs2_m"]} * {reac["A"]} * {reac['a']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']} - 1) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
                elif reac["ls2"] == s2:
                    J[(s1, s2)] += f" + {reac["rs2_m"]} * {reac["A"]} * {reac['b']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']} - 1) * Foam::exp(-{reac["E"] / (R * T)})"


            if reac["ls1"] == s1:
                if reac["ls1"] == s2:
                    J[(s1, s2)] += f" - {reac["ls1_m"]} * {reac["A"]} * {reac['a']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']} - 1) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
                elif reac["ls2"] == s2:
                    J[(s1, s2)] += f" - {reac["ls1_m"]} * {reac["A"]} * {reac['b']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']} - 1) * Foam::exp(-{reac["E"] / (R * T)})"
            elif reac["ls2"] == s1:
                if reac["ls1"] == s2:
                    J[(s1, s2)] += f" - {reac["ls2_m"]} * {reac["A"]} * {reac['a']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']} - 1) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']}) * Foam::exp(-{reac["E"] / (R * T)})"
                elif reac["ls2"] == s2:
                    J[(s1, s2)] += f" - {reac["ls2_m"]} * {reac["A"]} * {reac['b']} * Foam::pow(y[{sp[reac['ls1']]}], {reac['a']}) * Foam::pow(y[{sp[reac['ls2']]}], {reac['b']} - 1) * Foam::exp(-{reac["E"] / (R * T)})"
        J[(s1, s2)] += ';'


file.write("\n")

for s in J:
    file.write(J[s] + '\n')