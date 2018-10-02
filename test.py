 
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
print(lines)
