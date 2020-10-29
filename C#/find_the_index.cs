public class Program
{
    public static int FindIndex(string[] arr, string str)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] == str)
            {
                return i;
            }
        }

        return -1;
    }
}