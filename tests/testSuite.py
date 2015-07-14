
import unittest
import SidDisassemblerTest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(SidDisassemblerTest)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

