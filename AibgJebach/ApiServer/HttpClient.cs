#region

using System;
using AibgJebach;

#endregion

namespace ApiServer
{
  public class HttpClient : IClient
  {
    private readonly ServerStartingInformation ssi;

    public HttpClient()
    {
      this.ssi = new ServerStartingInformation
      (
        new Position(5, 11),
        new Position(12, 6),
        new MapState(
          "##  $-        ####        $-  ##" +
          "        ##  ########  ##        " +
          "    ##$-  ############  $-##    " +
          "##            ####            ##" +
          "##$-$-##  ##        ##  ##$-$-##" +
          "  ##  @1      ####          ##  " +
          "##  ##            ##  ##    ##  " +
          "        []    []          ####  " +
          "        []    []          ##    " +
          "##  ####  ##      ##          ##" +
          "##      @2  ##  ##$-$-##  ##    " +
          "    ##  ##$-$-####            ##" +
          "##            ##    ##$-########" +
          "####  $-##            ##  ######" +
          "##  ##        ##  $-        ####" +
          "        $-  ####  $-        ####", 16),
        1300
      );
    }

    public ServerStartingInformation GetServerStartingInformation() => this.ssi;

    public BotMove GetBot1Move() => throw new NotImplementedException();

    public BotMove GetBot2Move() => throw new NotImplementedException();
  }
}