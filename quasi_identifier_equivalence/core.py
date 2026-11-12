import json
from .common import identifier,integer
def run(data):
 rows=data['rows'];keys=data['quasi_identifiers'];sensitive=identifier(data['sensitive_field'])
 if not isinstance(rows,list)or len(rows)>10000 or not isinstance(keys,list)or not 1<=len(keys)<=20:raise ValueError('shape')
 if len(set(keys))!=len(keys):raise ValueError('duplicate_key')
 for k in keys:identifier(k)
 groups={}
 for i,r in enumerate(rows):
  key=json.dumps([r[k]for k in keys],sort_keys=True,allow_nan=False);groups.setdefault(key,[]).append(i)
 classes=[{'row_indices':ids,'size':len(ids),'sensitive_distinct':len({json.dumps(rows[i][sensitive],sort_keys=True,allow_nan=False)for i in ids})}for ids in groups.values()]
 return {'classes':classes,'minimum_class_size':min((r['size']for r in classes),default=None),'minimum_distinct_sensitive':min((r['sensitive_distinct']for r in classes),default=None),'anonymity_guaranteed':False,'external_linkage_tested':False}
