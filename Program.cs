using System;
using System.IO;

using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;

namespace csharp_hello_world
{
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var host = new WebHostBuilder()
                .UseKestrel()
                .UseContentRoot(Directory.GetCurrentDirectory())
                //.UseIISIntegration() // Only on windows server
                .UseStartup<Startup>()
                //.UseApplicationInsights()
                .Build();

            host.Run();

        }
    }

    public class Startup {
      public void Configure() {
        
      }
    }
}
