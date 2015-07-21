import urllib2 , re , sys

url = sys.argv[1]

searching = urllib2.urlopen(url)

reading = searching.read()

with_http = re.findall('href="http://(.*?)"',reading)
with_https = re.findall('href="https://(.*?)"',reading)

result = with_http + with_https

for i in range(len(result)):
    print "[+]",result[i]
