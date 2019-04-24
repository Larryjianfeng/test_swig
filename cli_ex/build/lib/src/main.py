import jieba
import argparse


def cut(line: str):
    return ' '.join(jieba.cut(line))


def cat(line):
    return ''.join(line.split())


def args():
    parser = argparse.ArgumentParser(description='parsing args')

    parser.add_argument('--mode', default='cut')
    parser.add_argument('--line', default='hello  world')

    return parser.parse_args()
