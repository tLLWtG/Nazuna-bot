from nonebot import on_command, CommandSession
import requests
import json
import time

@on_command('recent_contest', aliases=('contest', '查询比赛'), only_to_me=False)
async def recent_contest(session: CommandSession):
    contest = await get_contest()
    await session.send(contest)
    
async def get_contest() -> str:
    res_text = requests.get('https://codeforces.com/api/contest.list?gym=false').text
    # res_text = '{"status":"OK","result":[{"id":1835,"name":"Codeforces Round (Div. 1)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1687098900,"relativeTimeSeconds":-2081273},{"id":1836,"name":"Codeforces Round (Div. 2)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1687098900,"relativeTimeSeconds":-2081273},{"id":1834,"name":"Codeforces Round (Div. 2)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1687075500,"relativeTimeSeconds":-2057873},{"id":1838,"name":"Codeforces Round 876 (Div. 2)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1685284500,"relativeTimeSeconds":-266873},{"id":1830,"name":"Codeforces Round 875 (Div. 1)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":9000,"startTimeSeconds":1685198100,"relativeTimeSeconds":-180473},{"id":1831,"name":"Codeforces Round 875 (Div. 2)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":9000,"startTimeSeconds":1685198100,"relativeTimeSeconds":-180473},{"id":1837,"name":"Educational Codeforces Round 149 (Rated for Div. 2)","type":"ICPC","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1685025300,"relativeTimeSeconds":-7675},{"id":1833,"name":"Codeforces Round 874 (Div. 3)","type":"ICPC","phase":"FINISHED","frozen":false,"durationSeconds":8100,"startTimeSeconds":1684506900,"relativeTimeSeconds":510727},{"id":1827,"name":"Codeforces Round 873 (Div. 1)","type":"CF","phase":"FINISHED","frozen":false,"durationSeconds":7200,"startTimeSeconds":1684074900,"relativeTimeSeconds":942726},{"id":1828,"name":"Codeforces Round 873 (Div. 2)","type":"CF","phase":"FINISHED","frozen":false,"durationSeconds":7200,"startTimeSeconds":1684074900,"relativeTimeSeconds":942727},{"id":1832,"name":"Educational Codeforces Round 148 (Rated for Div. 2)","type":"ICPC","phase":"FINISHED","frozen":false,"durationSeconds":7200,"startTimeSeconds":1683902100,"relativeTimeSeconds":1115527},{"id":1824,"name":"Codeforces Round 872 (Div. 1)","type":"CF","phase":"FINISHED","frozen":false,"durationSeconds":7200,"startTimeSeconds":1683547500,"relativeTimeSeconds":1470126},{"id":1825,"name":"Codeforces Round 872 (Div. 2)","type":"CF","phase":"FINISHED","frozen":false,"durationSeconds":7200,"startTimeSeconds":1683547500,"relativeTimeSeconds":1470127},{"id":1829,"name":"Codeforces Round 871 (Div. 4)","type":"ICPC","phase":"FINISHED","frozen":false,"durationSeconds":8100,"startTimeSeconds":1683383700,"relativeTimeSeconds":1633927}]}'
    # {"id":1835,"name":"Codeforces Round (Div. 1)","type":"CF","phase":"BEFORE","frozen":false,"durationSeconds":7200,"startTimeSeconds":1687098900,"relativeTimeSeconds":-2081273}
    res_dict = json.loads(res_text)
    contest_BEFORE = []

    for contest in res_dict['result']:
        if contest['phase'] == 'BEFORE':
            contest_BEFORE.append(contest)
        else:
            break

    res_contest_info = "查询到最近的比赛：\n\n"

    for contest in contest_BEFORE[::-1]:
        contest_time = int(contest['startTimeSeconds'])
        time_array = time.localtime(contest_time)
        other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        res_contest_info += f'比赛: {contest["name"]}#{contest["id"]}\n时间: {other_style_time}\n时长: {int(contest["durationSeconds"]/60)}min\n\n'
    res_contest_info = res_contest_info[:-2]
    
    return res_contest_info