import urllib2
import json

#IP Adress of PI-Hole
ip_pihole = '192.168.2.254'


req = urllib2.Request("http://"+ip_pihole+"/admin/api.php")
opener = urllib2.build_opener()
f = opener.open(req)
output = json.load(f)
dnstotal = output[u'dns_queries_today']
dnsblocked = output[u'ads_blocked_today']
domainsblocked = output[u'domains_being_blocked']
percentage = output[u'ads_percentage_today']

#output
print dnstotal
print dnsblocked
print domainsblocked
print percentage