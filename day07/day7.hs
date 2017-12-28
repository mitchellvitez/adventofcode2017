import Data.Attoparsec.Text
import qualified Data.Text.IO as T

data Tower = Tower String Int [String]
instance Show Tower where
  show (Tower name weight xs) = name ++ " (" ++ show weight ++ ") " ++ show xs

parseName :: Parser String
parseName = do
  name <- count 4 anyChar
  char ','
  space
  return name

towerList :: Parser [String]
towerList = do
  space
  char '-'
  char '>'
  space
  names <- many1' parseName
  lastName <- count 4 anyChar
  return $ names ++ [lastName]

parseTower :: Parser Tower
parseTower = do
  name <- count 4 anyChar
  space
  char '('
  weight <- many1' digit
  char ')'
  tl <- option [] towerList
  endOfLine
  return $ Tower name (read weight) tl

parseTowers :: Parser [Tower]
parseTowers = many' parseTower

getDepth :: [Tower] -> Tower -> Int
getDepth _ (Tower _ _ []) = 0
getDepth towers (Tower _ _ sub) =
  1 + maximum $ map (getDepth towers) sub

subMain :: [Tower] -> [Int]
subMain towers =
  map (getDepth towers) towers

main = do
  f <- T.readFile "testinput.txt"
  case parseOnly parseTowers f of
    Left err -> putStrLn "failed to parse"
    Right rs -> print $ subMain rs

