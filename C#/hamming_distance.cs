public class Program
{
    public static int HammingDistance(string str1, string str2)
    {
        int diff = 0;

        for (int i = 0; i < str1.Length; i++)
        {
            if (str1[i] == str2[i])
            {
                continue;
            }

            diff++;
        }

        return diff;
    }
}