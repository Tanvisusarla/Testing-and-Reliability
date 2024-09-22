f = open(r"C:\\Users\tanvi\OneDrive\Documents\UIC_Fall24\testing\testbench.txt","r")
lines = f.readlines()
in_node = []
out_node = []
gates_out = []
gates_in = []
wires =[]
level=[]
nodes=[]
for i, val in enumerate(lines):
    val = val.replace("\n", "")  # get rid of linebreak at the end
    #location = val.find('(')
    input_Node = val.find('INPUT')
    output_Node = val.find('OUTPUT')
    g_out = val.find('=')
    g_1 = val.find('(')
    g_2 = val.find(')')
    g = val.count(',')
    if input_Node >= 0:
        in_node.append(val[input_Node + 6:g_2])
    if g_out >= 0:
        gates_out.append(val[0:g_out - 1])
        gates_in.append(g + 1)
        wires.append(val[g_1+1:g_2])

print(f'\nInput nodes are {in_node}')
print('---------------------------------------------')
#print(f'wires :{wires}')
#print(f'input : {gates_in}')
#print(f'gates_out{gates_out}')


nodes=in_node.copy()+gates_out
#print(nodes)


level=["u" for _ in range(len(nodes))] #initialize level to "u"

#print(level)
j=0
for i in range(len(in_node)):
    for j in range(len(nodes)):
        if  in_node[i] == nodes[j] :
            level[j]="0"
n=[]
n=n+in_node
#print(f'level{level}')
s=0
w=wires.copy()
while "u" in level:
    q=[]
    r=[]
    #print(r)
    i=0
    #print(wires)
    #print(f'n{n}')
    for x in range(len(wires)):
        l=wires[x].replace(" ","")
        l=l.split(",")
        #print(l)
        p=0

        for y in range(len(n)):
            #print(f'n is {n[y]} p is{p}')
            for z in range(len(l)):
                if l[z]==n[y]:
                    #print(f'p: {p}')
                    p=p+1
                    #print(f'n :{n[y]} p:{p} l:{l[z]}')    
                else:
                    pass
                    #print(f'no  n :{n[y]} p:{p} l:{l[z]}')

        if p==len(l) and len(l)!=0:
            level[len(in_node)+x]=f"{s+1}"
            r.append(gates_out[x])
            q.append(x)
        else:
            pass
    n=n+r
    for i in range(len(q)):
        wires[q[i]]=""
    #print(f'wires{wires}')
    s=s+1

k=0
for k in range(len(level)):
    print(f"node {nodes[k]}  is  at  level{level[k]}")

#print(n)



