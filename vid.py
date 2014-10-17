import requests
import optparse

parser = optparse.OptionParser()
parser.add_option('-u', default=False, dest='url')
parser.add_option('-s', default=False, dest='sf')


options, remainder = parser.parse_args()

fragment = int(options.sf) or 1
fragments = []
while fragment < 10:
    url = options.url.replace('$', str(fragment))
    print "url: ",url
    response = requests.get(url)
    fragment += 1
    fragments.append(response.content)

f = open('myvideo.mp4', 'wb')
f.write(''.join(fragments))
f.close()

