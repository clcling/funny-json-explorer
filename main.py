import argparse
from explorer import FunnyJsonExplorer
import json
from factory import TreeStyleFactory, RectangleStyleFactory


def main():
    # 读取命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, help='Visualization style')
    parser.add_argument('-i', '--icon', help='Icon family')

    args = parser.parse_args()

    if args.icon == 'star':
        contain_icon = '♣ '
        leaf_icon = '♦ '
    else:
        contain_icon = ''
        leaf_icon = ''

    factory = None

    if args.style == 'tree':
        factory = TreeStyleFactory(contain_icon, leaf_icon)
    if args.style == 'rectangle':
        factory = RectangleStyleFactory(contain_icon, leaf_icon)

    with open(args.file, 'r') as f:
        json_data = json.load(f)

    explorer = FunnyJsonExplorer(json_data, factory)
    explorer.show()


if __name__ == "__main__":
    main()
