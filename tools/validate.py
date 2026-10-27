"""Simulation-readiness validator for the foundation URDF."""
import re, sys, xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DOF = 23
t = ET.parse(ROOT/"urdf/bhiv_humanoid_foundation.urdf").getroot()
links = [l.get("name") for l in t.findall("link")]
joints = t.findall("joint")
res = []
def chk(name, ok, detail=""): res.append((name, ok, detail))
chk("unique link names", len(links)==len(set(links)), f"{len(links)} links")
jn = [j.get("name") for j in joints]
chk("unique joint names", len(jn)==len(set(jn)), f"{len(jn)} joints")
chk("link names snake_case ending _link", all(re.fullmatch(r"[a-z][a-z0-9_]*_link", n) for n in links))
chk("joint names snake_case ending _joint", all(re.fullmatch(r"[a-z][a-z0-9_]*_joint", n) for n in jn))
parents = {j.find("child").get("link"): j.find("parent").get("link") for j in joints}
roots = [l for l in links if l not in parents]
chk("single root link (base_link)", roots==["base_link"], str(roots))
chk("tree: every non-root link has exactly one parent joint", len(parents)==len(links)-1)
def reach(l, seen=()):
    return l=="base_link" or (l not in seen and l in parents and reach(parents[l], seen+(l,)))
chk("all links reach root, no cycles", all(reach(l) for l in links))
rev = [j for j in joints if j.get("type")=="revolute"]
chk(f"DOF == {EXPECTED_DOF} (estimated)", len(rev)==EXPECTED_DOF, str(len(rev)))
chk("revolute axes are unit vectors", all(abs(sum(float(x)**2 for x in j.find("axis").get("xyz").split())-1)<1e-9 for j in rev))
chk("revolute limits present, lower<upper", all(float(j.find("limit").get("lower"))<float(j.find("limit").get("upper")) for j in rev))
bad = [l.get("name") for l in t.findall("link") if float(l.find("inertial/mass").get("value"))<=0]
chk("all link masses > 0", not bad, str(bad))
ok_i = True
for l in t.findall("link"):
    i = l.find("inertial/inertia"); ix,iy,iz = (float(i.get(k)) for k in ("ixx","iyy","izz"))
    ok_i &= ix+iy>=iz and ix+iz>=iy and iy+iz>=ix
chk("inertia triangle inequality", ok_i)
chk("visual + collision on every link", all(l.find("visual") is not None and l.find("collision") is not None for l in t.findall("link")))
by = {j.get("name"): j for j in joints}; sym = True; why = []
for n,j in by.items():
    if n.startswith("l_"):
        r = by.get("r_"+n[2:])
        if r is None: sym=False; why.append(n); continue
        a = [float(x) for x in j.find("origin").get("xyz").split()]; b = [float(x) for x in r.find("origin").get("xyz").split()]
        if not (abs(a[0]-b[0])<1e-9 and abs(a[2]-b[2])<1e-9 and abs(a[1]+b[1])<1e-9): sym=False; why.append(n)
chk("L/R joint pairs exist and mirror in Y", sym, str(why))
w = max(len(r[0]) for r in res)
for n,ok,d in res: print(f"[{'PASS' if ok else 'FAIL'}] {n.ljust(w)} {d}")
print("\nRESULT:", "ALL PASS" if all(r[1] for r in res) else "FAILURES PRESENT")
sys.exit(0 if all(r[1] for r in res) else 1)
