readInt :: String -> Int
readInt = read

difference :: [Int] -> Int
difference list = maximum list - minimum list

divisDiff :: [Int] -> Int
divisDiff list =
  head [ x `div` y | x <- list, y <- list, x `divisibleBy` y ]
  where a `divisibleBy` b = a `rem` b == 0 && a `div` b /= 1

main :: IO ()
main = do
  f <- readFile "input.txt" 
  let nums = map (map readInt . words) $ lines f
  print $ sum $ map difference nums
  print $ sum $ map divisDiff nums
