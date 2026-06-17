"""
密码生成器
练习点：random / secrets、string 模块、argparse、函数组合
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
    pool = string.ascii_lowercase
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

    # TODO: 用 secrets.choice(pool) 补足剩余长度
    # TODO: 将 required + 剩余字符合并，随机打乱顺序后拼接成字符串
    raise NotImplementedError


def check_strength(password: str) -> str:
    """评估密码强度，返回 '弱' / '中' / '强'。"""
    # TODO: 根据长度和字符种类数量判断强度
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="随机密码生成器")
    parser.add_argument("-l", "--length", type=int, default=16, help="密码长度")
    parser.add_argument("-n", "--count", type=int, default=1, help="生成数量")
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
