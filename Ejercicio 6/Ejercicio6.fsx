open System

module calculadora = 
  let suma x y = x+y
  let resta x y = x-y
  let multi x y = x*y
  let dividir x y = x/y

[<EntryPoint>]
let main argv = 
    printfn "%A" argv
  
    let sumita = calculadora.suma 5 6
    Console.WriteLine("Suma: ")
    Console.WriteLine(sumita.ToString())
    let resta = calculadora.resta 5 6
    Console.WriteLine("Resta: ")
    Console.WriteLine(sumita.ToString())
    let mutlitplicacion = calculadora.multi 5 6
    Console.WriteLine("Multiplicacion: ")
    Console.WriteLine(sumita.ToString())
    let divicion = calculadora.dividir 5 6
    Console.WriteLine("divicion: ")
    Console.WriteLine(sumita.ToString())
    let tecla = Console.ReadKey()
    0 // devolver un código de salida entero