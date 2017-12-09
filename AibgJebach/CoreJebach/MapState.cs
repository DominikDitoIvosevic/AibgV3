#region

using System;
using System.Collections.Generic;
using System.Linq;

#endregion

namespace AibgJebach
{
  public class MapState
  {
    public MapState(List<List<TileType>> tiles)
    {
      this.Tiles = tiles;
    }

    public MapState(string tiles, int dimension)
    {
      List<string> stringTiles = new List<string>();
      while (!string.IsNullOrEmpty(tiles))
      {
        stringTiles.Add(tiles.Substring(0, dimension * 2));
        tiles = tiles.Substring(dimension * 2);
      }

      this.Tiles = stringTiles.Select(s =>
      {
        List<TileType> line = new List<TileType>();
        while (!string.IsNullOrEmpty(s))
        {
          line.Add(TileTypes.GetTileType(s.Substring(0, 2)));
          s = s.Substring(2);
        }
        return line;
      }).ToList();
    }

    public List<List<TileType>> Tiles { get; }

    public TileType GetTile(Position currentPosition) => this.Tiles[currentPosition.posX][currentPosition.posY];

    public void AcquireMine(Bot bot)
    {
      TileType newTileType = bot.IsBotNumberOne ? TileType.MinePlayer1 : TileType.MinePlayer2;

      if (this.Tiles[bot.Position.posX][bot.Position.posY] == newTileType)
      {
        throw new InvalidOperationException("Already acquired");
      }

      this.Tiles[bot.Position.posX][bot.Position.posY] = newTileType;
    }
  }
}