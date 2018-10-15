

 
opcode = {

            'CLA' : '0000',
            'LAC' : '0001',
            'SAC' : '0010',
            'ADD' : '0011',
            'SUB' : '0100',
            'BRZ' : '0101',
            'BRP' : '0111',
            'INP' : '1000',
            'DSP' : '1001',
            'MUL' : '1010',
            'DIV' : '1011',
            'STP' : '1100',

          }


file=open('input.txt','r')
lines=[]
for x in file:
    a=x.splitlines()[0]
    a=a.split(" ")
    z=[]
    for s in a:
        if(s!=""):
            z.append(s)
    lines.append(z)


for k in range(len(lines)):
    for i in range(len(lines[k])):                 
        if(lines[k][i] in opcode):                       #converting opcodes to opcode binary
            lines[k][i]=opcode[lines[k][i]]

get_bin = lambda x, n: format(x, 'b').zfill(n)
memorycounter=1
memory={}

for k in range(len(lines)):
    for i in range(len(lines[k])):
        if(lines[k][i] in memory):
            lines[k][i]=memory[lines[k][i]][0]


print(lines)


