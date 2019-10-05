using Cracking.Chapter1;
using Xunit;

namespace Cracking.Tests.Chapter1
{
    public class Problem4Tests : TestBase<IProblem4>
    {
        [Theory]
        [InlineData(true, "", "")]
        [InlineData(true, "a", "a")]
        [InlineData(false, "a", "b")]
        [InlineData(true, "abbc", "cbab")]
        [InlineData(true, "abcdefgg", "gfaebdcg")]
        [InlineData(false, "abcdefgg", "gfaebdcgg")]
        public void ExpectedBehavior(bool expected, string left, string right) =>
            Assert.Equal(
                expected,
                Solution.AreAnagrams(left, right)
                );
    }
}
