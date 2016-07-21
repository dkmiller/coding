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
        /// Chapter 1, 1.2. Reverses 
        /// </summary>
        static char[] Reverse(char[] s)
        {
            var l = s.Length;
            char holder;

            // String only needs to be reversed if more than one non-null char.
            if (l > 2)
            {
                for (var i = 0; i < l/2; i++)
                {
                    holder = s[i];
                    s[i] = s[l - 1 - i];
                    s[l - 1 - i] = holder;
                }
            }
            return s;
        }
    }
}
