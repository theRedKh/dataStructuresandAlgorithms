/* Trying out selection sort
* 9/12/24
*/
#include <stdio.h>

int main(){
    
    //SELECTION SORT
    int arr[] = {1,3,5,4,2,6}; //unsorted array
    int small = 0; //smallest value pointer
    int j = 0; //loops through the rest of the array
    int n=6; //array size

    //print unsorted array
    printf("Unsorted array: \n");
    for (int i=0; i < 6; i++){
        printf("%d ", arr[i]);
    }
    printf("\nSorted Array: \n");


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
