public class Program 
{
    public static int CharCount(char myChar, string str) 
    {
        int amt = 0;

        foreach (char c in str)
        {
            if(c == myChar)
            {
                amt++;
            }
        }

        return amt;
    }
}
