public class Program
{
    public static string smallerNum(string n1, string n2)
    {
        int a = int.Parse(n1);
        int b = int.Parse(n2);

        if (a > b)
        {
            return n2;
        }

        return n1;

    }
}