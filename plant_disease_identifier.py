symptom = input("Enter plant symptom: ").lower()

if "white powder" in symptom:
    print("Disease: Powdery Mildew")
    print("Cause: Fungi (Erysiphe spp.)")

elif "wilting" in symptom or "brown leaves" in symptom:
    print("Disease: Blight")
    print("Cause: Phytophthora infestans")

elif "dark spots" in symptom or "sunken lesions" in symptom:
    print("Disease: Anthracnose")
    print("Cause: Colletotrichum spp.")

elif "dead stem" in symptom or "sunken stem" in symptom:
    print("Disease: Canker")
    print("Cause: Coryneum spp.")

elif "swollen roots" in symptom:
    print("Disease: Clubroot")
    print("Cause: Plasmodiophora brassicae")

elif "seedling collapse" in symptom:
    print("Disease: Damping-off")
    print("Cause: Pythium spp.")

elif "yellow leaves and wilting" in symptom:
    print("Disease: Dutch Elm Disease")
    print("Cause: Ophiostoma ulmi")

elif "black coating" in symptom:
    print("Disease: Sooty Mold")
    print("Cause: Saprophytic fungi")

elif "leaf curl" in symptom:
    print("Disease: Peach Leaf Curl")
    print("Cause: Taphrina deformans")

elif "yellow leaves" in symptom:
    print("Condition: Chlorosis")
    print("Cause: Nutrient deficiency (Nitrogen/Iron)")

elif "black spots" in symptom:
    print("Disease: Tar Spot")
    print("Cause: Rhytisma spp.")

elif "brown patches" in symptom:
    print("Disease: Brown Patch")
    print("Cause: Rhizoctonia solani")

elif "rust spots" in symptom:
    print("Disease: Rust")
    print("Cause: Puccinia spp.")

elif "dark grains" in symptom:
    print("Disease: Ergot")
    print("Cause: Claviceps purpurea")

elif "blossom end rot" in symptom:
    print("Condition: Physiological Disorder")
    print("Cause: Calcium deficiency")

else:
    print("Disease not identified ❓ Try describing symptoms better.")