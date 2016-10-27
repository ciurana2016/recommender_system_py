import os.path
from scipy.sparse import coo_matrix


def no_file():
    print 'Dataset not found, please download the file from:'
    print 'http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-360K.tar.gz (1.6GB)'
    print 'then place it in recommender_system_py/data/ and change the file_path'
    print 'variable on the fetch_lastfm function'


def fetch_lastfm(min_plays=200):
   
    file_path = 'data/100k_lines_lastfm.tsv'

    if not os.path.exists(file_path):
        return no_file()

    # Data to create our coo_matrix
    data, row, col = [], [], []

    # Artists by id, and users
    artists, users = {}, {}

    # Read the file and fill variables with data to
    # create the matrix and have the artists by id
    with open(file_path) as data_file:
        for n, line in enumerate(data_file):

            # If you use the original data from lastfm (14 million lines)
            # if n == SOMEINT: break
            
            # Readable data (for humans)
            readable_data = line.split('\t')
            user =           readable_data[0]
            artist_id =      readable_data[1]
            artist_name =    readable_data[2]
            plays =     int(readable_data[3])

            if user not in users:
                users[user] = len(users)

            if artist_id not in artists:
                artists[artist_id] = {
                        'name' : artist_name,
                        'id' : len(artists)
                        }

            # Data for the coo_matrix if the artist was played > 200 times
            if plays > min_plays:
                data.append(plays)
                row.append(users[user])
                col.append(artists[artist_id]['id'])

    # Our matrix: ((plays, (user, artist)))
    coo = coo_matrix((data,(row,col)))

    # We return the matrix, the artist dictionary and the amount of users
    dictionary = {
        'matrix' : coo,
        'artists' : artists,
        'users' : len(users)
    }

    return dictionary
