"""Reject corrupt numerical evidence under normal and optimised execution."""
import copy,json,zipfile
from pathlib import Path
from numerical_contract import compare_numerical
root=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(root/'provenance/resolvent_extensions_v0_1.zip') as z:
    source=json.loads(z.read('resolvent_extensions_v0_1/results/numerical.json'))
compare_numerical(source,copy.deepcopy(source))
mutations=[('seed',lambda x:x.update(seed=0)),('objective',lambda x:x['trials'][0].update(objective=999)),('nan',lambda x:x['trials'][0].update(objective=float('nan'))),('start',lambda x:x['trials'][0]['initial'].__setitem__(0,0)),('failed',lambda x:x['trials'][0].update(success=False)),('domain',lambda x:x['trials'][0]['result'].__setitem__(0,2))]
for name,mutate in mutations:
    data=copy.deepcopy(source);mutate(data)
    try:compare_numerical(source,data)
    except ValueError:pass
    else:raise ValueError('accepted corruption: '+name)
print(json.dumps({'status':'PASS','valid_acceptances':1,'invalid_rejections':len(mutations)}))
