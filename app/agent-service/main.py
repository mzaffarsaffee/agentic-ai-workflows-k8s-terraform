from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    result = f"Agent processed: {data.get('input', '')}"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
