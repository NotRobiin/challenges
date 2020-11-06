using System;
using System.Linq;

public class Program {
	public static int CountDs(string str)
	{
		return str.ToLower().Count(c => c == 'd');
	}
}