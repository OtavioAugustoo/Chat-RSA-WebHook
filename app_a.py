
from flask import Flask, request, jsonify
from rsa_utils import gerar_chaves, criptografar, descriptografar
import requests
import time

app = Flask(__name__)

publica_A, privada_A = gerar_chaves()
publica_B = None

@app.route('/receive_key', methods=['POST'])
def receber_chave():
    global publica_B
    data = request.get_json()
    publica_B = tuple(data['publica'])
    print("Chave pública de B recebida!")
    return jsonify({"status": "Chave de B recebida com sucesso!"})

@app.route('/receive_msg', methods=['POST'])
def receber_mensagem():
    data = request.get_json()
    criptografada = data['mensagem']
    mensagem = descriptografar(criptografada, privada_A)
    print(f" Mensagem recebida de B: {mensagem}")
    return jsonify({"status": "Mensagem recebida"})

def enviar_chave():
    url = 'http://localhost:5001/receive_key'
    tentativas = 0
    while tentativas < 10:
        try:
            response = requests.post(url, json={"publica": list(publica_A)}, timeout=2)
            print(" Chave pública enviada para B com sucesso.")
            return
        except requests.exceptions.ConnectionError:
            tentativas += 1
            print(f" Tentando conectar ao App B... (tentativa {tentativas})")
            time.sleep(2)
    print(" Falha ao conectar com App B após várias tentativas.")

def enviar_mensagem(mensagem):
    if not publica_B:
        print(" Chave pública de B ainda não recebida.")
        return
    criptografada = criptografar(mensagem, publica_B)
    url = 'http://localhost:5001/receive_msg'
    print("Mensagem criptografada:", criptografada)
    try:
        requests.post(url, json={"mensagem": criptografada})
        print(" Mensagem enviada para B.")
    except:
        print("Erro ao enviar mensagem.")

if __name__ == '__main__':
    from threading import Thread

    def iniciar_flask():
        app.run(port=5000)

    flask_thread = Thread(target=iniciar_flask)
    flask_thread.start()

    time.sleep(2)
    enviar_chave()

    while True:
        msg = input("Você (A): ")
        enviar_mensagem(msg)
