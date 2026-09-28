#!/usr/bin/env python3
"""Rational research diagnostics. Input is a JSON file, output an exact JSON receipt."""
import argparse,json
from pathlib import Path
from core import *
def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("Use an integer or a rational string; JSON floats are not accepted.")
    return F(value)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);args=ap.parse_args();d=json.loads(args.input.read_text())
    if d['task']=='recover':
        S=[[rational(x) for x in row] for row in d['skew']];result=recover(S,rational(d['u']))
    elif d['task']=='weighted_minimum':
        m=list(map(rational,d['m']));g=list(map(rational,d['diagonal']));t=rational(d['t']);lo,hi=minimum_bracket(m,g,t,int(d.get('bits',120)))
        result={'task':d['task'],'minimum_interval':[str(lo),str(hi)],'all_transitive_orders_attain':True,
                'spectral_radius_below_one_possible':max(g)<1 and poly_minimum(F(1),m,g,t)>0,
                'statement_scope':'Specified factorised off-diagonal family only; not arbitrary network design.'}
    else:raise ValueError('unknown task')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
