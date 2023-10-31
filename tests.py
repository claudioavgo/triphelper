import unittest
from dependencies.colors import Colors

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super(CustomTextTestResult, self).addSuccess(test)
        self.stream.writeln(f"{Colors.LIGHT_GREEN}{Colors.BOLD}✓ {Colors.DARK_GRAY}{test._testMethodName} ({test.__class__.__name__}){Colors.END}")

    def addFailure(self, test, err):
        super(CustomTextTestResult, self).addFailure(test, err)
        self.stream.writeln(f"{Colors.LIGHT_RED}{Colors.BOLD}✗ {Colors.DARK_GRAY}{test._testMethodName} ({test.__class__.__name__}){Colors.END}")

if __name__ == "__main__":
    print()
    print(f"{Colors.LIGHT_WHITE}{Colors.NEGATIVE}{Colors.BOLD} TEST CASES {Colors.END}")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Use discover to find and load test cases from the "./tests" directory
    discover = unittest.defaultTestLoader.discover(start_dir="./tests", pattern="*.py")
    suite.addTest(discover)

    result = CustomTextTestResult(None, None, 1)
    runner = unittest.TextTestRunner(verbosity=2, resultclass=CustomTextTestResult)

    runner.run(suite)