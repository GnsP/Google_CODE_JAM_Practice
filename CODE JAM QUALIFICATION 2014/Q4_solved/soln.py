import sys

def normalStrategy(Naomi,Ken):
	scoreNaomi=0
	Naomi_l = [x for x in Naomi]
	Ken_l = [x for x in Ken]
	while len(Naomi_l)>0:
		if Naomi_l[-1] > Ken_l[-1]:
			del Naomi_l[-1]
			del Ken_l[0]
			scoreNaomi = scoreNaomi+1
		else:
			for k in range(len(Ken_l)):
				if Ken_l[k] > Naomi_l[-1]:
					del Ken_l[k]
					break
			del Naomi_l[-1]
	return scoreNaomi
	
def deceitStrategy(Naomi,Ken):
	scoreNaomi=0
	Naomi_l = [x for x in Naomi]
	Ken_l = [x for x in Ken]
	while len(Naomi_l)>0:
		index = None
		for i in range(len(Naomi_l)):
			if Naomi_l[i] > Ken_l[0]:
				index = i
				break
		if index != None:
			scoreNaomi = scoreNaomi+1
			del Naomi_l[index]
			del Ken_l[0]
		else:
			del Naomi_l[0]
			del Ken_l[0]
	return scoreNaomi
				

sys.stdin = open('input.in','r')
sys.stdout = open('output.out','w+')
				
T = int(input())
for i in range(1,T+1):
	N = int(input())
	Naomi = [float(x) for x in input().split()]
	Ken = [float(x) for x in input().split()]
	Naomi.sort()
	Ken.sort()
	print('Case #{CaseNo}: {Dct} {Nrm}'.format(CaseNo=i,Dct=deceitStrategy(Naomi,Ken),Nrm=normalStrategy(Naomi,Ken)))
	
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__