using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AibgJebach
{
  public static class TileTypes
  {
    public static string Hero1 = "@1";
    public static string Hero2 = "@2";
    public static string Obstacle = "##";
    public static string MinePlayer1 = "$1";
    public static string MinePlayer2 = "$2";
    public static string MineNeutral = "$-";
    public static string CoffeeMachine = "[]";

    private static string[] tileTypesMap =
    {
      Hero1,
      Hero2,
      Obstacle,
      MinePlayer1,
      MinePlayer2,
      MineNeutral,
      CoffeeMachine
    };

    public static string GetTileDisplay(TileType tileType)
    {
      return tileTypesMap[(int) tileType];
    }
  }

  public enum TileType
  {
    Hero1,
    Hero2,
    Obstacle,
    MinePlayer1,
    MinePlayer2,
    MineNeutral,
    CoffeeMachine
  }
}
