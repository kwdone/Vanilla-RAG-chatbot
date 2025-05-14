def clean_answer(text):
    text = text.strip().replace("\n", " ").replace("  ", " ")

    generic_phrases = [
        "thank you for your time", "please feel free to contact me",
        "thank you!", "thanks!", "i'm looking for"
    ]
    for phrase in generic_phrases:
        text = text.replace(phrase, "")

    text = text.replace("calories", "kcal").replace("protein", "g protein")
    text = text.replace("carbohydrates", "carbs").replace("fats", "g fat")
    text = text.replace("liters", "L").replace("litres", "L")

    sections = text.split("\n")
    formatted_text = "\n\n".join([section.strip() for section in sections if section.strip()])

    return formatted_text.strip('.') + '.'
