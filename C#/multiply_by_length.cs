public class Program
{
    public static int[] MultiplyByLength(int[] arr)
    {
        int len = arr.Length;
        int[] output = new int[len];

        for (int i = 0; i < len; i++)
        {
            output[i] = arr[i] * len;
        }

        return output;
    }
}