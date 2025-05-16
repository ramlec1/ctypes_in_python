#include "functions.h"

int main(){
	// initialize 
	size_t size = 5;
	double n[5];
	double m[5];
	VALUES *p = malloc(sizeof(double)*size*2);
	for (int i=0; i<size; i++)
	{
		n[i]=i;
		m[i]=size-i-1;
	}

	p = array_print(n,m,p,size);


	for (size_t i=0; i<size; i++) 
	{
		printf("p.x[%d] = %lf, \t m[%d] = %lf\n", i, p->hoi[i], i, m[i]);
	}
	for (int i=0; i<size; i++) 
	{
		printf("p.y[%d] = %lf, \t n[%d] = %lf\n", i, p->y[i], i, n[i]);
	}


	free(p);
}
