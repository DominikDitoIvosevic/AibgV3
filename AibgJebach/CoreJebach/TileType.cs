#region

using System.Linq;

#endregion

namespace AibgJebach
{
  public static class TileTypes
  {
    public static string EmptyTile = "  ";
    public static string Hero1 = "@1";
    public static string Hero2 = "@2";
    public static string Obstacle = "##";
    public static string MinePlayer1 = "$1";
    public static string MinePlayer2 = "$2";
    public static string MineNeutral = "$-";
    public static string CoffeeMachine = "[]";

    private static readonly string[] tileTypesMap =
    {
      EmptyTile,
      Hero1,
      Hero2,
      Obstacle,
      MinePlayer1,
      MinePlayer2,
      MineNeutral,
      CoffeeMachine
    };

    private static readonly TileType[] tileTypeMaps =
    {
      TileType.EmptyTile,
      TileType.Hero1,
      TileType.Hero2,
      TileType.Obstacle,
      TileType.MinePlayer1,
      TileType.MinePlayer2,
      TileType.MineNeutral,
      TileType.CoffeeMachine
    };

    public static string GetTileDisplay(TileType tileType) => tileTypesMap[(int) tileType];

    public static TileType GetTileType(string tileTypeString) =>
      tileTypeMaps[tileTypesMap.ToList().IndexOf(tileTypeString)];
  }

  public enum TileType
  {
    EmptyTile,
    Hero1,
    Hero2,
    Obstacle,
    MinePlayer1,
    MinePlayer2,
    MineNeutral,
    CoffeeMachine
  }
}