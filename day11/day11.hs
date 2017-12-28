import Data.List.Split
import Data.List

count' :: Int -> Int -> Int -> Int -> [String] -> IO ()
count' x y z m [] = do
  print $ maximum [abs x, abs y, abs z]
  print m
count' x y z m' (i:is) = do
  let m = maximum [abs x, abs y, abs z, m']
  case i of
    "n" -> count' (x-1) (y+1) z m is
    "s" -> count' (x+1) (y-1) z m is
    "nw" -> count' (x-1) y (z+1) m is
    "se" -> count' (x+1) y (z-1) m is
    "ne" -> count' x (y+1) (z-1) m is
    "sw" -> count' x (y-1) (z+1) m is
    _ -> error "bad instruction"

-- count' x y z m [] =
  -- (maximum [abs x, abs y, abs z], m)
-- count' x y z m' (i:is) =
  -- let m = maximum [abs x, abs y, abs z, m']
  -- in
  -- case i of
    -- "n" -> count' (x-1) (y+1) z m is
    -- "s" -> count' (x+1) (y-1) z m is
    -- "nw" -> count' (x-1) y (z+1) m is
    -- "se" -> count' (x+1) y (z-1) m is
    -- "ne" -> count' x (y+1) (z-1) m is
    -- "sw" -> count' x (y-1) (z+1) m is
    -- _ -> error "bad instruction"

count = count' 0 0 0 0

main = do
  f <- readFile "input.txt"
  let instructions = splitOn "," $ reverse . dropWhile (=='\n') . reverse $ f
  count instructions
