def recommend_outfit(data):
    face = data.get("face_shape")
    body = data.get("body_type")
    skin = data.get("skin_tone")
    occasion = data.get("occasion")

    outfits = []

    if body == "Athletic" and occasion == "Formal":
        outfits.append("Blazer with Slim Fit Trousers")

    if skin == "Dark":
        outfits.append("Bright pastel colors")

    return {
        "recommended_outfits": outfits,
        "accessories": ["Watch", "Leather Shoes"]
    }
