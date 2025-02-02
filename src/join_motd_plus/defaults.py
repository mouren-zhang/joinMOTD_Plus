from typing import Dict, List
from mcdreforged.api.all import Serializable, ServerInterface

PLUGIN_ID = 'join_motd_plus'
psi = ServerInterface.get_instance().as_plugin_server_interface()

class Configure(Serializable):
    permission: Dict[str, int] = {
        'motd': 0,
        'reload': 3,
        'server': 0
    }
    display_list: List[str] = [
        'motd',
        'day',
        '[自定义文本] 这是一段没卵用的垃圾话。',
        '',
        'random:random.txt',
        '',
    ]
    module_settings: Dict[str, dict] = {
        'motd': {
            'text': '§e§l$player§r, 欢迎回到§b服务器§r!'
        },
        'day': {
            'plugin': 'daycount_nbt',
            'entry': 'get_day_text'
        },
        'json': {
            'preload': True
        },
        'random': {
            'prefix': '[§b随机文本§r]'
        }
    }



DefaultRandom = '''
§e§lAlex3236, yyds!
如果你看到了这句话，那么你一定看到了这句话。
记得叫服务器管理员修改随机文本哦 awa
上次看到你这么有意思的人，还是在上次。
阿坝阿巴阿巴？
你知道吗？Github 是全球最大的§m同§r异性交友网站。
这是一句废话。
'''.strip()
