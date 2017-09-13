'''import json
l = "{'a':2,'b':3}"

k=json.loads(l)
print k
print k['a']'''
import json
import string
json_input = "{ 'one': 1, 'two': { 'list': [ {'item':'#A'},{'item':'B'} ] } }"
#json_input = "{'one':1, 'two':'ISIS'}"

s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
s = s.replace("#","\#")
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
print json_acceptable_string," ",s
# d = {u'muffin': u'lolz', u'foo': u'kitty'}
print "d value:", d['muffin']
json_input = json_input.replace("#"," ")
json_acceptable_string = json_input.replace("'", "\"")
d = json.loads(json_acceptable_string)
print "jjj ",d['two']

str = "{u'contributors': None, u'truncated': False, u'text': u'Great goal and great celebration by seb and the fans. OrlandoUnited OrlandoStrong #OCSC  https://t.co/ry45iGUeMe', u'is_quote_status'"

ind1 = str.index("u'text'")
ind2 = str.index("u'is_quote_status'")
print "hello", str[ind1+10:ind2-2]


'''
try:
    decoded = json.loads(json_input)

    # pretty printing of json-formatted string
    print json.dumps(decoded, sort_keys=True, indent=4)

    print "JSON parsing example: ", decoded['one']
    print "Complex JSON parsing example: ", decoded['two']['list'][1]['item']

except (ValueError, KeyError, TypeError):
    print "JSON format error"
'''