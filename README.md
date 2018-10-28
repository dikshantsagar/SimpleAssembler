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
* ['00000001', '00000001']
* ['00000011', '00000010']
* ['00000010', '00000101']
* ['00000001', '00000011']
* ['00000011', '00000100']
* ['00001010', '00000101']
* ['00001100']
* ['00000001', 'DS', '00000100']
* ['00000010', 'DS', '00000101']
* ['00000011', 'DS', '00000101']
* ['00000100', 'DS', '00000100']
* ['00000101', 'DS', '00000000']

Memory :
* I -> ['00000001', 4]
* J -> ['00000010', 5]
* K -> ['00000011', 5]
* L -> ['00000100', 4]
* INTER -> ['00000101', 0]

# Ouput File
* 00000001 00000001
* 00000011 00000010
* 00000010 00000101
* 00000001 00000011
* 00000011 00000100
* 00001010 00000101
* 00001100
