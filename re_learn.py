import re


def main():
    # 正则表达式中的pattern：r作用是消除转义字符在字符串中的特殊含义，^ 和 $ 的作用是规定这是一个完全匹配的字符串，而非某一子串
    pattern = re.compile(r"^((25[0-5]|2[0-4]\d|1\d{2}|\d{2}|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|\d{2}|\d)$")
    pattern2 = re.compile(r"[,\s](?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
                          r"(?:25[0-5]|2[0-4]\d|1\d{2}|\d{2}|\d)[^.\d]")

    test_ip = [
        "192.168.1.1",  # Valid
        "255.255.255.255",  # Valid
        "0.0.0.0",  # Valid
        "256.256.256.256",  # Invalid
        "123.456.78.90",  # Invalid
        "192.168.1.",  # Invalid
        "192.168.1.256",  # Invalid
        "192.168.1.1.1"  # Invalid
    ]

    string_ip = """
    192.168.1.1,  # Valid
    255.255.255.255,  # Valid
    0.0.0.0,  # Valid
    256.256.256.256,  # Invalid
    123.456.78.90,  # Invalid
    192.168.1.,  # Invalid
    192.168.1.256,  # Invalid
    192.168.1.1.1  # Invalid
    """  # 其中的192.168.1.1.1的子串就不会被识别

    string_dirty_talk = "你丫是叉吗? 我操你大爷的. Fuck you."
    dirty_pattern = r"[傻莎沙啥杀煞][比币必笔臂逼毕碧壁叉]?|[操肏]|cao|fuck|shit"
    recreate_dirty_talk = re.sub(dirty_pattern, '*', string_dirty_talk, flags=re.IGNORECASE)
    valid_ip_list = []
    # findall返回的默认是捕获的组，如果想要其返回匹配的内容，需要使用非捕获组?:
    valid_ip_list2 = re.findall(pattern2, string_ip)

    for temp in test_ip:
        if re.match(pattern, temp):
            valid_ip_list.append(temp)

    print("Valid IPs from test_ip list:")
    print(valid_ip_list)
    print()

    print("Valid IPs from string_ip string using findall:")
    for ip_tuple in valid_ip_list2:
        print(ip_tuple)

    print()
    print("Valid IPs from string_ip string using finditer:")
    for it_temp in pattern2.finditer(string_ip):
        print(it_temp.group())

    print()
    print(recreate_dirty_talk)


if __name__ == "__main__":
    main()
