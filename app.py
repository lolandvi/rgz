import argparse
import logging
from flask import Flask, request, jsonify, render_template
from collections import Counter
import re
import socket


app = Flask(__name__)

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/', methods=['GET'])
def serve_index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data['text']
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        total_words = len(words)
        top_words = word_counts.most_common(10)
        server_port = request.environ.get('SERVER_PORT') #получаем порт из окружения
        server_name = socket.gethostname() #получаем имя хоста

        result = {
            'total_words': total_words,
            'top_words': top_words,
            'server_port': server_port,
            'server_name': server_name
        }
        return jsonify(result)
    except KeyError:
        return jsonify({'error': 'Missing "text" key in JSON'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    app.run(port=args.port)


