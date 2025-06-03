# 🔐 Chat-RSA-WebHook

Este projeto é um sistema de troca de mensagens seguras usando criptografia RSA e comunicação via WebHook, implementado em Python com Flask. Ele permite que duas aplicações conversem criptografando mensagens com chaves públicas trocadas dinamicamente.

## 🚀 Funcionalidades

- Geração manual de chaves RSA (com primos simples)
- Troca de chaves públicas entre cliente e servidor via WebHook
- Envio e recebimento de mensagens criptografadas
- Threads para manter o Flask ativo enquanto o chat roda no terminal
- Possível extensão para assinatura digital e verificação de integridade

## 🛠 Tecnologias utilizadas

- Python 3.x
- Flask
- Requests
- Criptografia RSA (implementação própria, sem bibliotecas externas)

## 📁 Estrutura do Projeto

```bash
Chat-RSA-WebHook/
│
├── app_a.py               # Aplicação A (ex: servidor)
├── app_b.py               # Aplicação B (ex: cliente)
├── rsa_utils.py           # Funções para geração de chaves, criptografia e descriptografia
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação do projeto
```

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/OtavioAugustoo/Chat-RSA-WebHook.git
cd Chat-RSA-WebHook
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute as duas aplicações (em terminais separados)

Terminal 1:
```bash
python app_a.py
```

Terminal 2:
```bash
python app_b.py
```

## 🔐 Exemplo de chave gerada

```text
===== GERANDO CHAVES RSA =====
🟡 p:   199
🟡 q:   173
🔢 n:   34427
🧮 φ:   34056
🔐 e:   755
🔓 d:   15755
================================

🔐 Chave pública do servidor: (755, 34427)
🔐 Chave pública do cliente:  (1019, 28513)
```

## 📌 Observações

- O projeto usa primos pequenos para facilitar a visualização e entendimento do processo RSA.
- Em uma aplicação real, recomenda-se usar bibliotecas como `cryptography` ou `PyCryptodome` com primos grandes para segurança adequada.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias ou correções!

---

Feito com 💻 por [Otavio Augusto](https://github.com/OtavioAugustoo)