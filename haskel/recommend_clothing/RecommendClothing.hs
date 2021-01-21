recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreeFarenheight  
    | degreeCelcius > shortsleeve = "You should wear shortsleeve"  
    | degreeCelcius >= longsleeve = "You should wear longsleeve"
    | degreeCelcius >= sweater = "You should wear a sweater"
    | otherwise = "You should wear a jacket"
    where degreeCelcius = degreeFarenheight*(9/5) + 32
          shortsleeve = 80.0  
          longsleeve = 65.0
          sweater = 50.0
main = putStrLn (recommendClothing 60)