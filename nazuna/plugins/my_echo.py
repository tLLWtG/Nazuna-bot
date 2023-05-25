from nonebot import on_command, CommandSession
from nonebot.message import unescape

@on_command('echo', only_to_me=False)
async def echo(session: CommandSession):
    await session.send(session.state.get('message') or session.current_arg)
@on_command('say', only_to_me=False, permission=lambda s: s.is_superuser)
async def say(session: CommandSession):
    await session.send(
        unescape(session.state.get('message') or session.current_arg))

