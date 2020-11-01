public class Program
{
    public static string Bomb(string txt)
    {
        txt = txt.ToLower();

        return txt.IndexOf("bomb") == -1 ? "There is no bomb, relax." : "Duck!!!";
    }
}