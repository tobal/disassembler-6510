
import unittest
import os
from src.disassembler.SidDisassembler import SidDisassembler
from src.disassembler.SidCommon import AddressModes

class SidDisassemblerTest(unittest.TestCase):

    HEADER_SIZE = 124
    OFFSET_SIZE = 2

    def setUp(self):
        self.testFileName = "testfile"
        self.createSidFile()
        self.sut = SidDisassembler(self.testFileName)    # system under test

    def tearDown(self):
        self.deleteSidFile()

    def createSidFile(self):
        self.testFile = file(self.testFileName, "wb")
        for byte in range(0, self.HEADER_SIZE):
            self.testFile.write("\x00")
        for byte in range(0, self.OFFSET_SIZE):
            self.testFile.write("\x88")
        self.testFile.write("\xad\x01\x02\x00")
        self.testFile.close()

    def deleteSidFile(self):
        os.remove(self.testFileName)

    def testAbsoluteAddressedLoadAccumulator(self):
        output = self.sut.disassembleInstruction(0xAD)
        self.assertEquals(output, ["LDA", AddressModes.ABSOLUTE])

    def testAbsoluteHasTwoByteAddress(self):
        numOfBytes = self.sut.getAddrModeNumOfBytes(AddressModes.ABSOLUTE)
        self.assertEquals(numOfBytes, 2)

    def testReadSidFile(self):
        self.assertEquals(len(self.sut.sidStruct.header), self.HEADER_SIZE)
        self.assertEquals(len(self.sut.sidStruct.offset), self.OFFSET_SIZE)
        self.assertEquals(len(self.sut.sidStruct.data), 4)
        for byte in self.sut.sidStruct.header:
            self.assertEquals(byte, 0x00)
        for byte in self.sut.sidStruct.offset:
            self.assertEquals(byte, 0x88)

    def testGetBytesFromFile(self):
        testFile = file(self.testFileName, "rb")
        byte = self.sut.getBytesFromFile(testFile, 1)
        twoBytes = self.sut.getBytesFromFile(testFile, 2)
        self.assertEquals(len(byte), 1)
        self.assertEquals(len(twoBytes), 2)
        testFile.close()

    def testGetAnInstructionWithAddress(self):
        instr = self.sut.getNextInstruction()
        self.assertEquals(instr.mnemonic, "LDA")
        self.assertEquals(instr.address, [0x02, 0x01])

    def testInstructionComments(self):
        comment = self.sut.getCommentForMnemonic("LDA")
        self.assertEquals(comment, "Loads data from address into accumulator")

    def testGetInstructionAsAssembly(self):
        instruction = self.sut.getNextInstruction()
        asmCode = self.sut.getInstructionAsAssembly(instruction)
        self.assertEquals(asmCode, "LDA 02 01   ; Loads data from address into accumulator, addr: Absolute")

    def testImpliedAddressing(self):
        self.sut.getNextInstruction()
        ins = self.sut.getNextInstruction()
        self.assertEquals(ins.address, [])

    def testReadWholeFileAndGetAsm(self):
        printOutput = self.sut.getSidFileAsAssembly()
        self.assertEquals(printOutput, "LDA 02 01   ; Loads data from address into accumulator, addr: Absolute\nBRK   ; Cause software interrupt, addr: Implied\n")

