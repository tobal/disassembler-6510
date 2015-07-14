
class AddressModes():
    ABSOLUTE = "Absolute"
    ZERO_PAGE = "Zero page"
    ZERO_PAGE_X = "Zero page with X"
    ZERO_PAGE_Y = "Zero page with Y"
    ACCUMULATOR = "Accumulator"
    IMMEDIATE = "Immediate"
    INDIRECT = "Indirect"
    INDIRECT_X = "Indirect with X"
    INDIRECT_Y = "Indirect with Y"
    INDEXED_X = "Indexed with X"
    INDEXED_Y = "Indexed with Y"
    RELATIVE = "Relative"
    IMPLIED = "Implied"

class Instruction():
    mnemonic = ""
    address = []
    comment = ""
    addressing = ""

class SidStruct():
    header = []
    offset = []
    data = []

