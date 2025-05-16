gcc -c -fPIC functions.c -o functions.o
gcc functions.o -shared -o libfunc.so
del /S *.a *.o