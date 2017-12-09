{-# LANGUAGE RecordWildCards, ScopedTypeVariables, DuplicateRecordFields #-}
module Grid where

import Common
import qualified Data.Map.Strict as Map
import qualified Data.Set as Set
import Api
import qualified Data.Text as Text

data Tile = Empty | Wall | Me | Enemy | NeutralMine | AllyMine | EnemyMine | Heal

data Grid = Grid
    { size :: Int
    , tileMap :: Map (Int, Int) Tile }

readTile :: Int -> Text -> Tile
readTile n t = case t of
    "##" -> Wall
    "@1" -> if n == 1 then Me else Enemy
    "@2" -> if n == 2 then Me else Enemy
    "[]" -> Heal
    "$-" -> NeutralMine
    "$1" -> if n == 1 then AllyMine else EnemyMine
    "$2" -> if n == 2 then AllyMine else EnemyMine
    "  " -> Empty
    wat -> error $ "Strange tile: " <> toS wat

boardToMap :: Int -> Board -> Map (Int, Int) Tile
boardToMap n Board{..} = Map.fromList $ concat $
    zipWith (\y l -> map (\(x, a) -> ((x, y), a)) l) [0..] board
    where
    board :: [[(Int, Tile)]]
    board =
        zip [0..] . map (readTile n) . Text.chunksOf 2 <$> Text.chunksOf (size * 2) tiles

boardToGrid :: Int -> Board -> Grid
boardToGrid n board = Grid (size (board :: Board)) (boardToMap n board)

data GameState = GameState
    { myCoords :: Coords
    , enemyCoords :: Coords
    , myHp :: Int
    , enemyHp :: Int
    , grid :: Grid }

updateState :: Int -> GameState -> Response -> GameState
updateState n _ Response{..} =
    GameState (pos hero) (pos enm) (life hero) (life enm) (boardToGrid n (board game))
    where
    [enm] = filter (\h -> id (h :: Hero) /= n) $ heroes game

neighbors :: (Int, Int) -> [(Direction, (Int, Int))]
neighbors (x, y) =
    [ (North, (x, y + 1))
    , (East, (x + 1, y))
    , (South, (x, y - 1))
    , (West, (x - 1, y))
    ]

findPath :: (Tile -> Bool) -> (Int, Int) -> Map (Int, Int) Tile -> [Direction]
findPath cond start mp = go Set.empty (Set.singleton ([], start))
    where
    go visited frontier = case Set.minView (Set.filter (cond . snd) frontier) of
        Nothing ->
            let newVis = visited `Set.union` (Set.map snd frontier)
                newFront = flip map (Set.toList frontier) $ \(path, coord) ->
                    flip mapMaybe (neighbors coord) $ \(dir, newCoord') ->
                        case Map.lookup newCoord' mp of



moveToFirstMine :: (Int, Int) -> Grid -> Direction
moveToFirstMine

move :: GameState -> Direction
move GameState{..} =
    if myHp > 40 then moveToFirstMine myCoords grid
    else moveToFirstHeal myCoords grid
