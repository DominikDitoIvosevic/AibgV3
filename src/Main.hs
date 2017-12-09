{-# LANGUAGE RecordWildCards, DuplicateRecordFields #-}
module Main where

import Common
import Graphics.Gloss hiding (play)
import Graphics.Gloss.Interface.IO.Game
import Api
import Servant.API
import Servant.Client
import Network.HTTP.Client (newManager, defaultManagerSettings, Manager)
import GHC.IO.Unsafe
import Data.Maybe (fromJust)
import qualified Data.Text as Text

(training :<|> play) = client (Proxy @Api)

{-# NOINLINE man #-}
man :: Manager
man = unsafePerformIO $ newManager defaultManagerSettings

runClient :: ClientM a -> IO a
runClient cm = do
    eith <- runClientM cm (ClientEnv man (fromJust $ parseBaseUrl "http://192.168.2.104:9000"))
    case eith of
        Left err -> error (pshow err)
        Right res -> return res

tileToPicture :: Text -> Picture
tileToPicture tile = color (case tile of
    "##" -> white
    "@1" -> blue
    "@2" -> red
    "[]" -> magenta
    "$-" -> green
    "$1" -> cyan
    "$2" -> yellow
    "  " -> black
    wat -> error $ "Strange tile: " <> toS wat
    ) (rectangleSolid 10 10)

rowToPicture :: [Text] -> Picture
rowToPicture = Pictures . map (\(o, t) -> translate (o * 10) 0 (tileToPicture t)) . zip [0..]

boardToPicture :: Board -> Picture
boardToPicture Board{..} =
    Pictures $ map (\(o, r) -> translate 0 (o * 10) (rowToPicture r)) $ zip [0..] board
    where board = Text.chunksOf 2 <$> Text.chunksOf (size * 2) tiles

responseToPicture :: Response -> Picture
responseToPicture = boardToPicture . board . game

botKey :: Text
botKey = "9wydbx82"

playRandom resp = do
    i <- randomRIO (0 :: Int, 4)
    let dir = case i of
            0 -> North
            1 -> East
            2 -> South
            3 -> West
            4 -> Stay
    runClient (play a b (PlayPayload botKey dir))
    where
    (a, b) = (id (game resp :: Game), token resp)


keyToDir :: SpecialKey -> Direction
keyToDir KeyLeft = West
keyToDir KeyRight = East
keyToDir KeyUp = North
keyToDir KeyDown = South
keyToDir _ = Stay

processKey :: Event -> Response -> IO Response
processKey ev resp = case ev of
    EventKey (SpecialKey k) Up _ _ ->
        runClient (play a b (PlayPayload botKey (keyToDir k)))
    _ -> return resp
    where
    (a, b) = (id (game resp :: Game), token resp)

iterateM :: Monad m => (a -> m a) -> a -> m a
iterateM f i = iterateM f =<< f i

main :: IO ()
main = do
    res <- runClient (training (TrainingPayload botKey))
    print res
    void $ iterateM playRandom res
