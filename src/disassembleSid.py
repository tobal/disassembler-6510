
import sys
import os
from src.disassembler.SidDisassembler import SidDisassembler

if len(sys.argv) == 1:
    print "Please provide a sid file as an argument"
    sys.exit(1)
else:
    sidFilename = sys.argv[1]
    if not os.path.exists(sidFilename):
        print "File does not exist"
        sys.exit(1)

disassembler = SidDisassembler()
disassembler.openSidFile(sidFilename)
print disassembler.getSidFileAsAssembly()

