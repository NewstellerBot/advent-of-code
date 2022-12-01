import numpy as np

def find_top_elfs(elfs, n=3):
	if n > 0:
		top_elf = 0
		ti = 0
		for i, elf in enumerate(elfs):
			s = sum(elf)
			if s > top_elf:
				top_elf = s
				ti = i
		elfs.remove(elfs[ti])
		return top_elf + find_top_elfs(elfs, n - 1)
	else:
		return 0

with open('input.txt', 'r') as f:
	lines = f.readlines()
	elfs = ''.join(lines).split('\n\n')
	elfs = [elf.split('\n') for elf in elfs]
	elfs = [list(map(lambda x: 0 if x == '' else int(x), elf)) for elf in elfs]

	print(find_top_elfs(elfs, 3))

		

		
