import json
import random

def calculate_predictions():
    # यहाँ पर गेम के रिजल्ट्स के हिसाब से लॉजिक या रैंडम/ऐनलाइज्ड डेटा बनता है
    big_pct = round(random.uniform(40.0, 60.0), 1)
    small_pct = round(100.0 - big_pct, 1)
    
    colors = ["Green", "Red", "Violet"]
    top_color = random.choice(colors)
    top_number = random.randint(0, 9)
    
    data = {
        "big_percentage": big_pct,
        "small_percentage": small_pct,
        "top_color": top_color,
        "top_number": top_number
    }
    
    # latest_prediction.json फाइल को अपडेट करना
    with open("latest_prediction.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    calculate_predictions()
