import random
import math
import numpy as np
import matplotlib.pyplot as plt



X = [None,0,-1,-1,0,0,-1,-1,0,1,1,1,1,2,2,2,2]
Y = [None,2,2,1,1,0,0,-1,-1,-1,0,1,2,2,1,0,-1]


iterations = 100000


E = [0 for _ in range(iterations+2)] #energy in each iteration
N = [i for i in range(iterations+2)] #iteration number


energy = -1
E[1] = -9


for j in range(1,iterations+1):

	r = random.randint(1,16) #generate position in chain

	if r==1:
		m=2 #second to end terminal
		n=3 #third to end terminal

	if r==16:
		m=15 #second to end terminal
		n=14 #third to end terminal

	if r==1 or r==16: #end move
		if X[m] == X[r]-1: 
			if Y[n]==Y[r]:
				r1 = random.randint(1,2)
				if r1==1:
					a = X[r]-1
					b = Y[r]-1

				if r1==2:
					a=X[r]-1
					b=Y[r]+1

			if Y[n] == Y[r]+1:
				a = X[r]-1
				b = Y[r]-1

			if Y[n] == Y[r]-1:
				a = X[r]-1
				b = Y[r]+1

		if Y[m] == Y[r]-1:
			if X[n] == X[r]:
				r1 = random.randint(1,2)
				if r1==1:
					a=X[r]-1
					b=Y[r]-1

				if r1==2:
					a=X[r]+1
					b=Y[r]-1

			if X[n]==X[r]+1:
				a=X[r]-1
				b=Y[r]-1

			if X[n]==X[r]-1:
				a=X[r]+1
				b=Y[r]-1

		if X[m]==X[r]+1:
			if Y[n]==Y[r]:
				r1=random.randint(1,2)
				if r1==1:
					a=X[r]+1
					b=Y[r]-1
				
				if r1==2:
					a=X[r]+1
					b=Y[r]+1

			if Y[n]==Y[r]+1:
				a = X[r]+1
				b = Y[r]-1

			if Y[n] == Y[r]-1:
				a = X[r]+1
				b = Y[r]+1

		if Y[m] == Y[r]+1:
			if X[n] == X[r]:
				r1 = random.randint(1,2)
				if r1==1:
					a=X[r]+1
					b=Y[r]+1

				if r1==2:
					a=X[r]-1
					b=Y[r]+1

			if X[n] == X[r]+1:
				a=X[r]-1
				b=Y[r]+1

			if X[n] == X[r]-1:
				a=X[r]+1
				b=Y[r]+1



	if r>1 and r<16: #crankshaft
		a = X[r]
		b = Y[r]
		m = r+1
		n = r-1

		if X[n]==X[r] and Y[n]==Y[r]+1 and X[m]==X[r]+1 and Y[m]==Y[r]:
			a+=1
			b+=1

		if X[n]==X[r]-1 and Y[n]==Y[r] and X[m]==X[r] and Y[m]==Y[r]-1:
			a-=1
			b-=1

		if X[n]==X[r]+1 and Y[n]==Y[r] and X[m]==X[r] and Y[m]==Y[r]+1:
			a+=1
			b+=1

		if X[n]==X[r] and Y[n]==Y[r]-1 and X[m]==X[r]-1 and Y[m]==Y[r]:
			a-=1
			b-=1

		if X[n]==X[r]-1 and Y[n]==Y[r] and X[m]==X[r] and Y[m]==Y[r]+1:
			a-=1
			b+=1

		if X[n]==X[r] and Y[n]==Y[r]-1 and X[m]==X[r]+1 and Y[m]==Y[r]:
			a+=1
			b-=1

		if X[n]==X[r] and Y[n]==Y[r]+1 and X[m]==X[r]-1 and Y[m]==Y[r]:
			a-=1
			b+=1

		if X[n]==X[r]+1 and Y[n]==Y[r] and X[m]==X[r] and Y[m]==Y[r]-1:
			a+=1
			b-=1

	for i in range(1,17): #ignore if position is occupied
		if a==X[i] and b==Y[i]:
			a = X[r]
			b = Y[r]

	c = X[r] #old position
	d = Y[r]
	X[r] = a #assigning new position
	Y[r] = b


#interaction energies
	if (X[1]-X[12])**2 + (Y[1]-Y[12])**2 ==1:
		E[j+1] += energy
	if (X[1]-X[4])**2 + (Y[1]-Y[r])**2 ==1:
		E[j+1] += energy
	if (X[3]-X[6])**2 + (Y[3]-Y[6])**2 ==1:
		E[j+1] += energy
	if (X[4]-X[11])**2 + (Y[4]-Y[11])**2 ==1:
		E[j+1] += energy
	if (X[5]-X[10])**2 + (Y[5]-Y[10])**2 ==1:
		E[j+1] += energy
	if (X[5]-X[8])**2 + (Y[5]-Y[8])**2 ==1:
		E[j+1] += energy
	if (X[11]-X[14])**2 + (Y[11]-Y[14])**2 ==1:
		E[j+1] += energy
	if (X[10]-X[15])**2 + (Y[10]-Y[15])**2 ==1:
		E[j+1] += energy
	if (X[9]-X[16])**2 + (Y[9]-Y[16])**2 ==1:
		E[j+1] += energy

	dE = E[j+1] - E[j]
	probability = math.exp(-dE) #will be greater than 1 if dE is negative

	r2 = random.random()

	if r2>=probability:
		X[r]=c
		Y[r]=d
		E[j+1]=E[j]


	
	plt.plot(X,Y)
#	plt.xlim(-8,8)
#	plt.ylim(-8,8)
	plt.grid(linewidth=0.2)
	plt.title('iteration='+str(j))
	plt.pause(0.05)
	if j!=iterations:
		plt.clf()
plt.show()

plt.plot(N[1:],E[1:]) #plotting energy vs iteration graph
plt.show()
