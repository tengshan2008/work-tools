import argparse


def path_parser():
    parser = argparse.ArgumentParser(description='基本参数命令行解析')

    parser.add_argument('-i', '--input', type=str,
                        help='输入文件名称', required=True)
    parser.add_argument('-o', '--output', type=str,
                        help='输出文件名称', required=True)
    parser.add_argument('-r', '--root', type=str, help='词根文件名称', required=True)

    args = parser.parse_args()

    print(args.input, args.output, args.root)


if __name__ == '__main__':
    path_parser()
