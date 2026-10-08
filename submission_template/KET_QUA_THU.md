# Kết quả các lượt thử

Thử nghiệm ngày 08/10/2026. Tất cả lượt dưới đây dùng đúng 150 frame đầu, YOLO26n 640 px và lớp người. Các ngưỡng bên trong tracker giữ nguyên mặc định của BoxMOT 10.0.42.

## 1. Video_1 — bảng chấm thử 150 frame

Nhãn và seqLength được giới hạn cùng 150 frame; không dùng bảng này thay cho điểm 600 frame của bản nộp. Số HOTA/MOTA/IDF1 theo thang phần trăm.

| Tracker | conf | iou | HOTA | MOTA | IDF1 | FP | FN | IDSW |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| botsort | 0.15 | 0.5 | 33.563 | 18.432 | 32.763 | 114 | 3026 | 2 |
| botsort | 0.3 | 0.4 | 32.109 | 16.693 | 30.224 | 52 | 3157 | 0 |
| botsort | 0.3 | 0.5 | 32.292 | 17.316 | 30.716 | 70 | 3112 | 3 |
| botsort | 0.3 | 0.7 | 31.232 | 18.458 | 31.822 | 76 | 3060 | 5 |
| botsort | 0.5 | 0.5 | 29.177 | 13.733 | 24.46 | 9 | 3314 | 0 |
| bytetrack | 0.15 | 0.5 | 31.535 | 15.992 | 27.897 | 10 | 3226 | 0 |
| bytetrack | 0.3 | 0.4 | 31.153 | 15.628 | 27.228 | 6 | 3244 | 0 |
| bytetrack | 0.3 | 0.5 | 31.147 | 15.628 | 27.228 | 6 | 3244 | 0 |
| bytetrack | 0.3 | 0.7 | 28.692 | 15.369 | 26.655 | 6 | 3253 | 1 |
| bytetrack | 0.5 | 0.5 | 27.213 | 14.123 | 24.824 | 1 | 3306 | 1 |

## 2. Thống kê đầu ra của 34 lượt thử

Số dòng là tổng hộp có ID được xuất. Số ID là số định danh khác nhau trong file, **không phải** số người thật hoặc số lần đổi ID. Các số này chỉ giúp đối chiếu dữ liệu đã chạy; video_2–video_5 không có nhãn và không được chấm số.

| Video | Tracker | conf | iou | Frame xử lý | Dòng MOT | Số ID khác nhau |
|---|---|---:|---:|---:|---:|---:|
| video_1 | botsort | 0.15 | 0.5 | 150 | 978 | 15 |
| video_1 | botsort | 0.3 | 0.4 | 150 | 784 | 13 |
| video_1 | botsort | 0.3 | 0.5 | 150 | 847 | 15 |
| video_1 | botsort | 0.3 | 0.7 | 150 | 905 | 15 |
| video_1 | botsort | 0.5 | 0.5 | 150 | 561 | 10 |
| video_1 | bytetrack | 0.15 | 0.5 | 150 | 674 | 9 |
| video_1 | bytetrack | 0.3 | 0.4 | 150 | 651 | 9 |
| video_1 | bytetrack | 0.3 | 0.5 | 150 | 651 | 9 |
| video_1 | bytetrack | 0.3 | 0.7 | 150 | 642 | 9 |
| video_1 | bytetrack | 0.5 | 0.5 | 150 | 561 | 10 |
| video_2 | botsort | 0.15 | 0.5 | 150 | 1720 | 21 |
| video_2 | botsort | 0.3 | 0.4 | 150 | 1543 | 23 |
| video_2 | botsort | 0.3 | 0.5 | 150 | 1543 | 23 |
| video_2 | botsort | 0.3 | 0.7 | 150 | 1564 | 24 |
| video_2 | botsort | 0.5 | 0.5 | 150 | 1125 | 14 |
| video_2 | bytetrack | 0.3 | 0.5 | 150 | 1313 | 16 |
| video_3 | botsort | 0.15 | 0.5 | 150 | 844 | 22 |
| video_3 | botsort | 0.3 | 0.4 | 150 | 759 | 23 |
| video_3 | botsort | 0.3 | 0.5 | 150 | 760 | 24 |
| video_3 | botsort | 0.3 | 0.7 | 150 | 877 | 25 |
| video_3 | botsort | 0.5 | 0.5 | 150 | 566 | 17 |
| video_3 | bytetrack | 0.3 | 0.5 | 150 | 593 | 18 |
| video_4 | botsort | 0.15 | 0.5 | 150 | 1037 | 16 |
| video_4 | botsort | 0.3 | 0.4 | 150 | 958 | 18 |
| video_4 | botsort | 0.3 | 0.5 | 150 | 958 | 18 |
| video_4 | botsort | 0.3 | 0.7 | 150 | 958 | 18 |
| video_4 | botsort | 0.5 | 0.5 | 150 | 782 | 12 |
| video_4 | bytetrack | 0.3 | 0.5 | 150 | 809 | 15 |
| video_5 | botsort | 0.15 | 0.5 | 150 | 994 | 27 |
| video_5 | botsort | 0.3 | 0.4 | 150 | 907 | 27 |
| video_5 | botsort | 0.3 | 0.5 | 150 | 907 | 27 |
| video_5 | botsort | 0.3 | 0.7 | 150 | 916 | 28 |
| video_5 | botsort | 0.5 | 0.5 | 150 | 527 | 17 |
| video_5 | bytetrack | 0.3 | 0.5 | 150 | 673 | 20 |

Mỗi lượt có file track, metadata, log, video có ID và ảnh mẫu trong `runs/thu_nghiem/video_N/<cấu_hình>/`. Chi tiết nhận xét theo từng người và cảnh nằm trong báo cáo chính. Các lượt được thực hiện có lúc đồng thời trên một GPU, nên không dùng thời gian của chúng để xếp hạng tốc độ tracker.

## 3. Vì sao giữ iou=0.5

Đã thử 0.4 và 0.7 tại cùng conf=0.3. Trên video_1, HOTA thử của BoT-SORT lần lượt là 32.109, 32.292 và 31.232 cho iou=0.4, 0.5 và 0.7. Các frame mẫu của bốn video còn lại chưa cho thấy lợi ích đủ rõ để đổi khỏi 0.5. Kết quả phụ thuộc cả loại tracker và confidence; không suy ra rằng iou lớn hơn luôn tốt hơn.
