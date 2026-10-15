from flask import Flask, jsonify
import scratchattach as scratch3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows TurboWarp/CodeTorch to read this server without CORS blocks

STUDIO_ID = "52003727"  # Your studio ID

@app.route('/')
def get_curators():
    try:
        # Fetches live data directly from Scratch's backend system
        studio = scratch3.get_studio(STUDIO_ID)
        curators = studio.curators(limit=40, offset=0) # Pulls live curators
        
        # Extract just the usernames into a clean list
        usernames = [c.username for c in curators]
        
        return jsonify({
            "success": True,
            "total": len(usernames),
            "curators": usernames
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)main.py
