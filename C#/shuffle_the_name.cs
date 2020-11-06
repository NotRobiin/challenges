using System;

public class Program
{
    public static string NameShuffle(string str)
    {
        string[] output = str.Split(' ');

        return String.Format("{0} {1}", output[1], output[0]);
    }
}