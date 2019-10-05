namespace Cracking.Chapter1
{
    /// <summary>
    /// Write code to reverse a C-Style String. (C-String means that "abcd"
    /// is represented as five characters, including the null character.)
    /// </summary>
    public interface IProblem2
    {
        T?[] Reverse<T>(T?[] ts) where T : struct;
    }
}
