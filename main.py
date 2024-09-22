f = open(r"C:\\Users\tanvi\OneDrive\Documents\UIC_Fall24\testing\testbench.txt","r")
lines = f.readlines()
in_node = []
out_node = []
gates_out = []
gates_type = []
gates_in = []
wires =[]
print('Here are all the lines read from p2.txt')
print(lines)
print('\n')
for i, val in enumerate(lines):
    val = val.replace("\n", "")  # get rid of linebreak at the end
    #location = val.find('(')
    input_Node = val.find('INPUT')
    output_Node = val.find('OUTPUT')
    g_out = val.find('=')
    g_1 = val.find('(')
    g_2 = val.find(')')
    g = val.count(',')
    #print(f'line {i}: {val}')
    if input_Node >= 0:
        in_node.append(val[input_Node + 6:g_2])
        #print(f'found input node at {input_Node}')
    if output_Node >= 0:
        out_node.append(val[output_Node + 7:g_2])
            #print(f'found output node at {output_Node}')
    if g_out >= 0:
        gates_out.append(val[0:g_out - 1])
        gates_type.append(val[g_out + 1:g_1])
        gates_in.append(g + 1)
        wires.append(val[g_1+1:g_2])
    #print(f'input nodes are {in_node}')
    #print(f'output nodes are {out_node}')
    #print(f'gate output nodes are {gates_out}')
    #print(f'gates are {gates_type}')
    #print(f'gate input types are {gates_in}')
    #print(f'wires going into gate are {wires}')
    #input('Press enter to continue \n')

print(f'\nInput nodes are {in_node}')
print(f'Output nodes are {out_node}')
print('---------------------------------------------')
print('\nList of gate types and input wires:')
for i in range(len(gates_in)):
    print(f'\n{gates_in[i]} input {gates_type[i]} gate')
    print(f'wires going into gate are : {wires[i]}')
