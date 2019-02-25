#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>


void printTabs(int time){
	printf(" \\null ");
	for(int i = 0; i< time; i++){
		printf(" \\quad ");
	}
}
//assumes little endian
void printBits(size_t const size, void const * const ptr, int bits){
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=9-1;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    printf("\\\\ \n");
}

unsigned int divideAndConquerMultiplication(uint8_t a, uint8_t b, size_t size, int recLevel){


	if(recLevel != 0){
		printTabs(recLevel);
		printf("Recursion level %d \\\\ \n", recLevel);
	}
	if(recLevel == 0){

		printTabs(recLevel);
		printf("AT ORIGIN LEVEL  %d \\\\ \n", recLevel);
	}


	if(size == 1){

		printTabs(recLevel);
		printf("Base case reached: x = %d, y =  %d, xy = %d \\\\ \n", a,b, a*b);
		return a*b;
	}

		printTabs(recLevel);
	printf(" x\t= ");
	printBits(1,&a, size);
		printTabs(recLevel);
	printf(" y\t= ");
	printBits(1,&b, size);
	size_t shift_factor = size/2;
	
	uint8_t xr = a << 8 - shift_factor;
	xr = xr >> 8 - shift_factor;
	
	uint8_t xl = a >> shift_factor;
		printTabs(recLevel);
	printf(" xl\t= ");
	printBits(1,&xl, shift_factor);
		printTabs(recLevel);
	printf(" xr\t= ");
	printBits(1,&xr, shift_factor);
	uint8_t yr = b << 8 - shift_factor;
	yr = yr >> 8 - shift_factor;
	uint8_t yl = b >> shift_factor;
		printTabs(recLevel);
	printf(" yl\t= ");
	printBits(1,&yl, shift_factor);
		printTabs(recLevel);
	printf(" yr\t= ");
		printTabs(recLevel);
	printBits(1,&yr, shift_factor);	
		printTabs(recLevel);
	printf("Recursion level %d at branch %d \\\\ \n", recLevel, 1);
	unsigned int  p1 = divideAndConquerMultiplication(xl, yl, shift_factor, recLevel + 1);
		printTabs(recLevel);
	printf("Recursion level %d at branch %d \\\\ \n", recLevel, 2);
	unsigned int  p2 = divideAndConquerMultiplication(xr, yr, shift_factor, recLevel + 1);
		printTabs(recLevel);
	printf("Recursion level %d at branch %d \\\\ \n", recLevel, 3);
	unsigned int  p3 = divideAndConquerMultiplication(xl+xr, yl+yr, shift_factor, recLevel + 1);

		printTabs(recLevel);
	printf("p1 = %d, p2 = %d, p3 = %d \\\\ \n", p1, p2, p3);
	if(recLevel - 1 != -1){
		printTabs(recLevel);
		printf("Answer received for recursion level %d, returning to recursion level  %d \\\\ \n", recLevel, recLevel - 1);
	}

	return (p1 << size) + ((p3 - p1 - p2)<< shift_factor) + p2;
	return 0;
}

int main(){
	printf("Multiplying number of %ld bits \\\\ \n", sizeof(uint8_t)*8);
	printf("FULL ANSWER : %d \\\\ \n",	divideAndConquerMultiplication(155,186,8,0));
}


