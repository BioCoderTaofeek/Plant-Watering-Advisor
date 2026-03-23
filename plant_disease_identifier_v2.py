symptoms = input("Enter symptoms (separate with commas): ").lower()
symptom_list = symptoms.split(",")

scores = {
    "Powdery Mildew": 0,
    "Blight": 0,
    "Anthracnose": 0,
    "Canker": 0,
    "Chlorosis": 0
}

for s in symptom_list:
    s = s.strip()

    if "white" in s or "powder" in s:
        scores["Powdery Mildew"] += 1

    if "wilting" in s or "brown" in s:
        scores["Blight"] += 1

    if "dark" in s or "lesion" in s:
        scores["Anthracnose"] += 1

    if "dead" in s or "sunken" in s:
        scores["Canker"] += 1

    if "yellow" in s:
        scores["Chlorosis"] += 1


best_match = max(scores, key=scores.get)

if scores[best_match] > 0:
    print("Most likely disease:", best_match)
else:
    print("Disease not identified ❓")
    print("\nAll scores:", scores)