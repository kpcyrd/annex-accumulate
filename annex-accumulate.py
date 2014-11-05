#!/usr/bin/env python3
from argparse import ArgumentParser
import os

def walk(path):
	for x in os.listdir(path):
		if x[0] == '.':
			continue

		new = os.path.join(path, x)

		if os.path.isdir(new):
			for y in walk(new):
				yield y
		else:
			if os.path.exists(new):
				yield new


def mkdirp(file):
	path = '/'.join(file.split('/')[:-1])
	os.makedirs(path, exist_ok=True)


def ln(src, dest):
	os.symlink(src, dest)


def main():
	args = parser.parse_args()
	for x in args.annex:
		for absolute in walk(x):
			relative = absolute[len(x)+1:]

			mkdirp(os.path.join(args.dest, relative))

			dest = os.path.join(args.dest, relative)
			if not os.path.exists(dest):
				print('%r -> %r' % (dest, absolute))
				ln(absolute, dest)


parser = ArgumentParser()
parser.add_argument('dest')
parser.add_argument('annex', nargs='+')

if __name__ == '__main__':
	main()
