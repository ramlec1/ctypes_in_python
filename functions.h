#include "stdio.h"
#include "stdlib.h"

typedef struct
{
	double* hoi;
    double* y;
} VALUES;

typedef struct VAL
{
    double* vala;
    double* valb;
    double* valc;
}VAL;


int cloop(int n);
VALUES *array_print(double *array1, size_t size);

VAL* array(double* arr1, size_t size);
VAL* new_val(size_t size);
void del_val(VAL* val);