from flask import Flask, jsonify # type: ignore
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido a mi aplicación web'

@app.route('/ejecutar-script')
def ejecutar_script():
    try:
        resultado = subprocess.check_output(['python', 'simulacion_json.py'], stderr=subprocess.STDOUT)
        return jsonify({'resultado': resultado.decode('utf-8')})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)
