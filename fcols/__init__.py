#!/usr/bin/python3
import sys
from operator import add

def read_lines():
	lines = []
	while True:
		try:
			lines.append(input())
		except EOFError:
			break
	return lines

def get_all_column_data(lines, separators):
	result = []
	for line in lines:
		last = 0
		columns = []
		for sep in separators:
			pos = line.find(sep, last)
			if pos < 0:
				columns.append(-1)
			else:
				columns.append(pos - last)
				last = pos + len(sep)
		result.append(columns)
	return result

def format_columns(all_columns, separators):
	missed = [{} for x in range(len(all_columns))]
	for i in range(len(separators)):
		max_pos = 0
		for columns, m in zip(all_columns, missed):
			if columns[i] < 0:
				m[i] = 0
			if columns[i] > max_pos:
				if not m:
					max_pos = columns[i]

		for columns, m in zip(all_columns, missed):
			if not m:
				columns[i] = max_pos
	return missed, all_columns

def formatted_lines(lines, missed, all_columns):
	for line, m, columns in zip(lines, missed, all_columns):
		if m:
			yield line
			continue
		last = 0
		result = ''
		for sep, col in zip(separators, columns):
			pos = line.find(sep, last)
			if pos > -1:
				result += line[last:pos].ljust(col) + sep
				last = pos + len(sep)
		result += line[last:]
		yield result

def main():
	separators = sys.argv[1:]
	lines = read_lines()
	all_columns = get_all_column_data(lines, separators)
	missed, all_columns = format_columns(all_columns, separators)
	for line in formatted_lines(lines, missed, all_columns):
		print(line)

if __name__ == '__main__':
	main()
