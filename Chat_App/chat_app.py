import socket
import threading
from datetime import datetime
from colorama import init, Fore
init(autoreset=True)
emojis = {
    ":smile:": "😄",
    ":sad:": "😢",
    ":heart:": "❤️",
    ":thumbsup:": "👍",
    ":fire:": "🔥",
    ":laugh:": "😂"
}
def replace_emojis(message):
    for code, emoji in emojis.items():
        message = message.replace(code, emoji)
    return message
def save_message(message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        file.write(f"{timestamp} {message}\n")
def start_server():
    host = '127.0.0.1'
    port = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    clients = []
    names = []
    def broadcast(msg, sender=None):
        for client in clients:
            if client != sender:
                client.send(msg)
    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)
                decoded = message.decode('utf-8')
                print(Fore.YELLOW + decoded)
                save_message(decoded)
                broadcast(message, sender=client)
            except:
                idx = clients.index(client)
                name = names[idx]
                broadcast(f"{name} left the chat.".encode('utf-8'))
                clients.remove(client)
                names.remove(name)
                client.close()
                break
    print(Fore.GREEN + "Server is running...")
    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")
        client.send("NAME".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        broadcast(f"{name} joined the chat!".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
def start_client():
    host = '127.0.0.1'
    port = 5555
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    name = input("Enter the name: ")
    def receive():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "NAME":
                    client.send(name.encode('utf-8'))
                else:
                    print(Fore.CYAN + message)
            except:
                print(Fore.RED + "Connection closed.")
                client.close()
                break
    def write():
        while True:
            text = input("")
            text = replace_emojis(text)
            full_msg = f"{name}: {text}"
            client.send(full_msg.encode('utf-8'))
    threading.Thread(target=receive).start()
    threading.Thread(target=write).start()
if __name__ == "__main__":
    print("Welcome to Python Chat Application !!")
    print("Type 'server' to start the server or 'client' to join as a user.")
    mode = input("Please choose the Mode (server/client): ").lower()
    if mode == 'server':
        start_server()
    elif mode == 'client':
        start_client()
    else:
        print("Invalid option.")
