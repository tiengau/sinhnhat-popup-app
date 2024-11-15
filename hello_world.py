import streamlit as st
import random
import time

# Danh sách màu sắc để áp dụng cho văn bản
text_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Danh sách các thông điệp
messages = [
    "HÉP PI BỚT ĐÂY CHỊ 🐼",  # Đổi thông điệp ở đây
    "CHÚC CHỊ 8386! 💖",
    "VẠN SỰ NHƯ MƠ! 🌸",
    "MÃI ĐỈNH MÃI ĐỈNH! 💪"
]

# Danh sách các hình ảnh bóng bay (hoặc emoji bóng bay)
balloon_emoji = "🎈"  # Hoặc thay thế bằng URL của ảnh bóng bay nếu muốn sử dụng hình ảnh thật

# Kích thước màn hình điện thoại
screen_width = 375  # Chiều rộng màn hình điện thoại
screen_height = 667  # Chiều cao màn hình điện thoại

# Tiêu đề ứng dụng đã sửa đổi
st.title("HACKER ẤN VÀO MẤT NICK 👾🐼")

# Hàm để tạo hiệu ứng loạn xạ
def display_random_effect():
    for _ in range(100):  # Tăng số lần hiển thị lên 100 lần (hoặc thay đổi số lần tùy ý)
        # Chọn màu ngẫu nhiên từ danh sách
        chosen_color = random.choice(text_colors)
        # Chọn thông điệp ngẫu nhiên từ danh sách
        message = random.choice(messages)
        # Chọn vị trí ngẫu nhiên cho thông điệp và bóng bay
        x_position_message = random.randint(0, screen_width - 150)
        y_position_message = random.randint(0, screen_height - 100)
        
        x_position_balloon = random.randint(0, screen_width - 50)
        y_position_balloon = random.randint(0, screen_height - 50)
        
        # Hiển thị lời chúc tại vị trí ngẫu nhiên với màu sắc ngẫu nhiên, không xuống dòng
        st.markdown(
            f'<span style="font-size: 20px; color: {chosen_color}; background-color: pink; '
            f'padding: 10px; border-radius: 10px; position: absolute; top: {y_position_message}px; left: {x_position_message}px;">'
            f'{message}</span>',
            unsafe_allow_html=True
        )
        
        # Hiển thị bóng bay ở vị trí ngẫu nhiên
        st.markdown(
            f'<span style="font-size: 30px; position: absolute; top: {y_position_balloon}px; left: {x_position_balloon}px;">'
            f'{balloon_emoji}</span>',
            unsafe_allow_html=True
        )
        
        time.sleep(0.1)  # Thời gian giữa mỗi lần hiển thị

# Tạo nút để bắt đầu hiệu ứng
if st.button("Nhấn vào đây để nhận 🎁"):
    display_random_effect()

# Footer
st.write("!")
