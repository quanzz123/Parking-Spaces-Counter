# 🚗 Parking Space Detection with OpenCV

Dự án này là một hệ thống giám sát bãi đỗ xe đơn giản được xây dựng bằng **Python** và **OpenCV**.  
Chương trình sẽ phát hiện chỗ trống và chỗ đã có xe trong bãi đỗ thông qua video.
## Images
![Markdown Logo](https://github.com/quanzz123/Parking-Spaces-Counter/blob/main/result.png)

---

## 📂 Cấu trúc Project

- **carParkPicker.py**  
  - Dùng để chọn và lưu vị trí các ô đỗ xe thủ công.  
  - Chuột trái: thêm ô đỗ xe.  
  - Chuột phải: xóa ô đỗ xe.  
  - Các tọa độ được lưu trong file `carParkPos` bằng `pickle`.

- **main.py**  
  - Đọc danh sách vị trí ô đỗ từ `carParkPos`.  
  - Xử lý video `carPark.mp4` từng khung hình.  
  - Áp dụng các bước xử lý ảnh: **grayscale, blur, adaptive threshold, median blur, dilation**.  
  - Kiểm tra từng ô và hiển thị:  
    - Ô màu xanh lá = chỗ trống.  
    - Ô màu đỏ = có xe.  
    - Hiển thị số pixel (debug).  
    - Tổng số chỗ trống còn lại.

---

## 🛠️ Yêu cầu

- Python 3.x
- OpenCV
- NumPy
- cvzone (tùy chọn)

Cài đặt thư viện:

```bash
pip install opencv-python numpy cvzone
▶️ Cách chạy
1. Chọn chỗ đỗ xe
Chạy script chọn vị trí trên ảnh tĩnh carParkImg.png:

bash
Copy code
python carParkPicker.py
Nhấn chuột trái để thêm vị trí.

Nhấn chuột phải để xóa vị trí.

Nhấn q để thoát.

👉 Kết quả: tọa độ các chỗ đỗ được lưu trong file carParkPos.

2. Phát hiện chỗ trống
Chạy chương trình chính:

bash
Copy code
python main.py
Chương trình sẽ phân tích video carPark.mp4.

Các ô trống sẽ được đánh dấu màu xanh, ô có xe đánh dấu màu đỏ.

Góc trên màn hình hiển thị tổng số chỗ trống.

Nhấn q để thoát.

📸 Demo
Chọn chỗ đỗ xe

Kết quả phát hiện

📌 Ghi chú
Có thể chỉnh width và height để phù hợp kích thước chỗ đỗ trong video/ảnh.

Ngưỡng count < 900 có thể cần điều chỉnh tùy chất lượng video.

Làm việc tốt nhất với camera cố định.


