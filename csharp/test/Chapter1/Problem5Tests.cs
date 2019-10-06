using Cracking.Chapter1;
using Xunit;

namespace Cracking.Tests.Chapter1
{
    public class Problem5Tests : TestBase<IProblem5>
    {
        [Theory]
        [InlineData("", "")]
        [InlineData("a", "a")]
        [InlineData("a ", "a%20")]
        public void Expected(string input, string expected) =>
            Assert.Equal(expected, Solution.Replace(input));
    }
}
