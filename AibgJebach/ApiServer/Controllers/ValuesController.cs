#region

using AibgJebach;
using ApiServer.Model;
using Microsoft.AspNetCore.Mvc;

#endregion

namespace ApiServer.Controllers
{
  [Route("api/training")]
  public class ValuesController : Controller
  {
    public static HttpClient httpClient = new HttpClient();
    public static BotServer botServer = new BotServer(httpClient);

    // GET api/values
    [HttpGet]
    public ResponseObject Get()
    {
      return ResponseObject.GetResponseObject(botServer.Bot1, botServer.Bot2, botServer.MapState);
    }
  }
}