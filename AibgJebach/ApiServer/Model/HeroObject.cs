#region

using AibgJebach;

#endregion

namespace ApiServer.Model
{
  public class HeroObject
  {
    public bool crashed;
    public int gold;
    public int id;
    public string lastDir;
    public int life;
    public int mineCount;
    public string name;
    public Pos pos;
    public Pos spawnPos;
    public string userId;

    public HeroObject(int id, string name, string userId, Pos pos, string lastDir, int life, int gold, int mineCount,
      Pos spawnPos, bool crashed)
    {
      this.id = id;
      this.name = name;
      this.userId = userId;
      this.pos = pos;
      this.lastDir = lastDir;
      this.life = life;
      this.gold = gold;
      this.mineCount = mineCount;
      this.spawnPos = spawnPos;
      this.crashed = crashed;
    }

    public static HeroObject GetHeroObject(Bot bot1) => new HeroObject(
      bot1.IsBotNumberOne ? 1 : 0,
      "qewqe",
      "dsfdsfks",
      new Pos(bot1.Position.posX, bot1.Position.posY),
      "asrasadas",
      bot1.Health,
      bot1.Coins,
      bot1.OwnedMines.Count,
      new Pos(bot1.StartingPosition.posX, bot1.StartingPosition.posY),
      false);
  }

  public class Pos
  {
    public int x;
    public int y;

    public Pos(int x, int y)
    {
      this.x = x;
      this.y = y;
    }
  }
}