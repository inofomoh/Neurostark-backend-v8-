from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ NeuroStark Backend is running!"

@app.route('/generate-film', methods=['POST'])
def generate_film():
    data = request.json
    script = data.get("script", "Default script")
    genre = data.get("genre", "Drama")
    user = data.get("user_name", "User")

    return jsonify({
        "status": "success",
        "message": f"Film generated for {user} in genre {genre}.",
        "download_url": "https://neurostark-backend.onrender.com/download/film.mp4"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
