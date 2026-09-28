#!/usr/bin/env python3
"""Publication-specific checks. These check statements against exact fixtures,
source lineage and executable domains; they do not replace mathematical review.
"""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,io,json,zipfile
from core import require,BL,Q,recover,mm,eye,poly_minimum
ROOT=Path(__file__).resolve().parents[1]
def main():
    groups=[]
    p=(ROOT/'paper/perron_minima.md').read_text()
    required=['skew tournament matrix of even order $n\\ge4$','not asserted on the full skew box','Every local minimum','for every diagonal','fixed but unknown parameters','do **not** assert','not necessarily return a nearest','entrywise discrepancy','bit-complexity','publisher-controlled']
    for text in required:require(text.lower() in p.lower(),'missing scope clarification: '+text)
    groups.append('ten scope statements present')
    # The excluded n=2,t=1 endpoint is a nontrivial nilpotent shift.
    A=[[F(1)+x for x in row] for row in BL(2)];N=[[A[i][j]-F(i==j) for j in range(2)] for i in range(2)]
    require(mm(N,N)==[[0,0],[0,0]] and N!=[[0,0],[0,0]],'exceptional endpoint reconstruction')
    groups.append('exceptional endpoint reconstructed')
    for S,u in [(BL(2),F(1,2)),([[F(0)]*4 for i in range(4)],F(1,10)),(BL(4),F(1,3))]:
        try:recover(S,u)
        except ValueError:pass
        else:raise ValueError('bad recovery-domain acceptance')
    groups.append('invalid spectral domains rejected')
    require(poly_minimum(F(1),list(map(F,['1/3','2/3','1'])),[F(0)]*3,F(3,4))==F(13,48),'reviewed sanity example')
    groups.append('reviewed exact stability sign')
    fr=json.loads((ROOT/'results/fragility_exact.json').read_text());ph=list(map(F,fr['polynomials']['high']['coefficients']));pl=list(map(F,fr['polynomials']['low']['coefficients']))
    require(all(a==b for a,b in zip(ph[:-1],pl[:-1])) and ph[-1]-pl[-1]==F(-3,400),'published polynomial separation')
    groups.append('constant separation minus three over four hundred')
    require(fr['polynomials']['high']['count']==16 and fr['polynomials']['low']['count']==8,'fragility class counts')
    groups.append('transitive class multiplicities')
    local=json.loads((ROOT/'results/local_minima_intervals.json').read_text())
    require(local['strict_local_minimum_vertices']==24 and local['signed_coordinate_derivatives']==144,'local witness count')
    require(all(F(x)>F(6927,100000) for case in local['cases'] for x in case['lower_bounds_on_inward_coordinate_derivatives']),'published derivative margin')
    groups.append('exact gradient certificate consumed')
    rec=json.loads((ROOT/'results/recovery_example.json').read_text())
    require(rec['edits_to_returned_BL']==4 and rec['nearest_distance']==1 and rec['count_bound']==6,'recovery limitation')
    require(rec['spectral_upper_to_instance_distance_floor']==6,'input-specific bound')
    groups.append('non-nearest and instance estimates')
    for f in [ROOT/'replay.py',*(ROOT/'code').glob('*.py')]:
        tree=ast.parse(f.read_text())
        require(not any(isinstance(n,ast.Assert) for n in ast.walk(tree)),'assert gate in '+str(f))
    groups.append('no current assertion gates')
    z=zipfile.ZipFile(ROOT/'provenance/resolvent_extensions_v0_1.zip')
    require((ROOT/'code/core.py').read_bytes()==z.read('resolvent_extensions_v0_1/code/core.py'),'changed reviewed core')
    require((ROOT/'code/diagnostic.py').read_bytes()==z.read('resolvent_extensions_v0_1/code/diagnostic.py'),'changed reviewed diagnostic')
    groups.append('reviewed executable core retained byte-for-byte')
    nested=z.read('resolvent_extensions_v0_1/provenance/tournament_envelope_v0_1.zip')
    require(hashlib.sha256(nested).hexdigest()=='25a90b62e165d2a8e779f1760859283da67387bc06a7fdc334cb88c9a6071ac4','predecessor identity')
    groups.append('stable predecessor identity')
    for d in json.loads((ROOT/'PROVENANCE.json').read_text())['inputs']:
        require(hashlib.sha256((ROOT/d['path']).read_bytes()).hexdigest()==d['sha256'],'input changed')
    groups.append('unchanged supplied inputs')
    release=json.loads((ROOT/'RELEASE.json').read_text())
    require(release['doi']=='10.5281/zenodo.23014818' and release['canonical_release_url']=='https://evidencepress.org/releases/perron-minima/' and release['public_licence']=='CC0-1.0' and release['authors']==['Anonymous'],'publication identity mismatch')
    groups.append('authorised Anonymous CC0 publication identity matches reserved DOI')
    build=json.loads((ROOT/'BUILD.json').read_text())
    for name,h in build['sha256'].items():require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'build/source mismatch '+name)
    groups.append('document build identities')
    report={'status':'PASS','groups':groups,'group_count':len(groups),'scope':'bounded publication and arithmetic regression checks; not proof-assistant verification'}
    (ROOT/'results/manuscript_checks.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
