using System.Collections.Generic;
using System.Linq;

namespace Cracking.Chapter1
{
    public class Solution4 : IProblem4
    {
        public bool AreAnagrams<T>(IList<T> left, IList<T> right)
        {
            var leftCounts = Counts(left);
            var rightCounts = Counts(right);

            var result = leftCounts.Count == rightCounts.Count;

            if (result)
            {
                result = leftCounts.All(
                    kv => rightCounts.TryGetValue(kv.Key, out var value) && kv.Value == value
                    );
            }

            return result;
        }

        private static IReadOnlyDictionary<T, int> Counts<T>(IEnumerable<T> ts) =>
            ts.GroupBy(t => t)
            .ToDictionary(g => g.Key, g => g.Count());
    }
}
