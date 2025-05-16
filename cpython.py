import ctypes
import time as tm
import numpy as np
from numpy.ctypeslib import ndpointer, as_array
import os


class VAL(ctypes.Structure):
    ''' Class containing the data returned from a C-function in the form of a
    C-struct. Class is used in the c_arrays.'''
    _fields_ = [('vala', ctypes.POINTER(ctypes.c_double)),
                ('valb', ctypes.POINTER(ctypes.c_double)),
                ('valc', ctypes.POINTER(ctypes.c_double))]


def pyloop(n):
    ''' Arbitrary python loop for time comparisson with c-loop.'''
    count = 1
    for i in range(1,n):
        if i%2==0:
            count += 5
        if i%2==1:
            count -= 5
    return count


def p_vs_c(c_func):
    ''' Compare python vs C speed. Runs two arbitrary loops in python and C.
    Prints the runtime for both loops.'''
    n=10000000
    pystart = tm.time()
    pyloop(n)
    pyend = tm.time()

    cstart = tm.time()
    c_func.cloop(n)
    cend = tm.time()

    print("\nSpeed comparisson between Python and C")
    print("Python loop time is: ", pyend-pystart)
    print("C loop time is: ", cend-cstart, "\n")


def c_array_print(c_func, data):
    ''' Pass a numpy array to a c-function and print its contents.'''

    # declare the expected arguments and return variables expected in the c-function
    fun = c_func.array_print
    fun.restype = None
    fun.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                    ctypes.c_size_t]

    # reformat input array and run c-function                
    f_data = data.flatten()
    print("Numpy array printed elementwise by C-function:")
    c_func.array_print(f_data, len(f_data))


def c_arrays(c_func, data):
    ''' Pass numpy array to a C-function. The input data processed and returned
    as a C-struct containing 3 double pointers as members. The C-struct is then
    read by python as the VAL class. Using cast and from buffer, the datamember 
    pointers are converted to numpy arrays.'''

    # declare the expected arguments and return variables expected in the c-function
    c_arr = c_func.array
    c_del_val = c_func.del_val
    
    c_arr.restype = ctypes.c_void_p
    c_arr.argtypes = [ndpointer(ctypes.c_double, flags='C_CONTIGUOUS'), 
                        ctypes.c_size_t]
    c_del_val.restype = None
    c_del_val.argtype = ctypes.c_void_p

    # reformat input array and run c-function 
    size = len(data)
    f_data = data.flatten()
    p1 = VAL.from_address(c_arr(f_data,size))

    # convert data from pointers in the VAL class to numpy arrays
    ap = ctypes.cast(p1.vala, ctypes.POINTER(ctypes.c_double*size))
    a = np.frombuffer(ap.contents)
    bp = ctypes.cast(p1.valb, ctypes.POINTER(ctypes.c_double*size))
    b = np.frombuffer(bp.contents)
    cp = ctypes.cast(p1.valc, ctypes.POINTER(ctypes.c_double*size))
    c = np.frombuffer(cp.contents)

    # check if the data is returned correctly and as numpy arrays
    print("Print the contents of the C-function struct as numpy arrays:")
    print("Array a = ", a, "\t of type ", type(a))
    print("Array b = ", b, "\t of type ", type(b))
    print("Array c = ", c, "\t of type ", type(c))

    # free the memory of the struct in C
    c_del_val(ctypes.byref(p1))


def main():
    # call C funtions from a .so shared library (Linux, mac)
    # c_func = ctypes.CDLL("./libfunc.so")
    c_func = ctypes.WinDLL("./functions.dll") # .dll (windows)


    '''__________________ Call C Functions ______________________'''
    # perform loop and see speed difference python vs C
    p_vs_c(c_func)

    # pass array as argument and print
    c_array_print(c_func, np.array([[6.,3.,5.,5.],[1.,2.,4.,5.]]))

    # pass array as argument, perform operations, return new array
    # IMPORTANT: sub arrays must be of same size! (reason yet unknown)
    data = np.array([[6.,3.,5.],[1.,2.,4.],[1.,2.,3.],[4.,5.,6.],[7.,8.,9.],[10.,11.,12.]])
    c_arrays(c_func, data)

if __name__ == "__main__":
    main()
