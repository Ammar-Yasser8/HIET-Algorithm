
// Bubble Sort algorithm 
// Steps:
// 1. Start at the beginning of the array.  
// 2. Compare the first two elements. If the first is greater than the second, swap them.
// 3. Move to the next pair of elements and repeat step 2 until the end of the array is reached.


// complixity: O(n^2)

// input: [64, 34, 25, 12, 22, 11, 90]

int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
 for(int i= 0; i< arr.Length -1; i++)
 {
    for(int j= 0; j<arr.Length -i -1; j++)
    {
        if (arr[j] > arr[j+1])
        {
            // swap arr[j] and arr[j+1]
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }


    }

 }
// print sorted array
Console.WriteLine("Sorted array: ");
foreach(var item in arr)
{
    Console.Write(item + " ");
}