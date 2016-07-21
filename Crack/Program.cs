using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Crack
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Input string: ");
            var s = Console.ReadLine();
            Console.WriteLine(HasUniqueCharacters(s));
            Console.WriteLine(Reverse(s.ToCharArray()));
        }

        /// <summary>
        /// Chapter 1, 1.1. Returns true if and only if the string s has unique 
        /// characters.
        /// </summary>
        static bool HasUniqueCharacters(string s)
        {
            if (s == null)
                return true;

            var count = new Dictionary<char, bool>();

            foreach(char c in s) {
                if (count.ContainsKey(c))
                    return false;
                else
                    count[c] = true;
            }
            return true;
        }

        /// <summary>
        /// Chapter 1, 1.2. Reverses a "C-style string", i.e. character array 
        /// with  null character at the end.
        /// </summary>
        static T[] Reverse<T>(T[] ts)
        {
            if (ts == null)
                return null;

            var l = ts.Length;
            T holder;

            // String only needs to be reversed if more than one non-null char.
            if (l > 2)
            {
                for (var i = 0; i < l/2; i++)
                {
                    holder = ts[i];
                    ts[i] = ts[l - 2 - i];
                    ts[l - 2 - i] = holder;
                }
            }
            return ts;
        }

    }
}
