gcc -c -DBUILD_MY_DLL functions.c
gcc -shared -o functions.dll functions.o -Wl,--out-implib,libfunctions.a
del /S *.o