using System.Collections.Generic;

namespace Cracking.Chapter1
{
    class Solution1 : IProblem1
    {
        public bool HasUniqueMembers<T>(T[] ts) =>
            new HashSet<T>(ts).Count == ts.Length;
    }
}
