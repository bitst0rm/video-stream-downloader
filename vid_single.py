import requests
import optparse

from progressbar import *

CHUNK_SIZE = 1024

widgets = ['Downloading : ', Percentage(),
           ' ', Bar(marker='#',left='[',right=']'),
           ' ', ETA(), ' ', FileTransferSpeed()]


def download_file(url, file_name=None):
    response = requests.head(url)
    total_size = int(response.headers.get('content-length'))
    pbar = ProgressBar(widgets=widgets, maxval=total_size)
    pbar.start()

    going_size = 0

    if not file_name:
        file_name = url.split('/')[-1]
    elif os.path.isfile(file_name):
        file_name += 'new_' + file_name

    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=CHUNK_SIZE): 
            going_size += CHUNK_SIZE
            pbar.update(going_size)
            if chunk:
                f.write(chunk)
                f.flush()
    pbar.finish()
    return local_filename


parser = optparse.OptionParser()
parser.add_option('-u', default=False, dest='url')
parser.add_option('-n', default=False, dest='name')

options, remainder = parser.parse_args()
file_ = download_file(options.url, options.name)

