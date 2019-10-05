using System.Collections.Generic;

namespace Cracking.Chapter1
{
    /// <summary>
    /// Write an algorithm such that if an element in an MxN matrix is 0,
    /// its entire row and column is set to 0.
    /// </summary>
    interface IProblem7
    {
        void Normalize<T>(IList<IList<T>> matrix, T t);
    }
}
