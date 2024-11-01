using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Введите ID клиента: ");
        string clientId = Console.ReadLine();

        Console.Write("Введите название компании: ");
        string companyName = Console.ReadLine();

        string formattedInfo = FormatClientInfo(clientId, companyName);
        Console.WriteLine($"Форматированная информация о клиенте: {formattedInfo}");
    }

    static string FormatClientInfo(string id, string name)
    {
        return $"Клиент {id}: {name}";
    }
}
