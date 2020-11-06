using System.Globalization;

public class Program
{
    public static string MonthName(int num)
    {
        return CultureInfo.CurrentCulture.DateTimeFormat.GetMonthName(num);
    }
}