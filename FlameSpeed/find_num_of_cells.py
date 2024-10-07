

def find_n(filename):
    with open(filename, 'r') as file:
        while line := file.readline():
            if line == 'internalField   nonuniform List<scalar> \n':
                return int(file.readline()[:-1])

# print(find_n('/home/tgd323/PythonProject/IPMechRepos/H2O'))

