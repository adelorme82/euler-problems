import pprint
import Util
pp = pprint.PrettyPrinter(indent=4)
known_chains = {1:[1]}
max_chain_len = 1
max_chain_index = 1
loops = 1
def collatz(num):
	global max_chain_len
	global max_chain_index
	global loops
	chain = [num]
	temp_num = num
	while num > 1:
		loops += 1
		if num % 2 == 0:
			num /= 2
		else:
			num = num * 3 + 1
		if num in known_chains:
			chain = chain + known_chains[num]
			num = 1
		else:
			chain.append(num)
			# collatz(num)
	known_chains[temp_num] = chain
	if len(chain) > max_chain_len:
		max_chain_len = len(chain)
		max_chain_index = temp_num

MAX_NUM = 1000000
Util.start_time()
for i in range(MAX_NUM):
	collatz(i)
Util.stop_time()
# pp.pprint(known_chains)
print 'loops', loops
print 'max_chain_len', max_chain_len
print 'max_chain_index', max_chain_index

