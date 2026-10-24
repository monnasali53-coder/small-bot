import json
import os

MEMORY_FILE = "memory.json"
PREDICTION_FILE = "latest_prediction.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"history": [], "patterns": {}}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def calculate_deep_prediction(new_result):
    """
    new_result format: {"period": "101", "number": 7, "color": "Green", "size": "Big"}
    """
    memory = load_memory()
    history = memory["history"]
    
    # नया डेटा जोड़ें
    history.append(new_result)
    if len(history) > 100:  # आखिरी 100 राउंड याद रखेगा
        history.pop(0)
    
    memory["history"] = history
    save_memory(memory)
    
    # डीप प्रोबेबिलिटी कैलकुलेशन (लॉजिक)
    total_rounds = len(history)
    if total_rounds < 3:
        big_pct, small_pct = 50.0, 50.0
    else:
        big_count = sum(1 for item in history if item["size"] == "Big")
        big_pct = round((big_count / total_rounds) * 100, 2)
        small_pct = round(100.0 - big_pct, 2)
        
        # ट्रेंड के आधार पर परसेंटेज एडजस्टमेंट
        if history[-1]["size"] == "Big" and history[-2]["size"] == "Big":
            big_pct = min(90.0, big_pct + 5.0)
            small_pct = round(100.0 - big_pct, 2)

    # फाइनल प्रेडिक्शन आउटपुट तैयार करना
    prediction_data = {
        "big_percentage": big_pct,
        "small_percentage": small_pct,
        "top_color": "Green" if big_pct > 50 else "Red",
        "top_number": new_result.get("number", 5)
    }
    
    with open(PREDICTION_FILE, "w") as f:
        json.dump(prediction_data, f, indent=4)
        
    print("Deep Learning Analysis Updated Successfully!")

if __name__ == "__main__":
    sample_input = {"period": "101", "number": 7, "color": "Green", "size": "Big"}
    calculate_deep_prediction(sample_input)
