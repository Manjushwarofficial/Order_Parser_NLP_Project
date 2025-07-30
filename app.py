from flask import Flask, request, jsonify
import re
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Sample food keywords to match from voice/text
FOOD_ITEMS = ["paratha", "lassi", "samosa", "paneer", "rice", "roti", "dal", "chole", "burger", "pizza","Balu shahi", "Boondi", "Gajar ka halwa", "Ghevar", "Gulab jamun","naan", "Imarti", "Jalebi", "Kaju katli", "Kalakand",
    "Kheer", "Laddu", "Lassi", "Nankhatai", "Petha", "Phirni", "Rabri", "Sheera", "Singori", "Sohan halwa",
    "Sohan papdi", "Chhena jalebi", "Chhena kheeri", "Chhena poda", "Cham cham", "Kheer sagar", "Ledikeni",
    "Lyangcha", "Malapua", "Mihidana", "Misti doi", "Pantua", "Pithe", "Rasabali", "Ras malai", "Rasgulla",
    "Sandesh", "Adhirasam", "Ariselu", "Bandar laddu", "Chikki", "Dharwad pedha", "Double ka meetha", "Gavvalu",
    "Kakinada khaja", "Kuzhi paniyaram", "Mysore pak", "Obbattu holige", "Palathalikalu", "Poornalu", "Pongal",
    "Pootharekulu", "Qubani ka meetha", "Sheer korma", "Unni Appam", "Kajjikaya", "Anarsa", "Basundi", "Dhondas",
    "Doodhpak", "Mahim halwa", "Modak", "Shankarpali", "Shrikhand", "Sutar feni", "Maach Jhol", "Pork Bharta",
    "Chak Hao Kheer", "Galho", "Aloo gobi", "Aloo tikki", "Aloo matar", "Aloo methi", "Aloo shimla mirch",
    "Bhatura", "Bhindi masala", "Biryani", "Butter chicken", "Chana masala", "Chapati", "Chicken razala",
    "Chicken Tikka masala", "Chicken Tikka", "Chole bhature", "Daal baati churma", "Daal puri", "Dal makhani",
    "Dal tadka", "Dum aloo", "Poha", "Fara", "Kachori", "Kadai paneer", "Kadhi pakoda", "Karela bharta",
    "Khichdi", "Kofta", "Kulfi falooda", "Lauki ke kofte", "Lauki ki subji", "Litti chokha",
    "Makki di roti sarson da saag", "Misi roti", "Mushroom do pyaza", "Mushroom matar", "Naan", "Navrattan korma",
    "Palak paneer", "Paneer butter masala", "Paneer tikka masala", "Pani puri", "Panjeeri", "Papad", "Paratha",
    "Pattor", "Pindi chana", "Rajma chaval", "Rongi", "Samosa", "Sattu ki roti", "Shahi paneer", "Shahi tukra",
    "Vegetable jalfrezi", "Tandoori Chicken", "Tandoori Fish Tikka", "Attu", "Avial", "Bisi bele bath",
    "Currivepillai sadam", "Dosa", "Idiappam", "Idli", "Kanji", "Kaara kozhambu", "Keerai kootu", "Keerai masiyal",
    "Keerai sadam", "Keerai poriyal", "Beef Fry", "Kootu", "Kos kootu", "Koshambri", "Kothamali sadam",
    "Kuzhakkattai", "Kuzhambu", "Masala Dosa", "Pachadi", "Paniyaram", "Papadum", "Paravannam", "Payasam",
    "Paruppu sadam", "Pesarattu", "Poriyal", "Puli sadam", "Rasam", "Puttu", "Sambar", "Sandige", "Sevai",
    "Thayir sadam", "Theeyal", "Uttapam", "Vada", "Chicken Varuval", "Upma", "Amti", "Zunka", "Kolim Jawla",
    "Saath", "Bajri no rotlo", "Coconut vadi", "Bhakri", "Bombil fry", "Chakali", "Chevdo", "Chorafali",
    "Copra paak", "Daal Dhokli", "Kutchi dabeli", "Dahi vada", "Dalithoy", "Dhokla", "Dudhi halwa", "Gatta curry",
    "Gud papdi", "Ghooghra", "Handwo", "Halvasan", "Jeera Aloo", "Kansar", "Keri no ras", "Khakhra", "Khandvi",
    "Kombdi vade", "Laapsi", "Koshimbir", "Methi na Gota", "Mohanthal", "Muthiya", "Patra", "Pav Bhaji",
    "Puri Bhaji", "Sabudana Khichadi", "Sev khamani", "Sev tameta", "Namakpara", "Sukhdi", "Surnoli", "Thalipeeth",
    "Undhiyu", "Veg Kolhapuri", "Vindaloo", "Lilva Kachori", "Mag Dhokli", "Khichu", "Thepla", "Farsi Puri",
    "Khaman", "Turiya Patra Vatana sabji", "Churma Ladoo", "Cheera Doi", "Gheela Pitha", "Khar", "Kumol Sawul",
    "Luchi", "Alu Pitika", "Masor tenga", "Bengena Pitika", "Bilahi Maas", "Black rice", "Bora Sawul", "Brown Rice",
    "Chingri malai curry", "Goja", "Hando Guri", "Haq Maas", "Chingri Bhape", "Kabiraji", "Khorisa", "Koldil Chicken",
    "Konir Dom", "Koldil Duck", "Masor Koni", "Mishti Chholar Dal", "Pakhala", "Pani Pitha", "Payokh",
    "Prawn malai curry", "Red Rice", "Shukto", "Til Pitha", "Bebinca", "Shufta", "Mawa Bati", "Pinaca"]

def extract_items(raw_text):
    raw_text = raw_text.lower()
    structured_order = []

    for item in FOOD_ITEMS:
        # Match number before or after food item
        patterns = [
            rf'(\d+)\s+{item}',       # e.g. "2 samosas"
            rf'{item}\s+(\d+)',       # e.g. "samosas 2"
            rf'{item}'                # just the item (default quantity 1)
        ]
        for pattern in patterns:
            match = re.search(pattern, raw_text)
            if match:
                qty = 1
                if match.groups() and match.group(1) and match.group(1).isdigit():
                    qty = int(match.group(1))
                structured_order.append({"item": item.capitalize(), "quantity": qty})
                break  # Avoid duplicate matches

    return structured_order

@app.route('/submit-order', methods=['POST'])
def submit_order():
    data = request.get_json()
    raw_input = data.get('order')

    if not raw_input:
        return jsonify({"message": "No order received."}), 400

    structured = extract_items(" ".join(raw_input))  # join array to string
    with open('food.json', 'w') as f:
        json.dump({'order': structured}, f, indent=2)

    return jsonify({"message": "Structured order saved!", "structured_order": structured})

@app.route('/get-order', methods=['GET'])
def get_order():
    try:
        with open('food.json') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"order": []})

if __name__ == '__main__':
    app.run(debug=True)
