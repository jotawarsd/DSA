#include <stdio.h>

int main()
{
    int A[50], dim, sum;
    printf("enter dimension of array :");
    scanf("%d", &dim);

    for(int i = 0; i < dim; i++)
    {
        printf("element %d: ", i + 1);
        scanf("%d", &A[i]);
    }

    for(int j = 0; j < dim; j++)
    {
        sum += A[j];
    }

    printf("summation = %d \n", sum);
}