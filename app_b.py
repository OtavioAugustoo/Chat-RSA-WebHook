
from flask import Flask, request, jsonify
from rsa_utils import gerar_chaves, criptografar, descriptografar
import requests
import time

app = Flask(__name__)

publica_B, privada_B = gerar_chaves()
publica_A = None

@app.route('/receive_key', methods=['POST'])
def receber_chave():
    global publica_A
    data = request.get_json()
    publica_A = tuple(data['publica'])
    print(" Chave pública de A recebida!")
    return jsonify({"status": "Chave de A recebida com sucesso!"})

@app.route('/receive_msg', methods=['POST'])
def receber_mensagem():
    data = request.get_json()
    criptografada = data['mensagem']
    mensagem = descriptografar(criptografada, privada_B)
    print(f" Mensagem recebida de A: {mensagem}")
    return jsonify({"status": "Mensagem recebida"})

def enviar_chave():
    url = 'http://localhost:5000/receive_key'
    tentativas = 0
    while tentativas < 10:
        try:
            response = requests.post(url, json={"publica": list(publica_B)}, timeout=2)
            print(" Chave pública enviada para A com sucesso.")
            return
        except requests.exceptions.ConnectionError:
            tentativas += 1
            print(f" Tentando conectar ao App A... (tentativa {tentativas})")
            time.sleep(2)
    print(" Falha ao conectar com App A após várias tentativas.")

def enviar_mensagem(mensagem):
    if not publica_A:
        print(" Chave pública de A ainda não recebida.")
        return
    criptografada = criptografar(mensagem, publica_A)
    url = 'http://localhost:5000/receive_msg'
    print("Mensagem criptografada:", criptografada)
    try:
        requests.post(url, json={"mensagem": criptografada})
        print(" Mensagem enviada para A.")
    except:
        print(" Erro ao enviar mensagem.")

if __name__ == '__main__':
    from threading import Thread

    def iniciar_flask():
        app.run(port=5001)

    flask_thread = Thread(target=iniciar_flask)
    flask_thread.start()

    time.sleep(2)
    enviar_chave()

    while True:
        msg = input("Você (B): ")
        enviar_mensagem(msg)
