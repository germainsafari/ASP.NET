// using get set
public class Greetings{
    public string value{get; set;}
}
Greetings initGreetings = new Greetings()
initGreetings.value = "hello world"
Console.WriteLine(initGreetings.value)