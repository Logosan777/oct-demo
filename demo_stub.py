# demo_stub.py
# OCT-CANCER v3.0 — Simulated Therapeutic Planning Engine (Lite)

print("OCT-CANCER v3.0 Demo: μ/Δμ/τ Planning\n")

# Simulated patient structure
S = {
    "TP53": "inactive",
    "BAX": "low",
    "VEGF": "high"
}

Q = [
    "TP53 active → BAX upregulated",
    "VEGF ≤ medium"
]

print("Structure S:")
for k, v in S.items():
    print(f"  {k}: {v}")

print("\nEvaluating conflict with Q...")
mu = 6.2
print(f"μ(S, Q) = {mu}")

# Simulated transformations
T1 = {"apply": "activate TP53"}
T2 = {"apply": "inhibit VEGF"}

print("\nTrying T1:", T1)
mu_T1 = 3.1
tau_T1 = 0.4
print(f"  → μ = {mu_T1}, Δμ = {mu - mu_T1}, τ = {tau_T1}")

print("\nTrying T2:", T2)
mu_T2 = 2.9
tau_T2 = 1.1
print(f"  → μ = {mu_T2}, Δμ = {mu - mu_T2}, τ = {tau_T2} (REJECTED, τ > ε)")

print("\nSelected plan: T1")
print("Therapeutic gain Δμ = 3.1 (ACCEPTED)")
