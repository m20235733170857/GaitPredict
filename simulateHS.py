import socket
import keyboard  # 需要安装 keyboard 库，用于检测键盘按键

# 定义Unity服务器的IP地址和端口号
unity_server_address = ('localhost', 12345)  # 这里的IP地址和端口号应该与Unity服务器的设置相匹配

# 创建一个TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到Unity服务器
client_socket.connect(unity_server_address)

# 发送信号到Unity服务器
def send_signal(signal):
    message = signal.encode()  # 将信号转换为字节串
    client_socket.sendall(message)  # 发送信号
    print(f"Sent: {signal}")

# 监听键盘按键
try:
    print("Listening for key presses (Press 'ESC' to exit)...")
    while True:
        # 当按下D键时，发送"0,1"
        if keyboard.is_pressed('d'):
            send_signal("0,1")
            send_signal("0,0")
            while keyboard.is_pressed('d'):  # 避免重复发送信号
                pass
        
        # 当按下A键时，发送"1,0"
        if keyboard.is_pressed('a'):
            send_signal("1,0")
            send_signal("0,0")
            while keyboard.is_pressed('a'):  # 避免重复发送信号
                pass
        
        # 按下ESC键退出
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break

finally:
    # 关闭socket连接
    client_socket.close()
