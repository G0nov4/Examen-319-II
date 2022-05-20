suma :: Int -> Int -> Int
suma x y = x + y

resta :: Int -> Int -> Int
resta x y = x - y

multiplicacion :: Int -> Int -> Int
multiplicacion x y = x * y

divicion :: Float -> Float -> Float
divicion x y = x / y


main :: IO ()
main = do 
    putStrLn "Ingrese un número X: "
    n <- getLine
    putStrLn "Ingrese un numero Y: "
    u <- getLine
    
    putStrLn "Suma:"
    putStrLn (show (suma (read n) (read u)))
    putStrLn "Resta:"
    putStrLn (show (resta (read n) (read u)))
    putStrLn "Multiplicacion:"
    putStrLn (show (multiplicacion (read n) (read u)))
    putStrLn "Divicion:"
    putStrLn (show (divicion (read n) (read u)))