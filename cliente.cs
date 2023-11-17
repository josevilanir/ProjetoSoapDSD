using System;

namespace SoapClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var client = new MediaServiceReference.MediaServiceClient();
            
            // Substitua os números abaixo pelos valores desejados
            int[] numeros = { 10, 20, 30, 40, 50 };

            var resultado = client.calcular_media(numeros);

            Console.WriteLine(resultado);
        }
    }
}

