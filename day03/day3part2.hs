import Control.Monad.Loops
import Control.Monad
import qualified Data.Vector as V

sumNeighbors :: Int -> Int -> V.Vector (V.Vector Int) -> Int
sumNeighbors x y grid =
  sum [grid V.! a V.! b | a <- [x-1..x+1], b <- [y-1..y+1]]

update :: V.Vector (V.Vector Int) -> Int -> Int -> V.Vector (V.Vector Int)
update grid x y =
  let s = sumNeighbors (basex+x) (basey+y) grid
  in setCell grid (basex+x) (basey+y) s
  
setCell :: V.Vector (V.Vector Int) -> Int -> Int -> Int -> V.Vector (V.Vector Int)
setCell grid x y new =
  grid V.// [(x, (grid V.! x) V.// [(y, new)] )]

display :: V.Vector (V.Vector Int) -> IO ()
display grid = do 
  V.mapM_ print grid
  putStrLn ""

basex = 50
basey = 50

main :: IO ()
main = do
  let emptyGrid = V.replicate 100 (V.replicate 100 0)
      grid = setCell emptyGrid basex basey 1
      finalGrid = Main.iterate nextGrid grid 1 0 1 !! 100
  print . minimum . Prelude.filter (>361527) 
        . V.toList . V.concat . V.toList $ finalGrid

iterate f grid x y emu = 
  grid : Main.iterate f (f grid x y emu) x y emu

nextGrid grid x y emu
  | grid V.! (basex+x) V.! (basey+y) == 0 = update grid x y
  | y == -emu && x == emu = nextGrid grid (x+1) y (emu+1)
  | x == emu  && y < emu = nextGrid grid x (y+1) emu
  | y == emu  && x > -emu = nextGrid grid (x-1) y emu
  | x == -emu && y > -emu = nextGrid grid x (y-1) emu
  | y == -emu && x < emu = nextGrid grid (x+1) y emu

