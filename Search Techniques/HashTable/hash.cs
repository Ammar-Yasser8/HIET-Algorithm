using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace HashTable
{
    public class Hash
    {
        int buckets; // size of the hash table
        List<int>[] table; // the hash table itself

        // intialize the hash table with a given number of buckets
        public Hash(int V)
        {
            this.buckets = V;
            table = new List<int>[buckets];
            for (int i = 0; i < buckets; i++)
                table[i] = new List<int>();
        }

        // Hash fubcation to map values to key
        public int HashFunction(int key)
        {
            return key % buckets;
        }
        // Insert a key into the hash table
        public void Insert(int key)
        {
            int index = HashFunction(key);
            table[index].Add(key);
        }
        // Displays the hash table
        public void displayHash()
        {
            for (int i = 0; i < buckets; i++)
            {
                Console.Write(i + " --> ");
                foreach (int x in table[i])
                    Console.Write(x + " ");
                Console.WriteLine();
            }
        }

    }
}
