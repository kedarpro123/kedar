from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple rule-based skincare chatbot
def get_response(user_input: str) -> str:
    user_input = user_input.lower()

    if "acne" in user_input:
        return "For acne, use a gentle cleanser and products with salicylic acid or benzoyl peroxide."
    elif "dry skin" in user_input:
        return "Hydrate with hyaluronic acid and use a rich moisturizer."
    elif "oily skin" in user_input:
        return "Try oil-free moisturizers and cleansers with niacinamide."
    elif "sunscreen" in user_input:
        return "Always use SPF 30+ daily, even indoors."
    elif "routine" in user_input:
        return "A basic routine: Cleanser → Moisturizer → Sunscreen (AM), Cleanser → Treatment → Moisturizer (PM)."
    else:
        return "I recommend consulting a dermatologist for personalized skincare advice."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("messages", [""])[0]  # frontend sends messages list
    system_prompt = data.get("system_prompt", "")
    model_name = data.get("model_name", "")

    # For now, ignore model_name/system_prompt and use rule-based response
    reply = get_response(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
