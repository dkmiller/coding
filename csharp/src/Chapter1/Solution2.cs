namespace Cracking.Chapter1
{
    class Solution2 : IProblem2
    {
        public void Reverse<T>(T?[] ts) where T : struct
        {
            var length = 0;
            while (ts[length] != null)
            {
                length++;
            }

            for (var i = 0; i < length / 2; ++i)
            {
                Swap(ref ts[i], ref ts[length - i - 1]);
            }
        }

        private void Swap<T>(ref T left, ref T right)
        {
            (left, right) = (right, left);
        }
    }
}
