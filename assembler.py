
import sys
                                                    # Dikshant Sagar
opcode = {                                          
                                                    
            'CLA' : '0000',                         
            'LAC' : '0001',                         
            'SAC' : '0010',
            'ADD' : '0011',
            'SUB' : '0100',
            'BRZ' : '0101',
            'BRP' : '0111',                         # opcode dictionary
            'INP' : '1000',
            'DSP' : '1001',
            'MUL' : '1010',
            'DIV' : '1011',
            'STP' : '1100',

          }


file=open('input.txt','r')
lines=[]
for x in file:
    a=x.splitlines()[0]                     #reading code lines from the file
    a=a.split(" ")
    z=[]
    for s in a:
        if(s!="" and s[0]!='#'):  # condition to igone comments preceeding '#' character
            z.append(s)
    lines.append(z)
file.close()

for k in range(len(lines)): 
        try:                       
            lines[k][0]=opcode[lines[k][0]]      #converting opcodes to opcode binary
            if(lines[k][0]=='1100'):             #checking for STP opcode.
                break
        except:
            print("Error : Invalid Opcode in line:",k+1)
            sys.exit(0)

get_bin = lambda x, n: format(x, 'b').zfill(n)      #code to get binary format of a number in 4 bit format.
memorycounter=1                                     #memory counter for variable mem allocation.
memory={}


for k in range(len(lines)):
    for i in range(len(lines[k])):                 
        if(lines[k][i]=='DS'):
            memory[lines[k][i-1]]=[get_bin(memorycounter,8),int(lines[k][i+1])]   # detecting variable declaration and allocating virtual memory address
            memorycounter+=1
            lines[k][i+1]=get_bin(int(lines[k][i+1]),8)

for k in range(len(lines)):
    try:
        if(lines[k][0]=='1100'):               # checking for STP opcode
            break
        lines[k][1]=memory[lines[k][1]][0]       # replacing variables with allocated addresses.
    except:
        print('Error: variable',lines[k][1],'not defined in line',k+1)
        sys.exit(0)
        

print("translated code :")
for line in lines:                          #printing translated code
    print(line)

print("Memory Table :")
print("Variabe -> [Address , Value]")

for el in memory:
    print(el,"      ->",memory[el])

output=[]
for line in lines:
    if('DS' not in line):       #removing DS statements form thr translated code
        output.append(line)


for i in range(len(output)):
    output[i]=' '.join(output[i])   # forming lines of the code

file=open('output.txt','w')
for l in output:
    file.writelines(l)                  #writing final ouput code to a .txt file.
    file.write('\n')
file.close()
print("Open File named 'ouput.txt' in the same directory for the final assembled code :")


