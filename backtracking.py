from timeit import default_timer as timer
start = timer()
infinity = 2**32

def select_unassigned_varible(assignment,csp):
	"""define function select_unassigned_varibla"""
	var = [var for var in csp['var'] if var not in assignment]
	a = csp['domain']
	# print var
	base = infinity
	out = infinity
	for i in var:
		# print i
		time=a[i]
		h = time[0]+time[1] # find the heustic
		if h < base:
			base = h
			out = i
	return out

def orderd_domain_value(var,assignment,csp):
	"""define function of orderd_domain_value"""
	Val = csp['value']
	Num = csp['Num']
	# print Num
	# print Val,var
	Meval = Val[var]
	T1 = -0
	T2 = -0
	for k in assignment:
		values = assignment[k]
		# print values
		t1 = values[0]
		t2 = values[1]
		if t1 > T1:
			T1 = t1
		if t2 > T2:
			T2 = t2

	new_do = []
	time = a[var]


	t11 = T1 # landing time
	# print t11,'me'
	t12 = t11+time[0]+1 # this is for account for 0 time at the begining
	# print t12,'you'
	t1 = range(t11,t12)
    
    # wrong. rang(0,0) does not loop.
	for t1 in range(t11,t12):
		t21 = t1 + time[1]+time[2] # takenoff time
		t22 = t1 + time[1]+time[4]+1
		for t2 in range(t21,t22):
			val = [t1,t2]
			new_do.append(val)
	# print Num
	if Num > 24:
		return new_do
	else:
		return Meval


def assign(var,value,assignment):
	"""define function of assign"""
	assignment[var]=value
	return assignment

def check_safe(var,value,assignment):
	"""define function of check_safe"""
	T1 = []
	T2 = []
	T3 = []

	for k in assignment:
		time = a[k]
		# print time,k # key value
		values = assignment[k]
		t1 = range(values[0],values[0]+time[1]) # landing time for this varible
		t2 = range(values[1],values[1]+time[3]) # takeoff time for this varible
		t3 = range(values[0]+time[1],values[1]) # time at the gate

		T1.append(t1)
		T2.append(t2)
		T3.append(t3)
	meva = value 
	# print meva

	
	base = meva
	var = var
	time_base = a[var]
	start_base = base[0]
	# print start_base
	l_base = range(start_base, start_base+time_base[1])
	# # print l_base
	n=1
	for i in T1:
		if set(i).intersection(set(l_base)):
			# print set(i).intersection(set(l_base))
			n+=1
	# print n
	if n > L:
		return False

	end_base = base[1]
	t_base = range(end_base, end_base+time_base[3])
	# print t_base
	n=1
	for i in T2:
		if set(i).intersection(set(t_base)):
			# print set(i).intersection(set(t_base))
			n+=1
	# print n
	if n > T:
		return False

	g_base = range(start_base+time_base[1], end_base)
	# print g_base
	n=1
	for i in T3:
		if set(i).intersection(set(g_base)):
			# print set(i).intersection(set(g_base))
			n+=1
	# print n
	if n > G:
		return False

	return True 


def inference(csp,var,value):
	"""define function inference"""
	return None

def unassign(var,assignment):
	"""define unssign function"""
	if var in assignment:
		del assignment[var]



def backtraching_search(csp):
	"""define main function of backtracking_search"""
	return backtrack({},csp)

def backtrack(assignment,csp):
	"""define backtrack function """
	# inference={}
	varible=csp['var']
	if len(assignment) == len(varible):
		# print len(assignment)
		return assignment
	var = select_unassigned_varible(assignment,csp)
	# print var
	for meval in orderd_domain_value(var,assignment,csp):
		# print 'meb'
		if check_safe(var,meval,assignment) == True:
			# print check_safe(var,meval,assignment)
			assign(var,meval,assignment)
			# print assignment
			# inference = inference(csp,var,value)
			# if inference(csp,var,meval)== True:
			result = backtrack(assignment,csp)
			if result is not None:
				return result
		unassign(var,assignment)
		# print assignment
	return None



input = open('input.txt','r')
Nm = input.readline().replace('\n','').replace('\r','')
Nm = Nm.split()
# print Nm
L=int(Nm[0])
G=int(Nm[1])
T=int(Nm[2])
# print L,G,T

N1 = input.readline().replace('\n','').replace('\r','')

n = int(N1)
# print n
a = []
for i in range(n):
	NN = input.readline().replace('\n','').replace('\r','')
	l=NN.split()
	ai = []
	# print l
	for x in range(5):
		# print x # x is the index 
		ai.append(int(l[x]))
		# ai.append(int(NN[x]))
	a.append(ai)
# print(a)

Var = [] #define varible to be a list
Domain = {}
Value = []

## check the loop carefully. comment y. he.
for i in range(n):
	var = i
	# print i
	Var.append(var)

	value = []
	time = a[i]
	t11 = 0 # landing time
	t12 = time[0]+1 # this is for account for 0 time at the begining
	# print t12
	t1 = range(t11,t12)
    # print t1
    # wrong. rang(0,0) does not loop.
	for t1 in range(t11,t12):
		# print t1
		t21 = t1 + time[1]+time[2] # takenoff time
		t22 = t1 + time[1]+time[4]+1 # for the case with the same gate waiting time
		# print t21,t22
		for t2 in range(t21,t22):
			# print t1,t2
			val = [t1,t2]
			# print val

			value.append(val)
			# print value
	Value.append(value)


csp = {"land":L, "gate":G, "takeoff":T,'Num':n,"domain":a,"var":Var,"value":Value} # globle varibale

# print select_unassigned_varible(assignment,csp)
# print orderd_domain_value(var,assignment,csp)
# print assign(var,value,assignment)
# print unassign(var,assignment)
# print check_safe(var,value,assignment)
# print inference(csp,var,value)
# 
# print backtraching_search(csp)
opt = backtraching_search(csp)

filename = 'output.txt'
with open(filename,'w') as zaili:
	for i in opt:
		out = opt[i]
		a = out[0]
		b = out[1]
		zaili.write(str(a)+" "+str(b)+'\n')

end = timer()
print (end-start)
