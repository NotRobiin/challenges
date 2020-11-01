public class Program
{
    public static string GetFilename(string path)
    {
        string[] sub = path.Split('/');

        return sub[sub.Length - 1];
    }
}