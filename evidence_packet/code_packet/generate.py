"""Generates URDF, DOF map, joint hierarchy and previews from ONE parameter set.
All dimensions are PLACEHOLDERS (metres/kg/rad) until reconciled with real CAD."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
links, joints, GROUP = {}, [], {}

def L(name, size, center, mass, group):
    links[name] = dict(size=size, center=center, mass=mass); GROUP[name] = group
def J(name, typ, parent, child, xyz, axis=None, lim=None, group=""):
    joints.append(dict(name=name, type=typ, parent=parent, child=child, xyz=xyz, axis=axis, limit=lim, group=group))

YAW, PITCH, ROLL = (0,0,1), (0,1,0), (1,0,0)
S = (0.04, 0.04, 0.04)  # servo-housing placeholder block

L("base_link", (0.10,0.20,0.08), (0,0,0), 1.0, "hip")
J("waist_yaw_joint","revolute","base_link","torso_link",(0,0,0.04),YAW,(-1.57,1.57),"waist")
L("torso_link", (0.10,0.22,0.25), (0,0,0.125), 2.0, "torso")
J("neck_yaw_joint","revolute","torso_link","neck_link",(0,0,0.25),YAW,(-1.57,1.57),"head")
L("neck_link", S, (0,0,0.02), 0.1, "head")
J("head_pitch_joint","revolute","neck_link","head_link",(0,0,0.04),PITCH,(-0.7,0.7),"head")
L("head_link", (0.10,0.10,0.12), (0,0,0.06), 0.4, "head")

for p, s in (("l", 1), ("r", -1)):
    J(f"{p}_shoulder_pitch_joint","revolute","torso_link",f"{p}_shoulder_link",(0,s*0.14,0.21),PITCH,(-2.5,2.5),"arm")
    L(f"{p}_shoulder_link", S, (0,0,0), 0.1, "arm")
    J(f"{p}_shoulder_roll_joint","revolute",f"{p}_shoulder_link",f"{p}_shoulder_roll_link",(0,0,0),ROLL,(-1.57,1.57),"arm")
    L(f"{p}_shoulder_roll_link", S, (0,0,0), 0.1, "arm")
    J(f"{p}_upper_arm_yaw_joint","revolute",f"{p}_shoulder_roll_link",f"{p}_upper_arm_link",(0,0,-0.03),YAW,(-1.57,1.57),"arm")
    L(f"{p}_upper_arm_link", (0.04,0.04,0.12), (0,0,-0.06), 0.2, "arm")
    J(f"{p}_elbow_pitch_joint","revolute",f"{p}_upper_arm_link",f"{p}_forearm_link",(0,0,-0.12),PITCH,(-2.4,0.0),"forearm")
    L(f"{p}_forearm_link", (0.035,0.035,0.11), (0,0,-0.055), 0.15, "forearm")
    J(f"{p}_wrist_fixed_joint","fixed",f"{p}_forearm_link",f"{p}_hand_link",(0,0,-0.11),None,None,"hand")
    L(f"{p}_hand_link", (0.03,0.06,0.08), (0,0,-0.04), 0.1, "hand")
    J(f"{p}_hip_yaw_joint","revolute","base_link",f"{p}_hip_yaw_link",(0,s*0.07,-0.04),YAW,(-0.8,0.8),"leg")
    L(f"{p}_hip_yaw_link", S, (0,0,0), 0.15, "leg")
    J(f"{p}_hip_roll_joint","revolute",f"{p}_hip_yaw_link",f"{p}_hip_roll_link",(0,0,-0.03),ROLL,(-0.7,0.7),"leg")
    L(f"{p}_hip_roll_link", S, (0,0,0), 0.15, "leg")
    J(f"{p}_hip_pitch_joint","revolute",f"{p}_hip_roll_link",f"{p}_thigh_link",(0,0,-0.02),PITCH,(-1.57,0.8),"leg")
    L(f"{p}_thigh_link", (0.05,0.05,0.20), (0,0,-0.10), 0.4, "leg")
    J(f"{p}_knee_pitch_joint","revolute",f"{p}_thigh_link",f"{p}_shank_link",(0,0,-0.20),PITCH,(0.0,2.4),"leg")
    L(f"{p}_shank_link", (0.04,0.04,0.20), (0,0,-0.10), 0.3, "leg")
    J(f"{p}_ankle_pitch_joint","revolute",f"{p}_shank_link",f"{p}_ankle_link",(0,0,-0.20),PITCH,(-0.8,0.8),"foot")
    L(f"{p}_ankle_link", S, (0,0,0), 0.1, "foot")
    J(f"{p}_ankle_roll_joint","revolute",f"{p}_ankle_link",f"{p}_foot_link",(0,0,-0.02),ROLL,(-0.5,0.5),"foot")
    L(f"{p}_foot_link", (0.16,0.07,0.02), (0.03,0,-0.03), 0.2, "foot")

n = 0
for j in joints:
    if j["type"] == "revolute":
        n += 1; j["servo"] = f"S{n:02d}"
    else: j["servo"] = "-"

def f(v): return " ".join(f"{x:g}" for x in v)
def inertia(m, s):
    x,y,z = s
    return m/12*(y*y+z*z), m/12*(x*x+z*z), m/12*(x*x+y*y)

o = ['<?xml version="1.0"?>', '<!-- PLACEHOLDER-DIMENSION foundation model. REP-103: x fwd, y left, z up. Units SI. -->', '<robot name="bhiv_humanoid">']
for name, d in links.items():
    ix,iy,iz = inertia(d["mass"], d["size"])
    geo = f'<geometry><box size="{f(d["size"])}"/></geometry>'
    o += [f'  <link name="{name}">',
          f'    <inertial><origin xyz="{f(d["center"])}" rpy="0 0 0"/><mass value="{d["mass"]}"/>'
          f'<inertia ixx="{ix:.6g}" ixy="0" ixz="0" iyy="{iy:.6g}" iyz="0" izz="{iz:.6g}"/></inertial>',
          f'    <visual><origin xyz="{f(d["center"])}" rpy="0 0 0"/>{geo}</visual>',
          f'    <collision><origin xyz="{f(d["center"])}" rpy="0 0 0"/>{geo}</collision>',
          '  </link>']
for j in joints:
    o.append(f'  <joint name="{j["name"]}" type="{j["type"]}">')
    o.append(f'    <parent link="{j["parent"]}"/><child link="{j["child"]}"/>')
    o.append(f'    <origin xyz="{f(j["xyz"])}" rpy="0 0 0"/>')
    if j["type"] == "revolute":
        o.append(f'    <axis xyz="{f(j["axis"])}"/>')
        o.append(f'    <limit lower="{j["limit"][0]}" upper="{j["limit"][1]}" effort="3.0" velocity="5.0"/>')
        o.append('    <dynamics damping="0.05" friction="0.02"/>')
    o.append('  </joint>')
o.append('</robot>')
(ROOT/"urdf/bhiv_humanoid_foundation.urdf").write_text("\n".join(o)+"\n")
(ROOT/"config/model_params.json").write_text(json.dumps(dict(links=links, joints=joints), indent=1))

children = {}
for j in joints: children.setdefault(j["parent"], []).append(j)
tree = []
def walk(link, depth, via=None):
    tag = f"  <- {via['name']} [{via['type']}{', axis '+f(via['axis']) if via['axis'] else ''}]" if via else ""
    tree.append("    "*depth + ("└─ " if depth else "") + link + tag)
    for c in children.get(link, []): walk(c["child"], depth+1, c)
walk("base_link", 0)
(ROOT/"docs/joint_hierarchy_tree.txt").write_text("\n".join(tree)+"\n")

AX = {YAW:"Z (yaw)", PITCH:"Y (pitch)", ROLL:"X (roll)"}
rows = ["| # | Servo ch. (placeholder) | Joint | Parent → Child | Axis | Limits (rad) | Body region |","|---|---|---|---|---|---|---|"]
k = 0; groups = {}
for j in joints:
    if j["type"]=="revolute":
        k += 1; groups[j["group"]] = groups.get(j["group"],0)+1
        rows.append(f'| {k} | {j["servo"]} | `{j["name"]}` | {j["parent"]} → {j["child"]} | {AX[j["axis"]]} | {j["limit"][0]} … {j["limit"][1]} | {j["group"]} |')
summ = ["| Region | DOF |","|---|---|"] + [f"| {g} | {c} |" for g,c in groups.items()] + [f"| **Total** | **{sum(groups.values())}** |"]
(ROOT/"docs/03_dof_map.md").write_text("# DOF Map (ESTIMATED — see 06_assumptions_and_missing_info.md)\n\n"+"\n".join(summ)+"\n\n## Per-joint\n\n"+"\n".join(rows)+"\n")

jm = ["# Joint Map\n","Joint origins are in the PARENT link frame at zero pose (metres).\n","## Hierarchy\n","```",*tree,"```\n","## Joint origins\n","| Joint | Type | Parent | xyz (m) |","|---|---|---|---|"]
for j in joints: jm.append(f'| `{j["name"]}` | {j["type"]} | {j["parent"]} | {f(j["xyz"])} |')
(ROOT/"docs/04_joint_map.md").write_text("\n".join(jm)+"\n")

import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
world = {"base_link": (0,0,0.55)}
for j in joints:
    p = world[j["parent"]]; world[j["child"]] = tuple(p[i]+j["xyz"][i] for i in range(3))
COL = dict(hip="#888",waist="#c44",torso="#4a7",head="#59d",arm="#d90",forearm="#e70",hand="#a5a",leg="#27a",foot="#555")
fig, axs = plt.subplots(1,2,figsize=(11,7))
for ax,(title,ia,ib) in zip(axs,(("Front view (Y–Z)",1,2),("Side view (X–Z)",0,2))):
    for name,d in links.items():
        w = world[name]; c = [w[i]+d["center"][i] for i in range(3)]
        sa, sb = d["size"][ia], d["size"][ib]
        ax.add_patch(Rectangle((c[ia]-sa/2, c[ib]-sb/2), sa, sb, fc=COL[GROUP[name]], ec="k", lw=.4, alpha=.75))
    for j in joints:
        if j["type"]=="revolute":
            w = world[j["child"]]; ax.plot(w[ia], w[ib], "wo", mec="k", ms=4)
    ax.set_aspect("equal"); ax.set_title(title); ax.set_xlim((-.4,.4) if ia==1 else (-.2,.3)); ax.set_ylim(-.02,1.05); ax.grid(alpha=.3)
fig.suptitle("BHIV Humanoid foundation model — zero pose (PLACEHOLDER dims, 23 DOF; white dots = joints)")
plt.tight_layout(); plt.savefig(ROOT/"evidence_packet/screenshots/kinematic_preview_front_side.png", dpi=110)
print("links",len(links),"joints",len(joints),"DOF",sum(groups.values()))
