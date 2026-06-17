"""
密码生成器
练习点：random / secrets、string 模块、argparse、函数组合

使用示例 / 测试命令：
    # 查看命令行参数说明
    python main.py --help

    # 生成 1 个长度为 16 的随机密码
    python main.py

    # 生成 3 个长度为 20 的随机密码
    python main.py -l 20 -n 3

    # 生成不包含大写字母的密码
    python main.py -l 12 --no-upper

    # 生成不包含数字和特殊字符的密码
    python main.py -l 10 --no-digits --no-symbols

说明：
    当前文件仍保留练习用 TODO。
    除了 `python main.py --help` 之外，其余命令需要先完成 TODO 才能正常运行。
"""
import argparse
import secrets
import string


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """生成一个随机密码。

    至少包含每种字符类型各一个（如果该类型被启用）。
    """
    # 先把小写字母作为默认字符池。
    pool = string.ascii_lowercase

    # required 用来保存“必须出现”的字符，确保最终密码至少覆盖启用的字符类型。
    required = [secrets.choice(string.ascii_lowercase)]

    if use_upper:
        pool += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        pool += string.digits
        required.append(secrets.choice(string.digits))
    if use_symbols:
        pool += string.punctuation
        required.append(secrets.choice(string.punctuation))

    if length < len(required):
        raise ValueError(f"密码长度至少需要 {len(required)} 位")

    # 剩余位数 = 总长度 - 已经保证放入的字符数。
    while len(required) < length:
        required.append(secrets.choice(pool))

    # 为了避免“前几位总是固定类型字符”，需要把结果随机打乱。
    rng = secrets.SystemRandom()
    rng.shuffle(required)
    rng.shuffle(required)
    return ''.join(required)


def check_strength(password: str) -> str:
    """评估密码强度，返回 '弱' / '中' / '强'。"""
    # 可以从两个维度判断：
    # 1. 密码长度是否足够长
    # 2. 包含了多少种字符类型（小写、大写、数字、特殊字符）

    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    type_count = sum([has_digit,has_symbols,has_upper,has_lower])
    length = len(password)
    
    if length < 8 or type_count <= 1:
        return "弱"
    if length >= 12 and type_count >= 3:
        return "强"
    return "中"


def main():
    parser = argparse.ArgumentParser(description="随机密码生成器")
    # -l / --length: 控制每个密码的长度
    parser.add_argument("-l", "--length", type=int, default=16, help="密码长度")
    # -n / --count: 一次生成多少个密码
    parser.add_argument("-n", "--count", type=int, default=1, help="生成数量")
    # 下面几个参数是“关闭某类字符”的开关。
    parser.add_argument("--no-upper", action="store_true", help="不含大写字母")
    parser.add_argument("--no-digits", action="store_true", help="不含数字")
    parser.add_argument("--no-symbols", action="store_true", help="不含特殊字符")
    args = parser.parse_args()

    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        strength = check_strength(pwd)
        print(f"{pwd}  [{strength}]")


if __name__ == "__main__":
    main()
