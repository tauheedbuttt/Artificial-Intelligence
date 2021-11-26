import random


def reflex_vaccum_agent(state):
	if state['status'] == 'dirty':
		return 'suck'
	elif state['location']=='A':
		return 'right'
	elif state['location']=='B':
		return 'left'
	else:
		return '-1'


def take_action(state, action):
	if action=='suck':
		if state['status']=='dirty':
			state['status'] = 'clean'
	if action=='right':
		if state['location']=='A':
			state['location'] = 'B'
	if action=='left':
		if state['location']=='B':
			state['location'] = 'A'


choice = 'y'
while(choice != 'n'):
	state = {
		'status': random.choice(['clean', 'dirty']),
		'location': random.choice(['A', 'B'])
	}

	curr_state = "\n".join([f'{a}: {b}' for a,b in state.items()])
	print(f'--------Before--------\n {curr_state}')

	take_action(state, reflex_vaccum_agent(state))

	curr_state = "\n".join([f'{a}: {b}' for a,b in state.items()])
	print(f'--------After--------\n {curr_state}')

	choice = input('Try Again? (y/n): ')