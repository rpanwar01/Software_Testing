import unittest
import test_calc
import test_copycalc

class Test_000_Calc(test_calc.Test_000_Calculator):
   pass

class Test_001_CopyCalc(test_copycalc.Test_000_Calculator):
   pass

if __name__ == "__main__":
    unittest.main()