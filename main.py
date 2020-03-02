from queues import Queue

def main():
	q1 = Queue()
	print(q1.values)
	[q1.add(item) for item in ['Estágio 1', 'João Pessoa', '2019.2', 'ED', 'IFPB']]
	print(q1.values)
	
main()