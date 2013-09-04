# livemocha_checkout.py
#
# Check-out submissions posted to the legacy LiveMocha site.
#
# Usage: ./livemocha_checkout.py [writing URL] [speaking URL] [lesson number]
#
# Tim Kowalczyk 2013

from urllib2 import urlopen
from bs4 import BeautifulSoup
from sys import argv
import codecs

def main(argv):
    # Retrieve a text submission
    page = str(argv[1])
    soup = BeautifulSoup(urlopen(page).read())

    prompt = soup.find(id='exerciseContent').get_text()
    submission = soup.find(id='submission_content').get_text()

    print submission.encode('utf-8')
    filename = 'lesson' + str(argv[3]) + '.txt'
    file = codecs.open(filename,'w','utf-8')
    file.write(prompt.strip())
    file.write(submission.strip())
    file.close()

    # Retrieve an audio submission
    page = str(argv[2])
    soup = BeautifulSoup(urlopen(page).read())

    start_audio = str(soup).find('audioUrl=')
    start_audio += 9
    end_audio   = str(soup).find('flv')
    end_audio   += 3
    audiolink   = str(soup)[start_audio:end_audio]

    audio = urlopen(audiolink)
    filename = 'lesson' + str(argv[3]) + '.flv'
    audiofile = open(filename,'wb')
    audiofile.write(audio.read())
    audiofile.close()

if __name__ == '__main__':
    if len(argv) == 4:
	main(argv)
    else:
	print "%s [writing URL] [speaking URL] [lesson number]"
