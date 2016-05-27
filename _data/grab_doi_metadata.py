import os, json, urllib2, sys
sys.path.append('/home/psturm/bears_analyses')
from species import species_dict

base_dir = 'http://api.crossref.org/works/'
json_dictionaries = []

for subdir, dirs, files in os.walk("/home/psturm/bears_analyses/"):
    if 'config.json' in files:
        with open(subdir + '/config.json') as json_file:
            dictionary = json.load(json_file)
            if dictionary['DOI']:
                response = urllib2.urlopen(base_dir + dictionary['DOI'])
                status = response.getcode()
                data = response.read()
                if status == 200:
                    print dictionary['directory']
                    read_dict = json.loads(data)
                    read_dict = read_dict['message']
                    authors = []
                    dictionary['URL'] = read_dict['URL']

                    num_authors = 0
                    for author in read_dict['author']:
                        if num_authors >= 10:
                            authors.append('et al.')
                            break
                        authors.append(author['family'] + ', ' + author['given'])
                        num_authors += 1

                    date = "?"
	
                    if 'published-print' in read_dict:
                        date_parts = read_dict['published-print']['date-parts'][0]
                        date = '-'.join(str(x) for x in date_parts)
                        date += " print"

                    elif 'published-online' in read_dict:
                        date_parts = read_dict['published-online']['date-parts'][0]
                        date = '-'.join(str(x) for x in date_parts)
                        date += " online"
                    dictionary['fasta-link'] = species_dict[dictionary['species']]
                    dictionary['species'] = dictionary['species'].capitalize()
                    dictionary['species'] = dictionary['species'].replace('_', ' ')
                    dictionary['date'] = date
                    dictionary['authors'] = authors
                    dictionary['title'] = read_dict['title'][0]
                    dictionary['journal'] = read_dict['container-title'][0]
                    json_dictionaries.append(dictionary)


with open('doi_metadata.json', 'w') as fp:
    json.dump(json_dictionaries, fp)

print("Metadata grabbing complete!")
