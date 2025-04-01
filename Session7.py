# Date: 2025/04/01
# ==================================================================================================
# ======================== Madule and packages in Python ========================================

# what is a module?
    # - A module is a file containing Python code that can define functions, classes, and variables.
    # - A module can also include runnable code.
    # - A module is a way of organizing related code into a single file.
    # - A module can be imported into other modules or scripts using the import statement.

# diffrent methods for importing a module:
    # - import module_name: imports the entire module and allows you to access its functions and classes using the module name.
    # - from module_name import function_name: imports a specific function from the module, allowing you to use it without the module name prefix.
    # - from module_name import *: imports all functions and classes from the module, but this is not recommended as it can lead to naming conflicts.
    # - import module_name as alias: imports the module with an alias, allowing you to use a shorter name for the module.
    # - from module_name import function_name as alias: imports a specific function with an alias, allowing you to use a shorter name for the function.
    # - from module_name import function_name1, function_name2: imports multiple specific functions from the module.
    # example:
        # import math
        # # print(math.sqrt(16))  # Output: 4.0
        # # from math import sqrt
        # # # print(sqrt(16))  # Output: 4.0
        # # from math import sqrt, pi
        # # # print(sqrt(16))  # Output: 4.0
        # # print(pi)  # Output: 3.141592653589793
        # # # import math as m
        # # # print(m.sqrt(16))  # Output: 4.0
        # # # from math import sqrt as s
        # # # print(s(16))  # Output: 4.0
        # # from math import *  # Not recommended
        # # # print(sqrt(16))  # Output: 4.0
        # # print(pi)  # Output: 3.141592653589793
        # # # # from math import sqrt, pi  # Importing multiple functions
        # # # # print(sqrt(16))  # Output: 4.0
        # # # # print(pi)  # Output: 3.141592653589793
        # # # # # import math as m  # Importing with an alias
        # # # # print(m.sqrt(16))  # Output: 4.0    



# what is a package?
    # - A package is a way of organizing related modules into a single directory hierarchy.
    # - A package is a directory that contains a special file called __init__.py, which can be empty or contain initialization code for the package.
    # - A package can contain sub-packages, which are also directories with their own __init__.py files.
    # - A package can be imported using the import statement, just like a module.
    
# installing a package:
    # - You can install packages using package managers like pip or conda.
    # - Example: pip install package_name
    # - Example: conda install package_name
# if a package is not installed using pip or conda, it may be happening because:
    # - The package is not available in the package manager's repository.
    # - The package is not compatible with your Python version. In this case, you may need to check the package's documentation for compatibility information.
        # example:
            # if you are using Python 3.8 and the package is only compatible with Python 3.9 or higher, you may need to upgrade your Python version or find an alternative package like:
            # pip install package_name --upgrade
            # or even use a specific version of pip:
                # pip=3.9 install package_name
                # python3.9 -m pip install package_name
    # - The package is not compatible with your operating system. In this case, you may need to check the package's documentation for compatibility information.
    # - The package has dependencies that are not met. In this case, you may need to install the required dependencies first.   
    # - The package has been deprecated or removed from the repository.
    # - You may need to check the package's documentation for installation instructions or use an alternative package.

import emoji

print(emoji.emojize(':red_heart:'))  # Output: ❤️
print(emoji.emojize(':thumbs_up:'))  # Output: 👍

# drawing a toolbar using tqdm:
from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Loading", unit="item"):
    time.sleep(0.1)  # Simulating a time-consuming task
    # Output: A progress bar that shows the loading progress

# ================================================================================================
# dunder files:
    # - Dunder files are special files in Python that have double underscores before and after their names.
    # - Dunder files are also known as magic methods or special methods.
    # - For creating a package, you need to create a directory with the package name and add an __init__.py file inside it.
    # - The __init__.py file can be empty or contain initialization code for the package.
    # - Dunder files are used to define the behavior of objects and classes in Python.
    