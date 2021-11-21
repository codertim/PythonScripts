
import re, sys, time, urllib2


def get_links():
  f = open("links.txt", "rb")
  file_content = f.read()
  lines = file_content.split('\n')
  links = []

  for line in lines:
    # print("Current line: %s" % line)
    line_content = line.strip()
    if (len(line_content) > 0):
      # line is not empty, so is valid link
      links.append(line_content)

  return links
      

if len(sys.argv) < 2:
  print "Missing search term from command line"
  sys.exit(1)

search_term = sys.argv[1]
print("Search term: ", search_term)


links = get_links()
# print('***** Links from file: ', links)

hit_links = []

for link in links:
  print "  searching link: %s" % link
  time.sleep(0.3)
  response = urllib2.urlopen(link)
  page = response.read()
  # print("page = " + page)
  search_term_match = re.search(search_term, page)
  # print("my_match type = ", type(my_match))
  if search_term_match:
    print "    Found"
    hit_links.append(link)
  else:
    print "    Not found"


print "Found search term |%s| in links: " % search_term
for link in hit_links:
  print "  %s" % link




