namespace AibgJebach
{
  public interface IClient
  {
    ServerStartingInformation GetServerStartingInformation();
    BotMove GetBot1Move();
    BotMove GetBot2Move();
  }
}