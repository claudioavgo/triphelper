import unittest
from dependencies.colors import Colors
from tests.homepage import *
from tests.favorites import *

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super(CustomTextTestResult, self).addSuccess(test)
        self.stream.writeln(f"{Colors.LIGHT_GREEN}{Colors.BOLD}✓ {Colors.DARK_GRAY}{test}{Colors.END}")
        
    def addFailure(self, test, err):
        super(CustomTextTestResult, self).addFailure(test, err)
        self.stream.writeln(f"{Colors.LIGHT_RED}{Colors.BOLD}✗ {Colors.DARK_GRAY}{test}{Colors.END}")

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(HomePageCases)
    suite2 = loader.loadTestsFromTestCase(FavoriteCases)

    result = CustomTextTestResult(None, None, 1)
    runner = unittest.TextTestRunner(verbosity=0, resultclass=CustomTextTestResult)
    
    runner.run(suite)
    runner.run(suite2)