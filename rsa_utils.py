
import random
from math import gcd

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gerar_primo():
    while True:
        p = random.randint(100, 300)
        if eh_primo(p):
            return p

def gerar_chaves(nome=""):
    print(f"===== GERANDO CHAVES RSA {nome.upper()} =====")
    p = gerar_primo()
    q = gerar_primo()
    while p == q:
        q = gerar_primo()

    n = p * q
    totiente = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, totiente) != 1:
        e = random.randint(2, totiente - 1)

    d = pow(e, -1, totiente)

    print(f"🟡 p:   {p}")
    print(f"🟡 q:   {q}")
    print(f"🔢 n:   {n}")
    print(f"🧮 φ:   {totiente}")
    print(f"🔐 e:   {e}")
    print(f"🔓 d:   {d}")
    print("================================")
    print(f"🔐 Chave pública do {nome.lower()}: ({e}, {n})")
    print(f"🔐 Chave privada do {nome.lower()}: ({d}, {n})\n")
    return ((e, n), (d, n))

def criptografar(mensagem, chave_publica):
    e, n = chave_publica
    return [pow(ord(c), e, n) for c in mensagem]

def descriptografar(mensagem_codificada, chave_privada):
    d, n = chave_privada
    return ''.join([chr(pow(c, d, n)) for c in mensagem_codificada])
