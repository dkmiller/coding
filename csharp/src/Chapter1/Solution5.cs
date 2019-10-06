using System;
using System.Linq;

namespace Cracking.Chapter1
{
    public class Solution5 : IProblem5
    {
        public T[] Replace<T>(T[] ts, T source, T[] target)
            where T : notnull
        {
            var sourceCount = ts.Where(t => source.Equals(t))
                .Count();

            var gap = sourceCount * (target.Length - 1);
            if (gap > 0)
            {
                var oldLength = ts.Length;
                var newLength = oldLength + gap;
                Array.Resize(ref ts, newLength);

                var slot = newLength - 1;
                for (var i = oldLength - 1; i >= 0; --i)
                {
                    if (ts[i].Equals(source))
                    {
                        // TODO: do something!
                    }
                    else
                    {
                        // TODO: do something!
                    }
                }
            }

            return ts;
        }
    }
}
