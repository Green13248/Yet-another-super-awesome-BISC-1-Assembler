# How to use

Write a program ex: C:/Users/Green13248/Myproject/program.txt

Decide where you want the compiled file to go ex: C:/Users/Green13248/Myproject/compiledproject.txt

Done

# What

BISC is my own machine instruction set, it currently only exists in my mind.

Registers are a, b, c and d and are declared as !A

PSEUDO:

LABEL:
etc code

NORMAL:

Enable Add in the ALU                    ADD

Enable Subtract in the ALU				       SUB

Enable Multiply in the ALU			         MUL

Enable Divide in the ALU				         DIV

Jump to (Location)					             JMP, LABEL

Compare a=b						                   CMP

Compare a>b						                   CMG

Compare a>=b					                   CGE

Reg to Bus (Register)					           RTB, !A

Bus to Reg (Register)					           BTR, !C

Bus to ALU1						                   BTA

ALU1 to Bus                              ATB

Bus to ALU2                              BTM

ALU2 to Bus			                         MTB			

Bus to RAM (Address)				             BTR, $0x10

RAM to Bus (Address)				             RTB, $0x10

Bus to Stack						                 BTS

Stack to Bus                             STB

Bus to Serial		                         

Serial to Bus			

Bus to Serial 2				

Serial 2 to Bus					

Bus to Expansion				

Expansion to Bus					

Data to Bus (Data)					

NOP							

Serial input buffer on/off				

Serial 2 input buffer on/off				

Halt							

Clear ALU Accumulator 1 aka A			

Clear ALU Accumulator 2 aka B			

Jump if zero flag is true (Location)				

Jump if zero flag is false (Location)	

Set zero flag false

*Second last bit of instruction is for follow flag ex: 0”1”001101

