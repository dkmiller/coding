using System.Collections.Generic;

namespace Cracking.Chapter1
{
    /// <summary>
    /// Given an image represented by an NxN matrix, where each pixel in the
    /// image is 4 bytes, write a method to rotate the image by 90 degrees.
    /// Can you do this in place?
    /// </summary>
    interface IProblem6
    {
        void Rotate(IList<IList<byte[]>> image);
    }
}
