#!/usr/bin/env python3
"""Rational publication interfaces. Run: public_diagnostic.py robust input.json."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from extensions import robust_box,parse_vector,parse_rational,factorisation,approximate_factorisation

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['robust','factorisation','approximation'])
    p.add_argument('input',type=Path)
    a=p.parse_args();d=json.loads(a.input.read_text())
    if a.mode=='robust':
        out=robust_box(*[parse_vector(d[k]) for k in ['m_lower','m_upper','gamma_lower','gamma_upper']], parse_rational(d['t_lower']),parse_rational(d['t_upper']))
    else:
        b=[parse_vector(r) for r in d['pair_weights']]
        out=factorisation(b) if a.mode=='factorisation' else approximate_factorisation(b,parse_vector(d['vertex_weights']))
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
