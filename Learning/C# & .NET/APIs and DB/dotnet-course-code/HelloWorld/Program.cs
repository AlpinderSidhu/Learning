// See https://aka.ms/new-console-template for more information
using System;
using System.Net.Http.Headers;

namespace HelloWorld // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
        // array
        string[] myArray = {"A","B","C"};
        System.Console.WriteLine(myArray[2]);
        // List
        List<string> myList =  new List<string>{"A","B","C"};
        System.Console.WriteLine(myList[2]);
                
        // Dictionary
        Dictionary<string,string> myDict = new Dictionary<string, string>{{"Dairy","Cheese"}};
        System.Console.WriteLine(myDict["Dairy"]);
        // Ienumerable
        IEnumerable<string> myI= myList;
        foreach (var item in myI)
        {
            Console.WriteLine(item);
        }





        }
    }
}