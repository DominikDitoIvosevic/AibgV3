#region

using System.Linq;
using AibgJebach;

#endregion

namespace ApiServer.Model
{
  public class GameObject
  {
    public Board board;
    public bool finished;
    public HeroObject[] heroes;
    public string id;
    public int maxTurns;
    public int turn;

    public GameObject(string id, int turn, int maxTurns, HeroObject[] heroes, Board board, bool finished)
    {
      this.id = id;
      this.turn = turn;
      this.maxTurns = maxTurns;
      this.heroes = heroes;
      this.board = board;
      this.finished = finished;
    }

    public static GameObject GetGameObject(Bot bot1, Bot bot2, MapState mapState) => new GameObject("s2xh3aig", 1, 1200,
      new[] {HeroObject.GetHeroObject(bot1), HeroObject.GetHeroObject(bot2)},
      Board.GetBoardObject(mapState), false);
  }

  public class Board
  {
    public int size;
    public string tiles;

    public Board(int size, string tiles)
    {
      this.size = size;
      this.tiles = tiles;
    }

    public static Board GetBoardObject(MapState mapState)
    {
      return new Board(mapState.Tiles.Count,
        string.Join("",
          mapState.Tiles.Select(line => string.Join("", line.Select(TileTypes.GetTileDisplay)))));
    }
  }
}