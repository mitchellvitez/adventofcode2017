import Data.Vector.Unboxed (Vector, (!), (//), fromList, length)

runProgram :: Vector Int -> Int -> Int -> Int -> Int
runProgram program pc numSteps programLength
  | pc < 0 || pc >= programLength = numSteps
  | otherwise = 
      let instr = program ! pc
      in runProgram 
           (program // [(pc, instr + 1)]) -- if instr >= 3 then instr-1 else instr+1)])
           (pc + instr)
           (numSteps + 1)
           programLength

main = do
  f <- readFile "input.txt"
  let program = fromList $ map read $ lines f
  print $ runProgram program 0 0 (Data.Vector.Unboxed.length program)
  
