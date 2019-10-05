namespace Cracking.Chapter1
{
    /// <summary>
    /// Assume you have a method isSubstring which checks if one word is a
    /// substring of another. Given two strings, s1 and s2, write code to check
    /// if s2 is a rotation of s1 using only one call to isSubstring (i.e.,
    /// "waterbottle" is a rotation of "erbottlewat").
    /// </summary>
    interface IProblem8
    {
        bool IsRotation(string left, string right);
    }
}
