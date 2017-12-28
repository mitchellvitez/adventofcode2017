import Data.List (transpose)
import Control.Monad
 
spiral :: Int -> Int -> Int -> [[Int]]
spiral rows cols start
  | rows > 0 = [start .. start + cols - 1] :
               (reverse <$> transpose (spiral cols (rows - 1) (start + cols)))
  | otherwise = [[]]

spiral' :: Int -> [[Int]]
spiral' size = map (map (\x -> size^2 - x + 1)) $ spiral size size 1

enumerate = zip [0..]

find num grid = do
  (y, row) <- enumerate grid
  (x, cell) <- enumerate row
  guard $ cell == num
  return (x, y)

manhattanDistance (a,b) (c,d) =
  (max a c - min a c) + (max b d - min b d)
 
main :: IO ()
main = do
  let s = spiral' 602
  print "Built spiral"
  print $ manhattanDistance (head (find 1 s)) (head (find 361527 s))
