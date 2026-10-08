# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** Bài thực hiện cá nhân
**Thành viên:** Bùi Đức Thông — 2A202602931
**Ngày thực hiện:** 08/10/2026

Detector cố định: `yolo26n.pt`, ảnh đầu vào 640 px, chỉ lớp người (`classes=[0]`). Re-ID cố định: `osnet_x0_25_msmt17.pt`. Không thay trọng số hoặc các ngưỡng nội bộ của tracker.

## 1. Cấu hình đã chọn

Mỗi video thử ByteTrack và BoT-SORT trên cùng 150 frame đầu ở `conf=0.3, iou=0.5`. Với BoT-SORT, thử thêm `conf=0.15/0.5` và `iou=0.4/0.7`; mỗi lượt chỉ đổi một tham số từ cấu hình gốc. Riêng video_1 còn quét cùng các ngưỡng cho ByteTrack và chạy đủ 600 frame cho hai ứng viên. Chi tiết từng lượt có trong [KET_QUA_THU.md](KET_QUA_THU.md).

| Video | Tracker | conf | iou | Quan sát khi xem frame có ID | Đã thử nhưng loại |
|---|---|---:|---:|---|---|
| video_1 — quảng trường, tĩnh, ban ngày | BoT-SORT | 0.15 | 0.5 | Thêm hộp người phía xa so với ByteTrack, nhưng người áo tím vẫn đổi ID. HOTA/IDF1 đầy đủ cao hơn ứng viên ByteTrack. | ByteTrack 0.15/0.5: HOTA 27.314 so với 28.113; BoT-SORT 0.5/0.5 bỏ nhiều người xa trong lượt thử. |
| video_2 — phố đêm, tĩnh, đông | BoT-SORT | 0.15 | 0.5 | Trong lượt thử, người áo trắng bên trái cột đèn giữ ID 8 ở frame 25, 75, 125, 150; nhiều người tối hoặc bị che vẫn thiếu hộp. | ByteTrack 0.3/0.5: cùng người đó đổi 17 → 25; BoT-SORT 0.5/0.5 mất hộp của nhiều người rõ ở frame 125–150. |
| video_3 — camera di động, ảnh nhỏ | BoT-SORT | 0.3 | 0.5 | Lượt thử giữ ID 1 cho người áo sọc và ID 2 cho người áo xám ở bốn frame mẫu; hộp người xa và sát mép ảnh còn nhấp nháy. | ByteTrack 0.3/0.5 cũng giữ được hai người lớn nhưng thiếu thêm người nhỏ phía sau ở frame 125; BoT-SORT 0.15/0.5 thêm hộp nhỏ quanh vùng bị che, chưa cho lợi ích ID rõ ở người gần. |
| video_4 — trong nhà, camera tiến tới | BoT-SORT | 0.3 | 0.5 | Lượt thử giữ ID 2 cho người áo đỏ và ID 6 cho người áo trắng qua frame 25–150; người xa còn bị che bởi hai người này. | ByteTrack 0.3/0.5 vẫn bám người gần tốt, nhưng người phía trái sau cô gái tiền cảnh bị ngắt hộp; BoT-SORT 0.15/0.5 thêm hộp yếu phía xa mà chưa cải thiện ID hai người chính. |
| video_5 — xe bus, giao lộ | BoT-SORT | 0.15 | 0.5 | Cấu hình ngưỡng thấp ưu tiên người nhỏ ở hai vỉa hè; camera đổi góc làm nhiều track kết thúc hoặc xuất hiện lại. Quan sát chi tiết ghi ở mục 3. | ByteTrack 0.3/0.5: còn ít hộp trong bóng râm và người xa; BoT-SORT 0.5/0.5 loại thêm các hộp yếu. |

Các ID trong bảng là ID của từng lượt thử, không phải ID nhãn thật. ID có thể khác giữa các lần chạy. Các lựa chọn cho video_2–video_5 dựa trên kiểm tra bằng mắt; không khẳng định chúng tối ưu toàn bộ video khi không có nhãn.

## 2. Số liệu video_1

Bản nộp chạy **đủ 600 frame**, không giới hạn frame. Chấm bằng `scripts/evaluate_practice.py`, tên lần chấm `buiducthong_video1`, đúng nhãn gốc video_1. Số được in theo thang phần trăm của TrackEval:

| Cấu hình chạy đủ 600 frame | HOTA | MOTA | IDF1 | FP | FN | IDSW |
|---|---:|---:|---:|---:|---:|---:|
| ByteTrack, conf=0.15, iou=0.5 | 27.314 | 18.314 | 26.987 | 118 | 15.047 | 13 |
| **BoT-SORT, conf=0.15, iou=0.5 — bản nộp** | **28.113** | **20.725** | **28.742** | **506** | **14.197** | **27** |

Trích output thực tế của bản nộp:

```text
HOTA: buiducthong_video1-pedestrianHOTA      DetA      AssA      DetRe     DetPr     AssRe     AssPr     LocA      OWTA      HOTA(0)   LocA(0)   HOTALocA(0)
video_1                            28.113    19.221    41.449    19.946    75.792    45.752    76.514    82.779    28.683    35.051    76.834    26.931

CLEAR: buiducthong_video1-pedestrianMOTA      MOTP      MODA      CLR_Re    CLR_Pr    MTR       PTR       MLR       sMOTA     CLR_TP    CLR_FN    CLR_FP    IDSW      MT        PT        ML        Frag
video_1                            20.725    80.377    20.871    23.594    89.652    12.903    20.968    66.129    16.096    4384      14197     506       27        8         13        41        72

Identity: buiducthong_video1-pedestrianIDF1      IDR       IDP       IDTP      IDFN      IDFP
video_1                            28.742    18.153    68.978    3373      15208     1517
```

Output đầy đủ nằm tại `runs/nop_bai/video_1_cham.log`. Bảng thử trên 150 frame đầu được lưu riêng và không dùng thay cho điểm bản nộp. Không chấm hoặc điền HOTA/MOTA/IDF1 cho video_2–video_5.

## 3. Phân tích

### Video_1: chọn theo HOTA nhưng vẫn có lỗi ID

ByteTrack giữ ID của các người gần camera khá ổn trong đoạn thử; ở BoT-SORT, người áo tím đổi từ ID 3 sang 37 giữa frame 75 và 150, rồi mang ID 50 tại frame 450 trong bản đầy đủ. Tuy nhiên, trên toàn bộ 600 frame, BoT-SORT giảm 850 lượt bỏ sót so với ByteTrack ở cùng ngưỡng 0.15/0.5, đồng thời tăng 388 hộp giả và 14 lần đổi ID. HOTA cao hơn 0.799 điểm và IDF1 cao hơn 1.755 điểm nên chọn BoT-SORT theo tiêu chí tổng hợp của bài. DetA 19.221 thấp hơn AssA 41.449 và FN còn 14.197, cho thấy chất lượng phát hiện là hạn chế lớn của cấu hình này. Re-ID không thể phục hồi người mà detector không phát hiện, cũng không bảo đảm tránh mọi lần đổi danh tính.

### Video_2: ngưỡng thấp giúp người tối nhưng không giải quyết mọi che khuất

Ở các frame thử 25, 75, 125, 150, BoT-SORT 0.15/0.5 giữ ID 8 cho người áo trắng đi bên trái cột đèn, trong khi ByteTrack 0.3/0.5 đổi người này từ ID 17 sang 25. BoT-SORT 0.3/0.5 cũng đổi từ ID 8 sang 13 ở cùng đoạn, nên giảm confidence có lợi rõ ở trường hợp được quan sát này. Ngưỡng 0.5 làm mất nhiều hộp của người áo tối hoặc đang đi cạnh người khác, dù ảnh vẫn nhìn thấy người. Camera tĩnh giúp dự đoán chuyển động dễ hơn, nhưng mật độ cao và ánh sáng không đều làm các hộp yếu hoặc đứt đoạn; BoT-SORT kết hợp matching hộp yếu với đặc trưng ngoại hình để giữ track. Trong bản đầy đủ, người áo trắng vẫn mang ID 8 tại frame 525; người đứng bên phải ô tô giữ ID 4 ở các frame mẫu từ 25 đến 1.050. Không có nhãn nên không biến các quan sát này thành số lần IDSW của cả video.

### Video_3: chuyển động camera và độ phân giải thấp

Trong lượt thử, cả hai tracker giữ được hai người lớn phía trước; BoT-SORT 0.3/0.5 giữ ID 1 cho người áo sọc, ID 2 cho người áo xám, và còn có hộp cho một số người phía sau ở frame 125 mà baseline thiếu. Ngưỡng 0.15 thêm hộp nhỏ quanh người bị che và sát mép ảnh, còn 0.5 giảm các hộp yếu; chọn 0.3 để giữ cân bằng. Về cơ chế, bù chuyển động camera của BoT-SORT giúp tách dịch chuyển do camera khỏi dịch chuyển của người, phù hợp hơn giả định chỉ dự đoán chuyển động ảnh. Bản đầy đủ vẫn giữ ID 1, 2 và 17 cho ba người gần camera tới frame mẫu 209; khi camera chuyển sang đoạn phố tiếp theo, các track nhỏ và bị che còn gián đoạn, nhiều ID mới xuất hiện. Ngoại hình của người nhỏ, mờ hoặc chỉ lộ một phần vẫn không đáng tin như người gần camera.

### Video_4: theo người chính, kiểm tra vùng kính và nền bóng

Người áo đỏ và người áo trắng giữ ID 2 và 6 trong các frame mẫu của BoT-SORT 0.3/0.5; baseline ByteTrack cũng theo tốt hai người này. BoT-SORT giữ thêm hộp của người phía trái sau cô gái gần camera trong lượt thử, trong khi baseline có khoảng mất hộp. Chọn 0.3 thay cho 0.15 vì các hộp thêm ở phía xa chưa mang lại cải thiện danh tính rõ cho hai người chính, và chọn ngưỡng trung bình cho cảnh có kính, nền bóng. Camera tiến tới làm kích thước hộp thay đổi liên tục; bù camera và ngoại hình có cơ sở phù hợp với cảnh này. Bản đầy đủ bộc lộ giới hạn: người áo trắng mang ID 6 ở frame 225 nhưng ID 49 ở frame 450; người áo đỏ mang ID 2 tới frame mẫu 675 rồi ID 99 ở frame 900. Không khẳng định mọi hộp ở vùng phản chiếu đều là hộp giả chỉ dựa vào vị trí của chúng.

### Video_5: ưu tiên người nhỏ, vẫn khó khi xe đổi hướng

Trong lượt thử ở 0.3/0.5, người áo đỏ bên phải giữ ID 2 từ frame 25 đến 125 với BoT-SORT; baseline cũng giữ người này nhưng thiếu thêm hộp của các người trong bóng râm bên trái. Ngưỡng thấp được chọn để giữ thêm tín hiệu của người nhỏ trên vỉa hè, thay vì loại phần lớn hộp yếu khi đặt 0.5. Camera trên xe làm toàn cảnh dịch chuyển và thay đổi tỷ lệ; BoT-SORT có bù chuyển động camera và Re-ID, phù hợp về cơ chế với tình huống này. Người rời khỏi trường nhìn cần kết thúc track, nên ID mới xuất hiện ở cuối video chưa đủ chứng minh đổi ID của cùng một người. Ở bản đầy đủ, frame 375 còn theo được nhóm người sát giao lộ bên phải, nhưng nhiều người xa chưa có hộp; frame 562–750 đã chuyển sang phố khác, có hộp cho người gần camera và bỏ sót một phần người rất nhỏ phía xa. Các đoạn xe rung, quay góc và người bị cột hoặc biển báo che vẫn là điểm cần xem lại.

## 4. Nếu có thêm thời gian

Giữ nguyên detector và Re-ID của bài, thử OC-SORT hoặc DeepOCSORT ở các đoạn camera quay mạnh, rồi quét `conf` mịn hơn quanh 0.15–0.3. Với video_1, ưu tiên kiểm tra các frame bỏ sót người nhỏ và đoạn người áo tím đổi ID; chỉ xét đổi mô hình Re-ID sau bài nộp chính như một thử nghiệm mở rộng.

## 5. Kiểm tra trước khi nộp

Các file `video_1.txt` đến `video_5.txt` ở `runs/nop_bai/` dùng định dạng MOT 10 cột. Mỗi video chạy lại không giới hạn frame; `_meta.json` lưu cấu hình và số frame đã xử lý, `kiem_tra.json` lưu kiểm tra định dạng và số frame giải mã được từ video xem thử. Tổng số ảnh nguồn và frame đã xử lý đều là **4.137**. Cả năm video xem thử giải mã đủ frame; mọi dòng MOT đủ 10 cột, tọa độ hữu hạn, kích thước hộp dương, ID nguyên dương, frame tăng dần và không trùng ID trong cùng frame.

| File | Frame nguồn / xử lý / video xuất | Dòng MOT | Định dạng |
|---|---:|---:|---|
| video_1.txt | 600 / 600 / 600 | 5180 | Hợp lệ |
| video_2.txt | 1050 / 1050 / 1050 | 13821 | Hợp lệ |
| video_3.txt | 837 / 837 / 837 | 4761 | Hợp lệ |
| video_4.txt | 900 / 900 / 900 | 6218 | Hợp lệ |
| video_5.txt | 750 / 750 / 750 | 3391 | Hợp lệ |

Ảnh minh chứng từ bản đầy đủ nằm ở `runs/nop_bai/video_N_minh_chung.jpg`. Trong gói ZIP nộp bài, các ảnh này nằm trong thư mục `minh_chung/`; log chấm và metadata cũng được kèm theo. Video xem thử đầy đủ được giữ trong `runs/nop_bai/`.

Notebook ôn metric đã chạy xong, ba đáp án `True/False/True` đều đúng. Ở ảnh đầu video_1, YOLO cho 14/6/5 hộp khi `conf=0.15/0.3/0.5`, giữ `iou=0.5`. Tám kiểm thử của repo đã pass; môi trường và các sửa lỗi cần để chạy được mô tả trong [THUC_HIEN.md](THUC_HIEN.md).
