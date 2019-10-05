using Cracking.Chapter1;
using Xunit;

namespace Cracking.Tests.Chapter1
{
    public class Problem1Tests : TestBase<IProblem1>
    {
        [Theory]
        [InlineData("", true)]
        [InlineData("a", true)]
        [InlineData("aa", false)]
        [InlineData("aabc", false)]
        [InlineData("abcdefghijklmnopqrstuvwxyz", true)]
        [InlineData("abcdefghijklmnopqrstuvwxyza", false)]
        public void ExpectedBehavior(string items, bool result) =>
            Assert.Equal(
                result,
                Solution.HasUniqueMembers(items)
                );
    }
}
