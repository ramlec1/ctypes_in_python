This example script shows a number of ways on how to implement C functions in Python. It also includes some batch files to create the required .dll or .so files using the gcc compiler. 
The first example implements a simple for-loop and tests the performance difference between python and C. Then a string defined in python is printed using C code. And finally a multidimensional array is defined in python and then loaded into C. 
The C code does not do anything but return the array back as a numpy array. It serves just as an example of how to do this. Any wanted operation done to the array can be adjusted in the C code.

The code may look a bit messy, but it simply serves as an example of how ctypes can be implemented. 
