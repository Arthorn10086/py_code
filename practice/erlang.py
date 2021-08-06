import sys, struct
import json


def twice(args):
    return 2 * args[0]


def sum(args):
    return args[0] + args[1]


def tof(Msg):
    with open('e:/a.txt', 'a+') as f:
        f.write(str(Msg))
        f.write("\n")
        f.close()
    return 'ok'

def nf():
    return 'undefined function'

# 实现一个路由表，将索引和功能函数的对应关系存到这个字典中
router_dict = {1: twice, 2: sum, 3: tof}


def route_apply(l):
    index = l[0]
    func = router_dict.get(index,nf)
    return func(l[1:])


def main_loop():
    while True:
        # 2个字节的包头
        buf = sys.stdin.read(2)
        # 获取消息长度
        (sz,) = struct.unpack("!H", buf.encode())
        # 获取消息数据
        buf1 = sys.stdin.read(sz)
        # json
        xa = json.loads(buf1)
        # 路由
        res = route_apply(xa)
        # json压缩
        result = json.dumps(res)
        # 封装包头
        hearder = struct.pack("!H", len(result))
        # 返回给erlang port
        sys.stdout.write(hearder.decode() + result)


if __name__ == '__main__':
    main_loop()
