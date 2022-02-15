def find_missing(vetor):
	dif=vetor[len(vetor)-1] - vetor[0]
	pa=dif/len(vetor)
	for i in range(len(vetor)-1):
		if vetor[i+1] - vetor[i] != pa: 
			return vetor[i] + pa  

