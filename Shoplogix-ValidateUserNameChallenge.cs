using System;

public class Username
{
    public static bool Validate(string username)
    {

        /*
         * Rules: 
         * 1) Minimum length of username should be 6 characters
         * 2) Only Alphabets or Numbers or ONE hyphen only.
         * 3) The last letter cannot be a hyphen
         * 4) The first letter should be an alphabet
         * 5) Should have atleast one upper case letter, one lower case letter and atleast one number 
         * The fifth rule was added by me as a variation.
         * 
        */
        if (username == null || username.Length < 6) return false;

        bool hyphen = false, upperCase = false, lowerCase = false, number = false;
        char firstLetter = username[0];

        if (!char.IsLetter(firstLetter) || username.EndsWith("-"))
            return false;

        foreach (char c in username)
        {
            
            if (!(char.IsLetterOrDigit(c)))
            {
                if (c == '-')
                {
                    if (hyphen) return false;
                    else hyphen = true;
                }
                else return false;
            }
            else
            {
                if (char.IsLetter(c))
                {
                    if (char.IsUpper(c)) upperCase = true;
                    else if (char.IsLower(c)) lowerCase = true;
                }
                else number = true;
            }
        }
        if (upperCase && lowerCase && number)
            return true; // Satisfied all conditions of the username
        else return false; 
    }

    public static void Main(string[] args)
    {
        Console.WriteLine(Validate("Mike-Standish1")); // Valid username
        Console.WriteLine(Validate("Mike Standish")); // Invalid username - Because of space
        Console.WriteLine(Validate("Mike")); //Invalid because length
        Console.WriteLine(Validate("123sndjasndkjasndkjasndakjdn")); // Starts with a number
        Console.WriteLine(Validate("dnakjsdnakjsdnakjsdnkjasA1dn-")); // Ends with a -
        Console.WriteLine(Validate("sdnasdkjndjkasdnkjasndkjasnd")); // No number and upper case 
        Console.WriteLine(Validate("Mikenaskjdnadkjsn-asdaskjdnakjsd-")); // Two hyphens
        Console.WriteLine(Validate("MarkZucker1")); // True
        Console.WriteLine(Validate("-asdasdasdA1")); // First letter hyphen - false

        Console.ReadKey();
    }
}