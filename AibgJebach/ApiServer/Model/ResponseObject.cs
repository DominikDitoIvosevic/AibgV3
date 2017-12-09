#region

using AibgJebach;

#endregion

namespace ApiServer.Model
{
  public class ResponseObject
  {
    public GameObject game;
    public HeroObject hero;
    public string playUrl;
    public string token;
    public string viewUrl;

    public ResponseObject(GameObject game, HeroObject hero, string token, string viewUrl, string playUrl)
    {
      this.game = game;
      this.hero = hero;
      this.token = token;
      this.viewUrl = viewUrl;
      this.playUrl = playUrl;
    }

    public static ResponseObject GetResponseObject(Bot bot1, Bot bot2, MapState mapState) => new ResponseObject(
      GameObject.GetGameObject(bot1, bot2, mapState),
      HeroObject.GetHeroObject(bot1),
      "lte0",
      "http://localhost:9000/s2xh3aig",
      "http://localhost:9000/api/s2xh3aig/lte0/play"
    );
  }
}