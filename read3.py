import urllib2,json,base64
accesstoken = "SHFVSE0DGMXSXMYS7G3J"
institution = "10007772"
course = "U56119"
page = 0 
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data,indent=4)
for c in data:
	if c['Code'] == "SALARY":
	   a = c["Details"]
	   for r in a:
	   	   if r['Code'] == "MED":
	   	   	  print "Value is " + str(r['Value'])
for c in data:
	if c['Code'] == "SALARY":
	   a = c["Details"]
	   for r in a:
	   	   if r['Code'] == "LDMED":
	   	   	  print "Value is " + str(r['Value'])
for c in data:
	if c['Code'] == "NSS":
	   a = c["Details"]
	   for r in a:
	   	   if r['Code'] == "Q1":
	   	   	  print "Value is " + str(r['Value'])