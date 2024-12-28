from flask import Flask, request, jsonify
import serpapi
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)

# Defina sua chave de API
API_KEY = "c48af74105d1508eae39421d4a07171ad1aa2083274620def0308e930506ce21"

@app.route('/search', methods=['GET'])
def search():
    try: 
        searching = request.args.get('query')
        if not searching:
            return jsonify({"status": 400, "message": "O parâmetro 'query' é obrigatório."}), 400
        
        client = serpapi.Client(api_key=API_KEY)

        results = client.search({
            'engine': 'google_shopping',
            'type': 'search',
            'q': f"{searching} 'Angola'",
            'll': '@-8.914212,13.320480,3z',
        })

        return jsonify(results.get("shopping_results", []))
 
    except Exception as e:
        return jsonify({"status": 500, "message": f"Ocorreu um erro: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use a variável de ambiente 'PORT' ou 5000
    app.run(host='0.0.0.0', port=port, debug=True)
