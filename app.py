from flask import Flask, render_template, request, jsonify, current_app
import subprocess
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    print("hello 1")
    query = request.form.get('query')
    result = run_query(query)
    return render_template('results.html', result=result)

def run_query(query):
    try:
        query_url = 'http://127.0.0.1:5000/query' 
        print("hello 2")

        data = {'query': query}

        response = requests.post(query_url, data=data)

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)