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

