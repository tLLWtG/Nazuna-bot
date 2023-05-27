from nonebot import on_command, CommandSession
import requests
import json

@on_command('hitokoto', aliases=('一言', 'Hitokoto'), only_to_me=False)
async def hitokoto(session: CommandSession):
    hitokoto_arg = session.current_arg_text.strip()
    res = await get_hitokoto()
    await session.send(res[0])
    if hitokoto_arg != '-h' and len(res) == 2:
        await session.send(f'from: {res[1]}')
    
    
async def get_hitokoto() -> list[str]:
    try:
        res_text = requests.get('https://v1.hitokoto.cn/?c=a&c=b&c=d&c=i&c=k').text
    except:
        return ['与 Hitokoto 服务器通信异常 QAQ']
    
    try:
        res_dict = json.loads(res_text)
    except:
        return ['无法解析接收到的 Hitokoto 信息 QAQ']
    
    hitokoto_text = res_dict['hitokoto']
    hitokoto_from = res_dict['from']

    return [hitokoto_text, hitokoto_from]