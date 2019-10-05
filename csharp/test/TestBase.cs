using System;
using System.Linq;

namespace Cracking.Tests
{
    /// <summary>
    /// Base utility for testing solutions to problem specifications.
    /// </summary>
    public class TestBase<TProblem> where TProblem : notnull
    {
        private Type SolutionType { get; }

        /// <summary>
        /// A new instance of <typeparamref name="TProblem"/> is created
        /// on each call of this property.
        /// </summary>
        protected TProblem Solution =>
            (TProblem)Activator.CreateInstance(SolutionType);

        /// <summary>
        /// Parameterless constructor. This will throw an exception unless
        /// there is a unique type implementing <typeparamref name="TProblem"/>.
        /// </summary>
        public TestBase()
        {
            var type = typeof(TProblem);

            SolutionType = type
                .Assembly
                .GetTypes()
                .Where(type.IsAssignableFrom)
                .Where(HasParameterlessConstructor)
                .Single();
        }

        /// <summary>
        /// Follow https://stackoverflow.com/a/16162301 to detect if
        /// <paramref name="t"/> has a parameterless constructor.
        /// </summary>
        private static bool HasParameterlessConstructor(Type t) =>
            t.GetConstructor(Type.EmptyTypes) != null;
    }
}
