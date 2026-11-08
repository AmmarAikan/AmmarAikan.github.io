from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,hashlib,urllib.request,time,json
root=Path('public') if Path('public/index.html').exists() else Path('.')
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  for key in ['src','href']:
   if key in a:self.refs.append(a[key])
p=Parser();p.feed((root/'index.html').read_text(encoding='utf-8'))
assert p.h1==1 and len(p.ids)==len(set(p.ids))
for ref in p.refs:
 u=urlsplit(ref)
 if u.scheme:continue
 if u.path:assert (root/unquote(u.path).lstrip('/')).is_file(),ref
 elif u.fragment:assert u.fragment in p.ids,ref
assert (root/'assets/cv/Ammar_Aikan_ATS_CV.pdf').read_bytes().startswith(b'%PDF-')
print('Static assets, anchors, headings and PDF checks passed.')
if len(sys.argv)>1:
 base=sys.argv[1].rstrip('/')+'/'
 for attempt in range(8):
  try:
   for name in ['index.html','assets/cv/Ammar_Aikan_ATS_CV.pdf'] + [x.relative_to(root).as_posix() for x in root.glob('assets/reports/*Public_Portfolio_Edition.pdf')]:
    with urllib.request.urlopen(base+name+'?verify='+str(time.time_ns()),timeout=20) as r:data=r.read()
    expected=(root/name).read_bytes()
    assert hashlib.sha256(data).digest()==hashlib.sha256(expected).digest(),'Live content differs: '+name
    print(json.dumps({'url':base+name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
   print('LIVE_CONTENT_VERIFIED');break
  except Exception as exc:
   print('Attempt',attempt+1,str(exc))
   if attempt==7:raise
   time.sleep(10)
