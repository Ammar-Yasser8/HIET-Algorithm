/*We have array of integers and we want to find a specific integer in
 that array using linear search algorithm.*/

// The array may be unsorted or sorted, but linear search does not require

/* Linear search is a simple algorithm that checks each element in the
 array one by one until it finds the target value or reaches the end of the array.*/

// for example, if we have an array of integers [3, 5, 2, 4, 9] and we want to find place of 2

// Decalar the array of integers
int[] numbers = { 3, 5, 2, 4, 9 };
// The target value we want to find
int target = 10;
for(int i =0;  i < numbers.Length; i++)
{
    // Check if current element is equal to target
    if (numbers[i]== target)
        {
        Console.WriteLine($"Target {target} found at index {i}");
        // Exit the loop once we find the target
        break; 
    }
    // If we reach the end of the array without finding the target
    if (i == numbers.Length - 1)
    {
        Console.WriteLine($"Target {target} not found in the array");
    }
}


