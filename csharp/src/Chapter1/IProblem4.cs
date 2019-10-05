using System.Collections.Generic;

namespace Cracking.Chapter1
{
    /// <summary>
    /// Write a method to decide if two strings are anagrams or not.
    /// </summary>
    public interface IProblem4
    {
        bool AreAnagrams<T>(IList<T> left, IList<T> right);

        bool AreAnagrams(string left, string right) =>
            AreAnagrams(left.ToCharArray(), right.ToCharArray());
    }
}
