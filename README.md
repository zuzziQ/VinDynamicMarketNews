# 🤖 VinDynamic Intelligence Agent

**VinDynamic Intelligence Agent** là một hệ thống Trí Tuệ Nhân Tạo (AI Agent) tự động hóa, được thiết kế chuyên biệt cho việc thu thập, lọc và phân tích thông tin tình báo thị trường (Market Intelligence) trong lĩnh vực **Robotics, Tự động hóa công nghiệp (Automation), và AI** tại khu vực Đông Nam Á và toàn cầu.

Hệ thống đóng vai trò như một chuyên gia phân tích cấp cao (Senior Market Research Analyst), tự động theo dõi hàng chục trang báo, tạp chí công nghệ, trang gọi vốn mỗi ngày để đúc kết ra những báo cáo tóm tắt mang tính chiến lược cao (Actionable Intelligence Briefing).

---

## 🌟 Tính năng Nổi Bật (Features)
1. **Đa luồng nguồn cấp dữ liệu (Multi-Source RSS):** Thu thập dữ liệu song song từ 8+ trang tin tức hàng đầu thế giới (IEEE Spectrum, TechCrunch, The Robot Report, Tech In Asia...).
2. **Siêu tối ưu Chi phí (Pre-filtering Keywords):** Tích hợp bộ lọc từ khóa địa phương hóa (*Vietnam, ASEAN, AMR, Cobot...*). Chỉ những bài báo vượt qua bộ lọc khắt khe mới lộ diện gửi đi phân tích. Thuật toán này giúp tiết kiệm đến 90% chi phí Token API.
3. **Bảo vệ Vùng Giới hạn Rate-Limit (Batch Chunking):** Thuật toán chia lô tự động (Batching) kết hợp cơ chế nghỉ linh hoạt (Sleep delay) giúp Agent linh hoạt luồn lách qua các giới hạn API khắc nghiệt của nhóm tài khoản Tier 1, đảm bảo quá trình cào không bao giờ sụp đổ giữa phiên.
4. **Hồn cốt Chuyên gia (Persona Injection):** Được "hun đúc" bằng System Prompt cực mạnh của `VinDynamic`: Không sử dụng thuật ngữ sáo rỗng, tập trung xoáy sâu vào các đối thủ đánh chặn trực tiếp (KUKA, ABB, Universal Robots...), chú trọng số liệu cứng.

---

## 🛠️ Yêu Cầu Cần Có (Prerequisites)

Để hệ thống thức tỉnh, bạn cần đảm bảo các môi trường và tài khoản sau:
* **Hệ Điều Hành:** Windows / Linux / MacOS.
* **Ngôn Ngữ:** Python 3.10 trở lên.
* **Tài khoản & API Keys:**
  * **(Bắt buộc):** `Anthropic API Key` (Để trao quyền suy tủy cho hệ thống qua mô hình Claude 3.5 Sonnet). Bạn cần nạp $5 Credit tối thiểu vào Anthropic Console để kích hoạt kết nối.
  * **(Tùy chọn - Kênh phân phối):** `Notion Token` (Lưu data dài hạn làm Data Warehouse), `Slack Webhook URL` (Bắn chớp nhoáng cảnh báo dị thường), `SendGrid API Key` (Lên súng gửi email báo cáo mỗi sáng).

---

## ⚙️ Hướng Dẫn Cài Đặt (Installation)

1. **Truy cập không gian làm việc:**
   Dùng Terminal hoặc Command Prompt di chuyển vào gốc dự án:
   ```bash
   cd h:\ai-folder\new
   ```

2. **Khởi tạo không gian cách ly (Virtual Environment):**
   ```bash
   python -m venv venv
   # Kích hoạt trên Windows:
   venv\Scripts\activate
   # Kích hoạt trên Mac/Linux:
   source venv/bin/activate
   ```

3. **Tải nạp Động cơ cốt lõi:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Bộ lõi trung tâm bao gồm: `feedparser`, `beautifulsoup4`, `python-dotenv`, `anthropic`).*

4. **Khu vực Bí mật (Environment Variables):**
   * Đổi tên file vỏ bảo mật từ `.env.example` thành `.env`.
   * Mở file `.env` vừa đổi tên bằng Notepad, dán các Key tương ứng mà bạn đang sở hữu. **Khuyến cáo An ninh:** Tuyệt đối không sao lưu file này lên bất kỳ hệ thống Git Tracking công cộng nào.

---

## 🚀 Hướng Dẫn Sử Dụng (Usage)

**Bước 1: Tùy biến Khối Não của Agent (`config.py`)**  
Cốt tủy của Agent nằm ở file `config.py`. Tại đây, bạn hoàn toàn có thể tái định vị Agent bằng cách chỉnh sửa:
* Danh sách `RSS_FEEDS` (Quyết định xem Agent đi săn mồi ở trang nào).
* Array `KEYWORDS` (Linh hồn bộ lọc: Nếu muốn Agent chuyển sang phân tích Tài chính hoặc Y Tế, thay keyword ở đây).
* Dòng văn xuôi `ANALYST_PERSONA` (Yêu cầu Agent hành xử theo các chuẩn định công ty bạn, ví dụ chuyển góc độ sang một kỹ sư phần cứng phân tích linh kiện thay cho nhà đầu tư).

**Bước 2: Kích hoạt Pipeline**  
Trực tiếp kích nổ khối thu thập dữ liệu trên Terminal:
```bash
python test_rss_pipeline.py
```

**Bước 3: Truy xuất Insight Kết Quả**  
Hệ thống sẽ chạy hiển thị các lệnh Command line siêu việt (Logging): *Fetching -> Dediplicating -> Pre-filtering -> Batch 1 -> Batch 2...*
Đầu ra đích xác cuối cùng (trong cấu trúc thực tế) sẽ là một file định dạng chuẩn hóa JSON cực sạch và bản Báo cáo đánh giá tóm tắt kiểu Markdown được đẩy đến từng ứng dụng cá nhân hóa.

---
_Engineered for Market Intelligence - Applied Robotics Sector 🇻🇳 (ASEAN)_
