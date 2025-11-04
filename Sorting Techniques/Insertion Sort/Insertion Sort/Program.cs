/*
 * Insertions sort algirithm implementation in c# 
 * 
 * What is Insertion Sort? Sort an array 
 * by repeatedly taking an element from the unsorted portion and inserting it into 
 * the correct position in the sorted portion.*/
//------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------
//complexity: O(n^2) time complexity in the worst and average cases,
//O(n) in the best case (when the array is already sorted).
//------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------

// Insertion Sort Algorithm Steps:
// Step 1 If it is the first element, it is already sorted. return 1;
// Step 2 Take the next element from the unsorted portion.
// Step 3 Compare it with the elements in the sorted portion from right to left.
// Step 4 Shift all elements in the sorted portion that are greater than the current element to the right.
// Step 5 Insert the current element into its correct position in the sorted portion.
// Step 6 Repeat steps 2-5 until the entire array is sorted.
//------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------

//Example: Input: [5, 2, 9, 1, 5, 6]
// Output: [1, 2, 5, 5, 6, 9]

// Decalre the array to be sorted
int[] array = { 5, 2, 9, 1, 5, 6 };
for (int i = 0;  i < array.Length-1;  i++)
{
    // declare the current element to be compared
    int currentElement = array[i + 1];
    // declare the index of the previous element
    int j = i;
    // compare the current element with the previous elements
    while (j >= 0 && array[j] > currentElement)
    {
        // shift the previous element to the right
        array[j + 1] = array[j];
        j--;
    }
    // insert the current element into its correct position
    array[j + 1] = currentElement;

}

Console.WriteLine("Sorted array: " + string.Join(", ", array));



