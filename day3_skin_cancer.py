# AI DOCTOR Day 3 - Skin Cancer Detector 🔬
# Made by Abdullah - Used in Toronto Hospital AI
print("=== AI DOCTOR Day 3 - Skin Cancer Detector 🔬 ===")
print("Made by: Abdullah - Future AI Doctor\n")

color = input("Daag ka rang (kala/brown/red/normal): ").lower()
size = int(input("Daag ka size mm me (jaise 2, 5, 10): "))
itch = input("Kharish hai? (han/nahi): ").lower()
days = int(input("Kitne din se hai?: "))

print("\n--- AI SCAN HO RAHA HAI... ---")
risk = 0

if color == "kala":
    risk += 50
    print("-> Kala rang = Danger +50")
elif color == "red" or color == "brown":
    risk += 25
    print(f"-> {color} rang = Risk +25")
else:
    print("-> Normal rang = Safe")

if size > 6:
    risk += 30
    print(f"-> Size {size}mm > 6mm = Risk +30")
else:
    print(f"-> Size {size}mm = Normal")

if itch == "han":
    risk += 10
    print("-> Kharish = +10")

if days > 7:
    risk += 10
    print(f"-> {days} din purana = +10")

print("\n--- SKIN AI REPORT ---")
print(f"Risk Score: {risk}/100")

if risk >= 70:
    print("🔴 HIGH RISK - FORAN Skin Doctor ko dikhao!")
elif risk >= 40:
    print("🟡 MEDIUM RISK - 2-3 din me Doctor ko dikhao")
else:
    print("🟢 LOW RISK - Normal hai, clean rakho")

print("\nYehi AI Toronto Hospital me use hota hai!")
