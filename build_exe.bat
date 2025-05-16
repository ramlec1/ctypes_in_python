gcc -c main.c
gcc -o main.exe main.o -L. -lfunctions
del /S *.o