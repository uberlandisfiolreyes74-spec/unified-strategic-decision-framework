import sys
sys.path.append('../src')

from integration import unified_decision

structural = {
    'P_E': 0.85, 'P_R': 0.90, 'P_L': 0.80,
    'P_S': 0.88, 'P_M': 0.75
}
beliefs = {
    'C': 0.80, 'I': 0.75, 'S': 0.68, 'A_V': 0.65
}
bio = {
    'B_R': 0.72, 'B_E': 0.65, 'B_C': 0.60
}
fd = 0.82

options = [
    {'name': '10K Marines', 'opt': 0.45, 'base': 0.052, 'pess': -0.55},
    {'name': '5K Marines + Negotiation', 'opt': 0.25, 'base': 0.138, 'pess': -0.05},
    {'name': 'No Deployment', 'opt': 0.05, 'base': -0.26, 'pess': -0.50}
]

ii, risk, ranked = unified_decision(structural, beliefs, bio, fd, options)

print(f"II Score: {ii:.3f} - Risk Level: {risk}")
print("\nRanked Options:")
for i, opt in enumerate(ranked):
    print(f"{i+1}. {opt['name']}: Score={opt['Score']:.3f}, E[V]={opt['E[V]']:.2%}")
