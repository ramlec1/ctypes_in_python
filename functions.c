#include "functions.h"


int cloop(int n)
{
	int count = 1;
	for(int i = 1; i != n; ++i)
	{
		if(i%2==0){
			count += 5;
		}

		if(i%2==1){
			count -= 5;
		}
	}

	return count;
}


VALUES* array_print(double *array1, size_t size)
{
	for (size_t i=0; i<size; i++)
	{
		printf("%lf \n", array1[i]);
	}
	printf("\n");
	
}

/*_________________________array pass and return cpython______________________*/


VAL* array(double* arr1, size_t size)
/*  
fill VAL member arrays with input array data	
*/
{
	// initialize and reserve memory to the pointer to the struct, 
	// and check if the pointer exists.
    VAL *p = new_val(size*3);
    if(!p) {printf("func: no struct\n");}

	// fill the members of the struct with content of arr1
    for (size_t i=0; i<size; i++)
    {
        p->vala[i] = arr1[i];
        p->valb[i] = arr1[size+i];
        p->valc[i] = arr1[size*2+i];

		// check if assignment was correct
        // printf("a: %lf \t b: %lf \t c: %lf \n", p->vala[i], p->valb[i], p->valc[i]);
    }
    
    return p;
}

VAL* new_val(size_t size)
/*	
create VAL struct and reserve memory    
*/
{
    VAL *p = (VAL*) malloc(sizeof(VAL));
    if (p == NULL)
    {
        printf("p==NULL\n");
        return NULL;
    }

	// allocate struct member memory
    p->vala = malloc(sizeof(double)*size);
    p->valb = malloc(sizeof(double)*size);
    p->valc = malloc(sizeof(double)*size);

	// check if members exist
    if (p->vala == NULL && p->valb == NULL && p->valc == NULL) 
    {
        free (p);
        return NULL;
    }

    return p; 
}

void del_val(VAL* val)
/*	
Free memory of array 
*/
{
    if(val != NULL)
    {
        free(val->vala);
        free(val->valb);
        free(val->valc);
        free(val);
    }
}
