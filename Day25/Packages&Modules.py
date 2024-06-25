"""
Modules means Python files
Packages means  folders or Modules ( Modules are python files and folders may contain other folders or Modules)


Package:
   Module---A----A
                  **b
                     **Module (c.py)
                        def abc:

import A.b.c as e
e.abc()


pip: Python Package Manager
To install libraries
pip install flask, Django

"""

import math
print(math.pi)