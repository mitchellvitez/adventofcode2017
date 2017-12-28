import Data.List 

noDuplicates :: Eq a => [a] -> Bool
noDuplicates xs = xs == nub xs

result transform =
  print . length . filter noDuplicates . transform . map words . lines

-- main = do
--   input <- readFile "input.txt"
--   result id input
--   result (map (map sort)) input

main = print . length . filter (\xs -> xs == nub xs) . map (map sort) . map words . lines =<< readFile "input.txt"
