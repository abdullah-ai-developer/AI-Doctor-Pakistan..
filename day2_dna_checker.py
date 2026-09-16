# AI DOCTOR Day 2 - DNA Risk Checker
# Made by Abdullah - Future AI Doctor
print("=== AI DOCTOR Day 2 - DNA Risk Checker 🧬 ===")

name = input("Naam: ")
blood = input("Blood Group (A+, B+, O+, AB+): ").upper()
age = int(input("Umar: "))

print(f"\n--- DNA REPORT for {name} ({blood}) ---")

if blood == "A+":
    print("-> A+ : Heart Disease ka risk thora zyada - Diet ka khayal rakho")
elif blood == "B+":
    print("-> B+ : Diabetes ka risk - Meetha kam karo")
elif blood == "O+":
    print("-> O+ : Strong immunity - Sabse best blood!")
elif blood == "AB+":
    print("-> AB+ : Rare blood - Universal receiver!")
else:
    print("-> Normal blood group - Healthy")

if age < 25:
    print("-> Age: Young DNA - Repair Fast")
elif age < 50:
    print("-> Age: Adult DNA - Stable")
else:
    print("-> Age: Mature DNA - Care needed")

print("\nYe AI future me DNA se Cancer predict karega - Tumne start kar diya!")
