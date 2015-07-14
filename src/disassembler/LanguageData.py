
from src.disassembler.SidCommon import AddressModes

NumOfBytes = {
                AddressModes.ABSOLUTE : 2,
                AddressModes.ZERO_PAGE : 1,
                AddressModes.ZERO_PAGE_X : 1,
                AddressModes.ZERO_PAGE_Y : 1,
                AddressModes.ACCUMULATOR : 0,
                AddressModes.IMMEDIATE : 1,
                AddressModes.INDIRECT : 2,
                AddressModes.INDIRECT_X : 1,
                AddressModes.INDIRECT_Y : 1,
                AddressModes.INDEXED_X : 2,
                AddressModes.INDEXED_Y : 2,
                AddressModes.RELATIVE : 1,
                AddressModes.IMPLIED : 0
                        }

InstructionTypes = {
                0x6D : ["ADC", AddressModes.ABSOLUTE],
                0x69 : ["ADC", AddressModes.IMMEDIATE],
                0x61 : ["ADC", AddressModes.INDIRECT_X],
                0x71 : ["ADC", AddressModes.INDIRECT_Y],
                0x7D : ["ADC", AddressModes.INDEXED_X],
                0x79 : ["ADC", AddressModes.INDEXED_Y],
                0x65 : ["ADC", AddressModes.ZERO_PAGE],
                0x75 : ["ADC", AddressModes.ZERO_PAGE_X],
                0x2D : ["AND", AddressModes.ABSOLUTE],
                0x29 : ["AND", AddressModes.IMMEDIATE],
                0x21 : ["AND", AddressModes.INDIRECT_X],
                0x31 : ["AND", AddressModes.INDIRECT_Y],
                0x3D : ["AND", AddressModes.INDEXED_X],
                0x39 : ["AND", AddressModes.INDEXED_Y],
                0x25 : ["AND", AddressModes.ZERO_PAGE],
                0x35 : ["AND", AddressModes.ZERO_PAGE_X],
                0x03 : ["ASL", AddressModes.ABSOLUTE],
                0x0A : ["ASL", AddressModes.ACCUMULATOR],
                0x1E : ["ASL", AddressModes.INDEXED_X],
                0x06 : ["ASL", AddressModes.ZERO_PAGE],
                0x16 : ["ASL", AddressModes.ZERO_PAGE_X],
                0x90 : ["BCC", AddressModes.RELATIVE],
                0xB0 : ["BCS", AddressModes.RELATIVE],
                0xF0 : ["BEQ", AddressModes.RELATIVE],
                0x2C : ["BIT", AddressModes.ABSOLUTE],
                0x24 : ["BIT", AddressModes.ZERO_PAGE],
                0x30 : ["BMI", AddressModes.RELATIVE],
                0xD0 : ["BNE", AddressModes.RELATIVE],
                0x10 : ["BPL", AddressModes.RELATIVE],
                0x00 : ["BRK", AddressModes.IMPLIED],
                0x50 : ["BVC", AddressModes.RELATIVE],
                0x70 : ["BVS", AddressModes.RELATIVE],
                0x18 : ["CLC", AddressModes.IMPLIED],
                0xD8 : ["CLD", AddressModes.IMPLIED],
                0x58 : ["CLI", AddressModes.IMPLIED],
                0xB8 : ["CLV", AddressModes.IMPLIED],
                0xCD : ["CMP", AddressModes.ABSOLUTE],
                0xC9 : ["CMP", AddressModes.IMMEDIATE],
                0xC1 : ["CMP", AddressModes.INDIRECT_X],
                0xD1 : ["CMP", AddressModes.INDIRECT_Y],
                0xDD : ["CMP", AddressModes.INDEXED_X],
                0xD9 : ["CMP", AddressModes.INDEXED_Y],
                0xC5 : ["CMP", AddressModes.ZERO_PAGE],
                0xD5 : ["CMP", AddressModes.ZERO_PAGE_X],
                0xEC : ["CPX", AddressModes.ABSOLUTE],
                0xE0 : ["CPX", AddressModes.IMMEDIATE],
                0xE4 : ["CPX", AddressModes.ZERO_PAGE],
                0xCC : ["CPY", AddressModes.ABSOLUTE],
                0xC0 : ["CPY", AddressModes.IMMEDIATE],
                0xC4 : ["CPY", AddressModes.ZERO_PAGE],
                0xCE : ["DEC", AddressModes.ABSOLUTE],
                0xDE : ["DEC", AddressModes.INDEXED_X],
                0xC6 : ["DEC", AddressModes.ZERO_PAGE],
                0xD6 : ["DEC", AddressModes.ZERO_PAGE_X],
                0xCA : ["DEX", AddressModes.IMPLIED],
                0x88 : ["DEY", AddressModes.IMPLIED],
                0x4D : ["EOR", AddressModes.ABSOLUTE],
                0x49 : ["EOR", AddressModes.IMMEDIATE],
                0x41 : ["EOR", AddressModes.INDIRECT_X],
                0x51 : ["EOR", AddressModes.INDIRECT_Y],
                0x5D : ["EOR", AddressModes.INDEXED_X],
                0x59 : ["EOR", AddressModes.INDEXED_Y],
                0x45 : ["EOR", AddressModes.ZERO_PAGE],
                0x55 : ["EOR", AddressModes.ZERO_PAGE_X],
                0xEE : ["INC", AddressModes.ABSOLUTE],
                0xFE : ["INC", AddressModes.INDEXED_X],
                0xE6 : ["INC", AddressModes.ZERO_PAGE],
                0xF6 : ["INC", AddressModes.ZERO_PAGE_X],
                0xE8 : ["INX", AddressModes.IMPLIED],
                0xC8 : ["INY", AddressModes.IMPLIED],
                0x4C : ["JMP", AddressModes.ABSOLUTE],
                0x6C : ["JMP", AddressModes.INDIRECT],
                0x20 : ["JSR", AddressModes.ABSOLUTE],
                0xAD : ["LDA", AddressModes.ABSOLUTE],
                0xA9 : ["LDA", AddressModes.IMMEDIATE],
                0xA1 : ["LDA", AddressModes.INDIRECT_X],
                0xB1 : ["LDA", AddressModes.INDIRECT_Y],
                0xBD : ["LDA", AddressModes.INDEXED_X],
                0xB9 : ["LDA", AddressModes.INDEXED_Y],
                0xA5 : ["LDA", AddressModes.ZERO_PAGE],
                0xB5 : ["LDA", AddressModes.ZERO_PAGE_X],
                0xAE : ["LDX", AddressModes.ABSOLUTE],
                0xA2 : ["LDX", AddressModes.IMMEDIATE],
                0xBE : ["LDX", AddressModes.INDEXED_Y],
                0xA6 : ["LDX", AddressModes.ZERO_PAGE],
                0xB6 : ["LDX", AddressModes.ZERO_PAGE_Y],
                0xAC : ["LDY", AddressModes.ABSOLUTE],
                0xA0 : ["LDY", AddressModes.IMMEDIATE],
                0xBC : ["LDY", AddressModes.INDEXED_X],
                0xA4 : ["LDY", AddressModes.ZERO_PAGE],
                0xB4 : ["LDY", AddressModes.ZERO_PAGE_X],
                0x4E : ["LSR", AddressModes.ABSOLUTE],
                0x4A : ["LSR", AddressModes.ACCUMULATOR],
                0x5E : ["LSR", AddressModes.INDEXED_X],
                0x46 : ["LSR", AddressModes.ZERO_PAGE],
                0x56 : ["LSR", AddressModes.ZERO_PAGE_X],
                0xEA : ["NOP", AddressModes.IMPLIED],
                0x0D : ["ORA", AddressModes.ABSOLUTE],
                0x09 : ["ORA", AddressModes.IMMEDIATE],
                0x01 : ["ORA", AddressModes.INDIRECT_X],
                0x11 : ["ORA", AddressModes.INDIRECT_Y],
                0x1D : ["ORA", AddressModes.INDEXED_X],
                0x19 : ["ORA", AddressModes.INDEXED_Y],
                0x05 : ["ORA", AddressModes.ZERO_PAGE],
                0x15 : ["ORA", AddressModes.ZERO_PAGE_X],
                0x48 : ["PHA", AddressModes.IMPLIED],
                0x08 : ["PHP", AddressModes.IMPLIED],
                0x68 : ["PLA", AddressModes.IMPLIED],
                0x28 : ["PLP", AddressModes.IMPLIED],
                0x2E : ["ROL", AddressModes.ABSOLUTE],
                0x2A : ["ROL", AddressModes.ACCUMULATOR],
                0x3E : ["ROL", AddressModes.INDEXED_X],
                0x26 : ["ROL", AddressModes.ZERO_PAGE],
                0x36 : ["ROL", AddressModes.ZERO_PAGE_X],
                0x6E : ["ROR", AddressModes.ABSOLUTE],
                0x6A : ["ROR", AddressModes.ACCUMULATOR],
                0x7E : ["ROR", AddressModes.INDEXED_X],
                0x66 : ["ROR", AddressModes.ZERO_PAGE],
                0x76 : ["ROR", AddressModes.ZERO_PAGE_X],
                0x40 : ["RTI", AddressModes.IMPLIED],
                0x60 : ["RTS", AddressModes.IMPLIED],
                0xED : ["SBC", AddressModes.ABSOLUTE],
                0xE9 : ["SBC", AddressModes.IMMEDIATE],
                0xE1 : ["SBC", AddressModes.INDIRECT_X],
                0xF1 : ["SBC", AddressModes.INDIRECT_Y],
                0xFD : ["SBC", AddressModes.INDEXED_X],
                0xF9 : ["SBC", AddressModes.INDEXED_Y],
                0xE5 : ["SBC", AddressModes.ZERO_PAGE],
                0xF5 : ["SBC", AddressModes.ZERO_PAGE_X],
                0x38 : ["SEC", AddressModes.IMPLIED],
                0xF8 : ["SED", AddressModes.IMPLIED],
                0x76 : ["SEI", AddressModes.IMPLIED],
                0x8D : ["STA", AddressModes.ABSOLUTE],
                0x81 : ["STA", AddressModes.INDIRECT_X],
                0x91 : ["STA", AddressModes.INDIRECT_Y],
                0x9D : ["STA", AddressModes.INDEXED_X],
                0x99 : ["STA", AddressModes.INDEXED_Y],
                0x85 : ["STA", AddressModes.ZERO_PAGE],
                0x95 : ["STA", AddressModes.ZERO_PAGE_X],
                0x8E : ["STX", AddressModes.ABSOLUTE],
                0x86 : ["STX", AddressModes.ZERO_PAGE],
                0x96 : ["STX", AddressModes.ZERO_PAGE_Y],
                0x8C : ["STY", AddressModes.ABSOLUTE],
                0x84 : ["STY", AddressModes.ZERO_PAGE],
                0x94 : ["STY", AddressModes.ZERO_PAGE_X],
                0xAA : ["TAX", AddressModes.IMPLIED],
                0xA8 : ["TAY", AddressModes.IMPLIED],
                0xBA : ["TSX", AddressModes.IMPLIED],
                0x8A : ["TXA", AddressModes.IMPLIED],
                0x9A : ["TXS", AddressModes.IMPLIED],
                0x98 : ["TYA", AddressModes.IMPLIED],
                        }

Comments = {
                "LDA" : "Loads data from address into accumulator",
                "LDX" : "Loads data from address into X register",
                "LDY" : "Loads data from address into Y register",
                "STA" : "Stores data from accumulator to address",
                "STX" : "Stores data from X register to address",
                "STY" : "Stores data from Y register to address",
                "INC" : "Increments the addressed data by one",
                "DEC" : "Decrements the addressed data by one",
                "TAX" : "Loads data from accumulator to X register",
                "TAY" : "Loads data from accumulator to Y register",
                "TXA" : "Loads data from X register to accumulator",
                "TYA" : "Loads data from Y register to accumulator",
                "TXS" : "Loads data from X register to stack pointer",
                "TSX" : "Loads data from stack pointer to X register",
                "SEC" : "Sets the carry bit to high",
                "SED" : "Sets decimal-mode bit to high",
                "CLC" : "Clears the carry bit",
                "CLD" : "Clears the decimal-mode bit",
                "CLV" : "Clears the overflow bit",
                "CLI" : "Clears the interrupt bit (enables maskable interrupts)",
                "SEI" : "Sets the interrupt bit to high (disables maskable interrupts)",
                "DEX" : "Decrements the value of X register by one",
                "DEY" : "Decrements the value of Y register by one",
                "INX" : "Increments the value of X register by one",
                "INY" : "Increments the value of Y register by one",
                "JMP" : "Sets the instruction pointer to given address",
                "JSR" : "Calls a subroutine",
                "RTS" : "Returns from a subroutine",
                "RTI" : "Returns from an interrupt-handler",
                "BRK" : "Cause software interrupt",
                "BCC" : "The operand is added to the value of the instruction pointer (loops), if carry-bit is cleared",
                "BCS" : "The operand is added to the value of the instruction pointer (loops), if carry-bit is set",
                "BNE" : "The operand is added to the value of the instruction pointer (loops), if null-bit is cleared",
                "BEQ" : "The operand is added to the value of the instruction pointer (loops), if null-bit is set",
                "BPL" : "The operand is added to the value of the instruction pointer (loops), if negative-bit is cleared",
                "BMI" : "The operand is added to the value of the instruction pointer (loops), if negative-bit is set",
                "BVC" : "The operand is added to the value of the instruction pointer (loops), if overflow-bit is cleared",
                "BVS" : "The operand is added to the value of the instruction pointer (loops), if overflow-bit is set",
                "PHA" : "Push to stack from accumulator",
                "PLA" : "Pop from stack to accumulator",
                "PHP" : "Push stateregister to stack",
                "PLP" : "Pop stateregister from stack",
                "ASL" : "Bitwise step to left (lowest bit will be zero)",
                "ROL" : "Bitwise step to left (lowest bit comes from carry bit)",
                "ASR" : "Bitwise step to right (highest bit will be zero)",
                "ROR" : "Bitwise step to right (highest bit comes from carry bit)",
                "AND" : "Bitwise AND between accumulator and addressed byte",
                "ORA" : "Bitwise OR between accumulator and addressed byte",
                "EOR" : "Bitwise XOR between accumulator and addressed byte",
                "BIT" : "Bitwise AND between accumulator and addressed byte (result not loaded into accumulator)",
                "ADC" : "Add instruction (accumulator = accumulator + specific_byte + carry_bit)",
                "SBC" : "Subtract instruction",
                "CMP" : "Compares accumulator with specific byte (acc - byte)",
                "CPX" : "Compares X register with specific byte (X - byte)",
                "CPY" : "Compares Y register with specific byte (Y - byte)",
                "NOP" : "No operation",
                "LSR" : "UNKNOWN"
                        }
