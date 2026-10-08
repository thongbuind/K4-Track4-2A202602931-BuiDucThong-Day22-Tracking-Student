# Nhật ký thực hiện và chạy lại bài lab

Thực hiện ngày 08/10/2026 trên macOS Apple Silicon. Dữ liệu, trọng số, TrackEval, môi trường Python và video kết quả được lưu cục bộ; các thư mục này nằm trong `.gitignore`.

## Môi trường đã dùng

Môi trường riêng `.lab_env_clean` dùng Python 3.11.17, Ultralytics 8.4.174, BoxMOT 10.0.42, PyTorch 2.5.1, TorchVision 0.20.1, NumPy 1.26.4, OpenCV 4.11.0.86 và TrackEval cài từ bản clone cục bộ. Môi trường conda `cv_robotics_lab21` chưa có trên máy; môi trường riêng được dùng để hoàn thành bài mà không thay đổi các môi trường conda sẵn có.

BoxMOT 10.0.42 khai báo NumPy 1.23.1, phiên bản này thiếu wheel cho Python 3.11 trên máy. Vì vậy đã cài BoxMOT bằng `--no-deps` sau khi cài các thư viện chạy cần thiết và NumPy 1.26.4. Pin `setuptools<81` vì BoxMOT còn dùng `pkg_resources`. Toàn bộ lượt tracking và chấm số đều chạy thành công với môi trường này.

```bash
export LAB_DATA="$PWD/lab_data"
export MPLCONFIGDIR=/private/tmp/lab_mpl
export YOLO_CONFIG_DIR=/private/tmp/lab_yolo
source .lab_env_clean/bin/activate
python scripts/check_data.py --lab-data-root "$LAB_DATA"
pytest
```

## Chuẩn bị dữ liệu

Gói tải từ liên kết giảng viên trong README có thư mục gốc `data_lab21`; đã đổi tên cục bộ thành `lab_data`. Số ảnh lần lượt là 600, 1.050, 837, 900 và 750, tổng cộng 4.137 ảnh. Chỉ `video_1` có `gt/gt.txt`. Gói này không có thư mục `preview` và thiếu `video_1/eval_config.json`. Đã tạo cấu hình chấm cục bộ từ tiền tố `name` trong `seqinfo.ini` của video luyện và đặt `split=train`; không thay đổi nhãn.

Video xem thử được tạo trực tiếp từ ảnh và file track. Không dùng file detection có sẵn trong gói: mọi hộp đầu vào tracker đều do detector cố định `yolo26n.pt` sinh ra ở `imgsz=640`, `classes=[0]`.

## Notebook và thử nghiệm

Notebook `on_tap_metrics.ipynb` đã chạy tất cả ô, lưu cả ảnh và output. Đáp án ba nhận định là `True`, `False`, `True`. Trên ảnh đầu `video_1`, `conf=0.15/0.3/0.5` cho 14/6/5 hộp người với `iou=0.5`.

Mỗi video có lượt thử 150 frame đầu cho ByteTrack và BoT-SORT ở `conf=0.3, iou=0.5`. BoT-SORT được thử tiếp với `conf=0.15/0.5` và `iou=0.4/0.7`, mỗi lượt chỉ thay một ngưỡng so với cấu hình gốc. Riêng `video_1`, ByteTrack cũng được thử cùng bốn biến thể vì baseline giữ ID tốt cho các người gần camera.

Kết quả thử nằm trong `runs/thu_nghiem/video_N/<tracker>_c<conf>_i<iou>/`. Mỗi lượt có `.txt`, `_meta.json`, `_preview.mp4`, `chay.log` và ảnh đối chiếu `so_sanh.jpg`. Các số trong bảng thử chỉ mô tả đầu ra; số ID được tạo không phải số lần đổi ID.

Chấm thử trên 150 frame chỉ áp dụng `video_1`: nhãn gốc được lọc tới frame 150 trong `runs/nhan_thu/video_1`, đồng thời `seqLength` được đặt thành 150 để không tính các frame chưa chạy là bỏ sót. Các số thử được tách khỏi bảng chấm đầy đủ của bản nộp. Hai ứng viên của `video_1` còn được chạy và chấm trên đủ 600 frame trước khi chọn.

## Script đã sửa để chạy thực tế

- `run_tracking.py`: chuyển detector và Re-ID sang thiết bị được chọn, truyền `torch.device` cho BoxMOT; dừng khi ảnh không đọc được; ghi tiến độ và metadata số frame, ngưỡng, thời gian.
- `evaluate_practice.py`: dùng đúng `split` khi chuẩn bị dữ liệu; vá alias NumPy trong chính tiến trình con chấm điểm và đưa thư mục TrackEval vào đường dẫn import.
- `pytest.ini`: chỉ thu thập kiểm thử của lab trong `tests`, tránh chạy nhầm bộ test cần dữ liệu của bản clone TrackEval.

Tám kiểm thử đã pass, không dùng GPU, ảnh lab hay mạng. Các kiểm thử mới xác nhận thiết bị được truyền đúng, đủ frame được ghi, ảnh lỗi không bị âm thầm bỏ qua và dữ liệu chấm đi vào đúng `split`.

## Bản nộp và đánh giá

Cấu hình cuối, số liệu và nhận xét nằm trong `BAO_CAO_mau.md`. Chạy lại mỗi video theo bảng cấu hình, bỏ `--max-frames`:

```bash
python scripts/run_tracking.py \
  --source "$LAB_DATA/video_N/img1" --seq-name video_N \
  --tracker TRACKER --conf CONF --iou IOU \
  --device mps --out runs/nop_bai --save-video
```

Trên máy không có GPU Metal, dùng `--device cpu`; số học dấu phẩy động và thời gian chạy có thể khác. Khi chấm bản nộp:

```bash
python scripts/evaluate_practice.py \
  --trackeval-root TrackEval --lab-data-root "$LAB_DATA" \
  --submission runs/nop_bai/video_1.txt --run-name buiducthong_video1
```

Không chấm số hoặc thêm nhãn cho `video_2`–`video_5`. Quan sát các video đó bằng frame có vẽ ID và các đoạn liên tiếp trong video xem thử.
