# takes as input a number and returns a collection of associated pegs

import sys
import json
import pathlib

def main():
	# Determine the directory where this script is located
	script_dir = pathlib.Path(__file__).parent.resolve()
	json_path = script_dir / "wiki_major_mapping.json"

	# Check if a word was provided via command line
	if len(sys.argv) < 2:
		print("Usage: major_peg <number>")
		sys.exit(1)
	else:
		num_str = sys.argv[1]

	with open(json_path) as f:
		d = json.load(f)

	length = len(num_str)
	if length%2 == 0:
		n_pegs = length//2
		for i in range(n_pegs):
			peg_2 = num_str[2*i] + num_str[2*i+1]
			print(f'\'{peg_2}\': {d[peg_2]},')
	else:
		n_pegs = 1 + length//2
		for i in range(n_pegs-1):
			peg_2 = num_str[2*i] + num_str[2*i+1]
			print(f'\'{peg_2}\': {d[peg_2]},')
		print(f'\'{num_str[-1]}\' : {d[num_str[-1]]}')

if __name__ == "__main__":
	main()
	

