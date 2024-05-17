import os
import sys

import pytest


def find_test_directories(root_dir):
    test_dirs = []
    for _, dirnames, _ in os.walk(root_dir):
        test_dirs = dirnames
        break
    for remove_dir in ['.git', '.pytest_cache', '__pycache__']:
        if remove_dir in test_dirs:
            test_dirs.remove(remove_dir)
    return test_dirs


def run_tests():
    print(f"Running tests in {os.getcwd()}")
    directories = find_test_directories('tests/')
    if len(directories) == 0:
        print("No test directories found")
        sys.exit(0)
    # Run pytest for each test directory
    for test_dir in find_test_directories('tests/'):
        test_dir = os.path.join('tests', test_dir, 'src')
        print(f"Running tests in {test_dir}")
        # Run pytest.main with the test directory
        result = pytest.main([test_dir])
        if result != 0:
            sys.exit(result)


if __name__ == "__main__":
    run_tests()
