
score = {
	'X': 1,
	'Y': 2,
	'Z': 3,
}

outcome = {
	'X': 0,
	'Y': 3,
	'Z': 6,
}

def map_to_my_symbol(opponent):
	if opponent == 'A':
		return 'X'
	elif opponent == 'B':
		return 'Y'
	else:
		return 'Z'

def score_game(opponent_score, me_score):
	p1 = opponent_score - 1
	p2 = me_score - 1
	if (p1 + 1) % 3 == p2:
		return 6
	elif (opponent_score == me_score):
		return 3
	else: 
		return 0

def game_outcome(me, opponent_score):
	p1 = opponent_score - 1
	if me == 'X':
		if p1 - 1 < 0:
			return p1 - 1 + 3 + 1
		else:
			return p1
	if me == 'Y':
		return p1 + 1
	else:
		if p1 + 1 > 2:
			return 1
		else:
			return p1 + 2


with open('input.txt', 'r') as f:
	total_score_1 = 0
	total_score_2 = 0
	lines = f.readlines()
	for line in lines:
		print(line)
		[opponent, me] = line.split()
		me_score, opponent_score = score[me], score[map_to_my_symbol(opponent)]
		
		total_score_1 += me_score 
		total_score_1 += score_game(opponent_score, me_score)

		total_score_2 += outcome[me]
		total_score_2 += game_outcome(me, opponent_score)
	print(total_score1, total_score_2)




