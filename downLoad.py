# Write a function to download and save a sequence of files
# INPUT: URL for first item,output directory path
# http://699340.youcanlearnit.net/image001.jpg
# http://699340.youcanlearnit.net/image050.jpg


# download_files('http://699340.youcanlearnit.net/image001.jpg', '.\images')



import os
import re
import urllib.parse
import urllib.request


def download_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    url_head, url_tail, = os.path.split(first_url)
    first_index = re.findall(r'[0-9]+', url_tail)[-1]
    index_count, error_count = 0, 0
    while error_count < 5:
        next_index = str(int(first_index) + index_count)
        if first_index[0] == '0':
            next_index = '0' * (len(first_index) - len(next_index)) + next_index
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print('Successfully downloaded {}'.format(os.path.basename(next_url)))
        except IOError:
            error_count +=1
        index_count +=1


download_files('http://699340.youcanlearnit.net/image001.jpg', '.\\~\Downloads\tes')