import pyautogui
import time
import keyboard  # Cần cài thư viện này bằng `pip install keyboard`
import pyperclip  # Cần cài thư viện này bằng `pip install pyperclip`
import threading

# Cờ để theo dõi trạng thái dừng
stop_flag = False

def esc_listener():
    """Luồng lắng nghe phím ESC."""
    global stop_flag
    while not stop_flag:
        if keyboard.is_pressed("esc"):
            stop_flag = True
            print("Nhấn ESC để dừng chương trình.")

def main():
    global stop_flag
    try:
        # Khởi chạy luồng lắng nghe phím ESC
        listener_thread = threading.Thread(target=esc_listener, daemon=True)
        listener_thread.start()

        # Nhập số lượng tin nhắn
        so_luong_tin_nhan = int(input("Nhập số lượng tin nhắn cần gửi: "))
        if so_luong_tin_nhan <= 0:
            print("Số lượng tin nhắn phải là số nguyên dương.")
            return

        # Nhập danh sách tin nhắn
        messages = []
        for i in range(so_luong_tin_nhan):
            message = input(f"Nhập tin nhắn thứ {i + 1}: ")
            if not message.strip():
                print("Tin nhắn không được để trống.")
                return
            messages.append(message)

        # Nhập thời gian delay giữa các lần gửi
        delay = float(input("Nhập thời gian delay (giây): "))
        if delay < 0:
            print("Thời gian delay phải là số không âm.")
            return

        # Nhập tổng số lần gửi toàn bộ danh sách tin nhắn
        so_lan_gui = int(input("Nhập tổng số lần gửi toàn bộ danh sách tin nhắn: "))
        if so_lan_gui <= 0:
            print("Số lần gửi phải là số nguyên dương.")
            return

        print("Di chuột vào vị trí nhập tin nhắn...")
        print("Bắt đầu gửi tin nhắn trong...")
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)

        # Lấy vị trí hiện tại của chuột
        x, y = pyautogui.position()
        print(f"Vị trí chuột được ghi nhận: ({x}, {y})")

        # Tiến hành gửi tin nhắn
        print("Bắt đầu spam tin nhắn... Nhấn 'ESC' để dừng.")
        for i in range(so_lan_gui):  # Lặp lại toàn bộ danh sách tin nhắn
            for message in messages:  # Gửi từng tin nhắn trong danh sách
                if stop_flag:  # Kiểm tra cờ dừng
                    print("Dừng chương trình theo yêu cầu của người dùng.")
                    return
                pyperclip.copy(message)  # Sao chép nội dung tin nhắn vào clipboard
                pyautogui.click(x, y)  # Click vào vị trí nhập tin nhắn
                time.sleep(0.1)  # Chờ để ổn định vị trí
                pyautogui.hotkey("ctrl", "v")  # Dán nội dung từ clipboard
                time.sleep(0.2)  # Chờ để nội dung dán hoàn tất
                pyautogui.press("enter")  # Nhấn Enter để gửi
                time.sleep(delay)  # Chờ trước khi gửi tin nhắn tiếp theo
                print(f"Đã gửi tin nhắn '{message}' lần {i + 1}/{so_lan_gui}")

        print("Hoàn thành quá trình gửi tin nhắn.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ cho thời gian delay và số lần gửi.")
    except KeyboardInterrupt:
        print("Chương trình đã bị dừng bởi người dùng.")

if __name__ == "__main__":
    main()
