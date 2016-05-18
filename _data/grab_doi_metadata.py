import os, json, urllib2


base_dir = 'http://api.crossref.org/works/'
json_dictionaries = []


for subdir, dirs, files in os.walk("."):
    if 'config.json' in files:
        with open(subdir + '/config.json') as json_file:
            dictionary = json.load(json_file)
            print '.',
            if dictionary['DOI']:
                response = urllib2.urlopen(base_dir + dictionary['DOI'])
                status = response.getcode()
                data = response.read()
                if status == 200:
                    read_dict = json.loads(data)
                    read_dict = read_dict['message']
                    authors = []
                    dictionary['URL'] = read_dict['URL']
                    num_authors = 0
                    for author in read_dict['author']:
                        if num_authors >= 3:
                            authors.append('et al.')
                            break
                        authors.append(author['given'] + ' ' + author['family'])
                        num_authors += 1

                    dictionary['authors'] = authors
                    dictionary['title'] = read_dict['title'][0]
                    dictionary['publisher'] = read_dict['publisher']
                    json_dictionaries.append(dictionary)

with open('doi_metadata.json', 'w') as fp:
    json.dump(json_dictionaries, fp)

print("Metadata grabbing complete!")
