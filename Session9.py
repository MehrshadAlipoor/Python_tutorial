# Date: 11/04/2025
# ==================================================================================================
# ======================== Error handling in Python ========================================
# Linter in error handling:
# - A linter is a tool that analyzes code for potential errors, style issues, and best practices.
# - It helps identify problems in the code before it is executed, making it easier to catch errors early in the development process.
# - Linters can provide suggestions for improving code quality and readability.
# - Examples of popular Python linters include pylint, flake8, and black.
# - Linters can be integrated into code editors and IDEs to provide real-time feedback while writing code.
# - Using a linter can help maintain consistent coding standards and improve collaboration among developers.

# Pylint:
# - Pylint is a widely used linter for Python that checks for errors, enforces coding standards, and suggests improvements.
# - It analyzes the code for potential issues such as syntax errors, undefined variables, and unused imports.
# How to install pylint:
    # pip install pylint
# How to run pylint:
    # pylint <filename.py>
# Example of using pylint:
    # def add_numbers(a, b):
    #     return a + b  # Correct operation (addition)
    # result = add_numbers(5, 3)
    # print(result)  # Output will be 8

    # # pylint: disable=unused-variable
    # # pylint: disable=missing-docstring
    # # pylint: disable=invalid-name
    # # pylint: disable=too-many-arguments
    # # pylint: disable=too-many-locals
    # # pylint: disable=too-many-statements
    # # pylint: disable=too-many-branches
    # # pylint: disable=too-many-return-statements
    # # pylint: disable=too-many-nested-blocks
    # # pylint: disable=too-many-public-methods

# Diffrence between linter and formatter:
    # - A linter checks for potential errors and enforces coding standards, 
    # while a formatter focuses on code formatting and style.
    # - A linter provides suggestions for improving code quality, 
    # while a formatter automatically applies formatting changes.
    # - A linter helps identify issues in the code, 
    # while a formatter ensures consistent code appearance.
    # - A linter can be used to catch potential bugs and improve code readability,
    # while a formatter is primarily concerned with code aesthetics.


# Report command in pylint:
    # pylint --reports=y <filename.py>

# black:
# - Black is a popular code formatter for Python that automatically formats code to conform to PEP 8 style guidelines.
# - It focuses on code readability and consistency, making it easier to maintain codebases.
# - Black can be integrated into code editors and IDEs for real-time formatting.

# PEP 8:
# - PEP 8 is the official style guide for Python code.
# - It provides guidelines for writing clean and readable Python code.
# - For example it recommends using 4 spaces for indentation, limiting lines to 79 characters, and using blank lines to separate functions and classes.

# ===========================================================================================
# Testing in Python:
# - Testing is the process of evaluating a program or system to identify any errors or defects.
# - It is an essential part of the software development process to ensure that the code works as intended.
# - Testing helps identify bugs, improve code quality, and ensure that the software meets the requirements.
# - Testing can be done manually or automatically using testing frameworks and tools.
# - Testing can be done at different levels, including unit testing, integration testing, and system testing.


# Types of Testing:
# - Unit Testing: Testing individual components or functions in isolation.
# - Integration Testing: Testing the interaction between different components or modules.
# - System Testing: Testing the entire system as a whole to ensure it meets the requirements.
# - Acceptance Testing: Testing the system from the user's perspective to ensure it meets their needs.
# - Regression Testing: Testing the system after changes or updates to ensure that existing functionality is not affected.
# - Performance Testing: Testing the system's performance under various conditions, such as load and stress testing.
# - Security Testing: Testing the system for vulnerabilities and security risks.
# - Usability Testing: Testing the system's user interface and user experience to ensure it is user-friendly.
# - Smoke Testing: A preliminary test to check the basic functionality of the system.
# - Sanity Testing: A quick test to check if a specific functionality is working after changes or updates.
# - Exploratory Testing: Testing the system without a predefined test plan to discover unexpected issues.
# - Automated Testing: Using tools and frameworks to automate the testing process.

# Unit test:
# - Unit testing is a software testing technique that involves testing individual components or functions of a program in isolation.
# - The goal of unit testing is to verify that each component works as intended and produces the expected results.
# - Unit tests are typically written by developers and are executed automatically as part of the development process.
# - Unit tests help identify bugs and issues early in the development process, making it easier to fix them before they become larger problems.
# - Unit tests are usually written using a testing framework, such as unittest or pytest, which provides tools and utilities for writing and running tests.
# - Unit tests are typically small and focused on a specific functionality or behavior of the code.

# How to write a unit test in Python using unittest:
# - Import the unittest module in a new Python file.
# - Create a test class that inherits from unittest.TestCase.
# - Define test methods within the class, using the prefix "test_" to indicate that they are test cases.
# - Use assertion methods provided by unittest to check the expected results.
# - Run the tests using unittest.main() or a test runner.
# Example of a simple unit test using unittest:

# a program to do sum calculation for GPA with Test cases
def calculate_gpa(grades):
    """Calculate the GPA based on a list of grades."""
    if not grades:
        return 0.0
    total_points = sum(grades)
    return total_points / len(grades)


import unittest

class TestGPA(unittest.TestCase):
    def test_calculate_gpa(self):
        # Test with valid grades
        grades = [3.5, 4.0, 2.8, 3.2]
        expected_gpa = (3.5 + 4.0 + 2.8 + 3.2) / 4
        self.assertAlmostEqual(calculate_gpa(grades), expected_gpa)

    def test_empty_grades(self):
        # Test with empty grades list
        self.assertEqual(calculate_gpa([]), 0.0)

    def test_single_grade(self):
        # Test with a single grade
        self.assertEqual(calculate_gpa([3.0]), 3.0)


    def test_invalid_grades(self):
        # Test with invalid grades (negative values)
        with self.assertRaises(ValueError):
            calculate_gpa([-1.0, 2.5, 3.0])


    def test_invalid_grades_type(self):
        # Test with invalid grades (non-numeric values)
        with self.assertRaises(TypeError):
            calculate_gpa(['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()
# - The unittest module is a built-in Python module that provides a framework for writing and running unit tests.

# Running the tests for the above code:

grades = [3.5, 4.0, 2.8, 3.2]
expected_gpa = (3.5 + 4.0 + 2.8 + 3.2) / 4
print("Expected GPA:", expected_gpa)
print("Calculated GPA:", calculate_gpa(grades))

# - The unittest module provides a framework for writing and running unit tests in Python.
# - It includes features such as test discovery, test organization, and test reporting.

# Important assertion methods in unittest:
# - assertEqual(a, b): Check if a and b are equal.
# - assertNotEqual(a, b): Check if a and b are not equal.
# - assertTrue(expr): Check if expr is True.
# - assertFalse(expr): Check if expr is False.
# - assertIsNone(expr): Check if expr is None.
# - assertIsNotNone(expr): Check if expr is not None.
# - assertRaises(exception, func, *args, **kwargs): Check if the specified exception is raised when calling func with the given arguments.

# TDD:
# - Test-Driven Development (TDD) is a software development approach that emphasizes writing tests before writing the actual code.
# - In TDD, developers write a test case for a specific functionality, run the test to see it fail, and then write the code to make the test pass.
# - This cycle is repeated for each new feature or functionality.


# ===========================================================================================
# Library vs Framework:
# - A library is a collection of pre-written code that can be used to perform specific tasks or functions.
# - A library provides a set of functions and classes that can be used to build applications.
# - A framework is a pre-defined structure or skeleton for building applications.
# - A framework provides a set of rules and guidelines for building applications, along with pre-defined components and libraries.
# - A libreary can be used independently, while a framework requires the use of its components and structure.
# - for example when you use Django framework you have to follow its structure and rules,
# while when you use a library like NumPy you can use it independently without following any specific structure.
# - A library is typically smaller and more focused on specific tasks, while a framework is larger and provides a more comprehensive solution for building applications.
# - A library is often used to extend the functionality of a program, while a framework provides a foundation for building applications.





# ==========================================================================================



