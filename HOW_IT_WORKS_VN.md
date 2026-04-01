# Hướng Dẫn Dành Cho Người Dùng: Luồng Hoạt Động Của Trợ Lý VinDynamic AI

Tài liệu này giải thích cách hoạt động của hệ thống trí tuệ nhân tạo (AI) VinDynamic bằng ngôn ngữ đơn giản, minh họa bằng các ví dụ dễ hiểu trong đời thực. Cốt lõi của hệ thống giống như **một tòa soạn báo thu nhỏ gồ 3 nhân viên xuất sắc**.

---

## Bước 1: Thu thập Tin Tức (Người Gom Báo)
Mỗi ngày, có hàng nghìn bài viết trên Internet. Thay vì bạn phải tự đọc từng trang, hệ thống sẽ phái một "người gom báo" đi làm nhiệm vụ:
- Người này mang theo **Danh sách Trang web** (RSS Sources) mà bạn đã chỉ định.
- Họ mang theo một **Danh sách Từ khóa** bắt buộc (như "robot", "vietnam", "automation").
- Họ dạo quanh các trang web. Nếu bài báo nào có chứa từ khóa trong danh sách thì họ sẽ lưu lại. Nếu bài báo nói về các quốc gia Đông Nam Á (như Việt Nam, Singapore...), họ dán thêm nhãn màu đỏ **"Tin Địa Phương"**. Còn lại họ dán nhãn xanh **"Tin Toàn Cầu"**.
- Cuối cùng, họ vứt đi những bài báo mà hệ thống đã từng đọc vào các ngày trước (nhờ vào cuốn sổ Lịch sử `history.json`), chỉ giữ lại **tin tức hoàn toàn mới tinh**.

---

## Bước 2: Tóm Tắt Nhanh (Thư Ký Đọc Nhanh - Stage 1)
Lúc này, tòa soạn có thể rinh về hàng chục bài báo dài lê thê. Đưa tất cả cho Biên tập viên trưởng đọc sẽ rất tốn thời gian (và tốn tiền mô hình AI xử lý).
- Hệ thống giao xấp báo này cho một "Thư ký tốc ký" (Sử dụng AI cấp thấp tên là Haiku - rất nhanh nhạy và chi phí siêu rẻ).
- Thư ký này sẽ đọc tất cả, băm nhỏ thông tin và tóm tắt thành các gạch đầu dòng ngắn nhất có thể. Họ ghi chú rõ mỗi ý được lấy từ trang web nào.

---

## Bước 3: Cập Nhật Trí Nhớ (Người Thủ Thư - Stage 2)
Sau khi Thư ký làm xong, bản tóm tắt được chuyển cho "Người Thủ Thư" (Cũng sử dụng AI Haiku).
- Người Thủ Thư giữ một cuốn sổ tay khổng lồ tên là **"Knowledge Base" (Bộ Não Tri Thức)**. Cuốn sổ này ghi nhớ mọi diễn biến thị trường từ trước đến nay.
- Thủ Thư sẽ lấy thông tin mới của ngày hôm nay chép thêm vào sổ. Ý nào mới tinh, họ sẽ lấy bút dạ quang bôi đậm chữ `[NEW]`. Tin nào đã cũ rích, họ sẽ tẩy đi cốt để cuốn sổ luôn mỏng nhẹ, tránh bị quá tải thông tin.

---

## Bước 4: Viết Báo Cáo Chiến Lược (Chuyên Gia Phân Tích - Stage 3)
Đây là lúc nhân vật quan trọng nhất xuất hiện: **Chuyên gia Phân tích Cấp cao** (Sử dụng AI thông minh nhất - Sonnet 3.5).
- Chuyên gia này không thèm đọc các bài báo nhảm nhí bên ngoài. Họ **chỉ làm việc dựa trên cuốn sổ "Knowledge Base"** dày dặn kinh nghiệm do Người Thủ Thư đưa cho.
- Nhờ có cuốn sổ chứa đầy [Tin Toàn Cầu] và [Tin Địa Phương], Chuyên gia bắt đầu chắp bút viết ra bản **Báo Cáo Tình Báo Thị Trường (Intelligence Briefing)** hoàn mỹ:
  - Ngay ở phần đầu, chuyên gia tóm lược xu hướng thị trường Toàn Cầu.
  - Sau đó, họ tách những thông tin được dán nhãn "Tin Địa Phương" để viết hẳn một phần riêng mang tên *SEA & Vietnam Spotlight*.
  - Cuối cùng, họ đưa ra các lời khuyên Hành động (Implications) cho ban lãnh đạo công ty. 
  - Mọi thông tin viết ra đều được Chuyên gia **trích dẫn nguồn minh bạch** theo format chuẩn quốc tế (ví dụ: *Nguồn: TechCrunch* in nghiêng ở dưới mỗi ý).

---

## Bước 5: Đóng Gói (Xuất File PDF)
Máy in của phần mềm sẽ tự động lấy bài Diễn giải xuất sắc của Chuyên gia, thiết kế lại thành văn bản chỉnh chu có tiêu đề, màu sắc rõ ràng và đóng gói thành một tệp PDF tên là `VinDynamic_Strategy_Day_Month_Year.pdf` để bạn dễ dàng gửi Mail báo cáo cho sếp hoặc lưu trữ nội bộ!

> **Tóm lại lợi ích cốt lõi:** Luồng hoạt động này vừa giúp hệ thống **không bao giờ quên tin tức cũ**, luôn rạch ròi giữa **tin trong nước và quốc tế**, lại **tiết kiệm tiền tối đa** do đã để nhân viên cấp thấp (Haiku) gánh phần lớn công việc cực nhọc, chỉ dùng Chuyên gia (Sonnet) đúng một lần duy nhất lúc xuất bản báo cáo.
