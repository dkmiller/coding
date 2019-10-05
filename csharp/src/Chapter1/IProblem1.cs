namespace Cracking.Chapter1
{
    /// <summary>
    /// Implement an algorithm to determine if a string has all unique
    /// characters. What if you can not use additional data structures?
    /// </summary>
    public interface IProblem1
    {
        bool HasUniqueMembers<T>(T[] ts);

        bool HasUniqueMembers(string s) =>
            HasUniqueMembers(s.ToCharArray());
    }
}
