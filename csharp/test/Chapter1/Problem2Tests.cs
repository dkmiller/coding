using Cracking.Chapter1;
using System.Linq;
using Xunit;

namespace Cracking.Tests.Chapter1
{
    public class Problem2Tests : TestBase<IProblem2>
    {
        [Theory]
        [InlineData(" ", " ")]
        [InlineData("a ", "a ")]
        [InlineData("ab ", "ba ")]
        [InlineData("ab a", "ba a")]
        [InlineData("abcdefghijkl ab", "lkjihgfedcba ab")]
        [InlineData("abcdefghijklm ab", "mlkjihgfedcba ab")]
        public void ExpectedBehavior_WithSpaceAsNull(string input, string expected)
        {
            var inputAsArray = input
                .Select(c => c == ' ' ? (char?)null : c)
                .ToArray();

            Solution.Reverse(inputAsArray);

            var inputAsString = string.Concat(
                inputAsArray.Select(c => c is null ? ' ' : c)
                );

            Assert.Equal(expected, inputAsString);
        }
    }
}
