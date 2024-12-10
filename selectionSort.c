#include <stdio.h>

int main(){
    
    //SELECTION SORT
    int arr[] = {1,3,5,4,2,6};
    int small = 0;
    int j = 0;
    int n=6;

    printf("Unsorted array: \n");
    for (int i=0; i < 6; i++){
        printf("%d ", arr[i]);
    }
    printf("\n Sorted Array: \n");


    for (int i = 0; i < n-1 ; i++){
        int small = i;
        for (j = i+1; j < n; j++){
            if (arr[j] < arr[small]){
                small = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[small];
        arr[small] = temp;
    }

    //Print sorted array
    for (int i=0; i < 6; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}