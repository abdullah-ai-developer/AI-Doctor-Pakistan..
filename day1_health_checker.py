# AI DOCTOR Day 1 - Health Risk Checker
# Made by: Abdullah - Future AI Doctor
print("=== AI DOCTOR - Health Risk Checker ===")
print("Made by: Abdullah - Future AI Doctor 👨‍⚕️🤖\n")

age = int(input("Umar batao: "))
fever = input("Fever hai? (han/nahi): ").lower()
bp = int(input("Blood Pressure batao (jaise 120): "))

risk = 0

if fever == "han":
    risk += 30
    print("-> Fever risk: Zyada")

if bp > 140 or bp < 90:
    risk += 40
    print("-> BP risk: Zyada")
else:
    print("-> BP Normal")

if age > 50:
    risk += 30
    print("-> Age risk: Zyada")

print("\n--- AI REPORT ---")
print(f"Total Risk Score: {risk}/100")

if risk >= 70:
    print("RESULT: 🔴 High Risk - Foran Doctor ko dikhao")
elif risk >= 40:
    print("RESULT: 🟡 Medium Risk - Kal Doctor ko check karao")
else:
    print("RESULT: 🟢 Low Risk - Ghar par rest karo")

print("\nYe tumne banaya hai - Yehi AI Doctor ka kaam hai!")
