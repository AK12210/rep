#task1
def imdbch(movies): 
    return movies['imdb'] > 5.5


print(imdbch(movies[7]))
#task2
def imdbchl(movies):
	mov = []
	for i in range(0, len(movies)):
		if movies[i]['imdb'] > 5.5:
			mov.append(movies[i]['name'])
	return mov


print(imdbchl(movies))
#task3
def imdbc(s):
	mov = []
	for i in range(0, len(movies)):
		if movies[i]['category'] == s:
			mov.append(movies[i]['name'])
	return mov


print(imdbc('Romance'))
#task4
def imdbs(s):
	sum = 0
	for i in range(0, len(movies)):
		sum += movies[i]['imdb']
	return sum / len(movies)


print(imdbs(movies))
#task5
def imdbss(s):
	sum = 0
	j = 0
	for i in range(0, len(movies)):
		if movies[i]['category'] == s:
			sum += movies[i]['imdb']
			j += 1
	return sum / j


print(imdbss('Suspense'))
