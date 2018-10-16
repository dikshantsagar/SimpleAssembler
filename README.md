# AssemblyLangTranslator
A python Program to translate Assembly code to Machine Code with given specific opcode definitions

eg Assembly code [performs (i+j)*(k+l)] :

*     LAC I     
*     ADD J
*     SAC INTER
*     LAC K
*     ADD L
*     MUL INTER
*     STP
*     I DS 4
*     J DS 5
*     K DS 5
*     L DS 4
*     INTER DS 0

# Output

translated code :
* ['0001', '0001']
* ['0011', '0010']
* ['0010', '0101']
* ['0001', '0011']
* ['0011', '0100']
* ['1010', '0101']
* ['1100']
* ['0001', 'DS', '0100']
* ['0010', 'DS', '0101']
* ['0011', 'DS', '0101']
* ['0100', 'DS', '0100']
* ['0101', 'DS', '0000']

Memory :
* I -> ['0001', 4]
* J -> ['0010', 5]
* K -> ['0011', 5]
* L -> ['0100', 4]
* INTER -> ['0101', 0]
