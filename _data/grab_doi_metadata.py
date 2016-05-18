import os, json, urllib2


base_dir = 'http://api.crossref.org/works/'
json_dictionaries = []


for subdir, dirs, files in os.walk("."):
	if 'config.json' in files:
		with open(subdir + '/config.json') as json_file:
			dictionary = json.load(json_file)
			print(dictionary['directory'])
			print(dictionary['DOI'])
			if dictionary['DOI']:
				response = urllib2.urlopen(base_dir + dictionary['DOI'])
				status = response.getcode()
				data = response.read()
				if status == 200:
					dictionary = json.loads(data)
					json_dictionaries.append(dictionary['message'])
			print("-------")

for d in json_dictionaries:
	print(d['title'])
	print(d['author'])
	print(d['URL'])
	print(d['publisher'])
	print("----")

#with open('doi_metadata.json', 'w') as fp:
#	json.dump(json_dictionaries, fp)
