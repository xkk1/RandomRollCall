"""用于获取文件编码"""
# win10:ANSI、UTF-16 LE、UTF-16 BE、UTF-8、带有 BOM 的 UTF-8
# win7:ANSI、Unicode、 Unicode big endian、UTF-8
# 说明：UTF兼容ISO8859-1和ASCII,GB18030兼容GBK,GBK兼容GB2312,GB2312兼容ASCIl
CODES = ['UTF-8', "GB18030", "BIG5", "UTF-16"]
# UTF-8 BOM前缀字节
UTF_8_BOM = b"\xef\xbb\xbf"


def string_coding(b: bytes):
    """
    获取字符编码类型
    """
    for code in CODES:
        try:
            b.decode(encoding=code)
            if "UTF-8" == code and b.startswith(UTF_8_BOM):
                return "UTF-8-SIG"
            else:
                return code
        except Exception:
            continue
    return "未知字符编码类型"

def file_coding(file_path):
    """
    获取文件编码类型
    """
    coding = "UTF-8"
    with open(file_path, "rb") as f:
        coding = string_coding(f.read())
    # print(f"文件“{file_path}”编码“{coding}”")
    return coding

def main():
    print(file_coding("a.txt"))
    with open("a.txt", "r", encoding=file_coding("a.txt")) as f:
        print(f.read())
    input()


if __name__ == "__main__":
    main()
